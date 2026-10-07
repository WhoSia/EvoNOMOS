#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "zlib.h"

#define DICT_SIZE 32768
#define PLAIN_SIZE 4096
#define COMP_SIZE 8192
#define OUT_SIZE 8192

static void fill_dictionary(unsigned char *dict) {
    for (size_t i = 0; i < DICT_SIZE; i++) {
        dict[i] = (unsigned char)(((i * 131u) + 17u) % 251u);
    }
}

static int compress_with_dictionary(
    const unsigned char *dict,
    const unsigned char *plain,
    unsigned char *comp,
    uLong *comp_len
) {
    z_stream s;
    memset(&s, 0, sizeof(s));

    int rc = deflateInit2(&s, Z_BEST_COMPRESSION, Z_DEFLATED,
                          -MAX_WBITS, 8, Z_DEFAULT_STRATEGY);
    if (rc != Z_OK) return rc;

    rc = deflateSetDictionary(&s, dict, DICT_SIZE);
    if (rc != Z_OK) {
        deflateEnd(&s);
        return rc;
    }

    s.next_in = (Bytef *)plain;
    s.avail_in = PLAIN_SIZE;
    s.next_out = comp;
    s.avail_out = COMP_SIZE;

    rc = deflate(&s, Z_FINISH);
    if (rc != Z_STREAM_END) {
        deflateEnd(&s);
        return rc;
    }

    *comp_len = s.total_out;
    deflateEnd(&s);
    return Z_OK;
}

typedef struct {
    int q;
    int r;
    int g_init;
    int g_input;
    int g_output;
    unsigned int h_len;
    int rc;
    unsigned long out_len;
    int y;
} arm_result;

static arm_result decode_arm(
    const unsigned char *dict,
    int install_dictionary,
    const unsigned char *comp,
    uLong comp_len,
    const unsigned char *expected
) {
    arm_result out;
    memset(&out, 0, sizeof(out));

    z_stream s;
    memset(&s, 0, sizeof(s));
    unsigned char decoded[OUT_SIZE];
    unsigned char measured_dict[DICT_SIZE];
    memset(decoded, 0, sizeof(decoded));
    memset(measured_dict, 0, sizeof(measured_dict));

    int rc = inflateInit2(&s, -MAX_WBITS);
    out.q = (rc == Z_OK);
    out.r = 1; /* frozen raw-DEFLATE route in both arms */
    out.g_init = out.q;
    out.g_input = (comp != NULL && comp_len > 0);
    out.g_output = (OUT_SIZE >= PLAIN_SIZE);

    if (rc != Z_OK) {
        out.rc = rc;
        return out;
    }

    if (install_dictionary) {
        rc = inflateSetDictionary(&s, dict, DICT_SIZE);
        if (rc != Z_OK) {
            out.rc = rc;
            inflateEnd(&s);
            return out;
        }
    }

    uInt dict_len = DICT_SIZE;
    rc = inflateGetDictionary(&s, measured_dict, &dict_len);
    if (rc != Z_OK) {
        out.rc = rc;
        inflateEnd(&s);
        return out;
    }
    out.h_len = dict_len;

    s.next_in = (Bytef *)comp;
    s.avail_in = (uInt)comp_len;
    s.next_out = decoded;
    s.avail_out = OUT_SIZE;

    do {
        rc = inflate(&s, Z_NO_FLUSH);
    } while (rc == Z_OK && s.avail_in > 0 && s.avail_out > 0);

    out.rc = rc;
    out.out_len = s.total_out;
    out.y = (rc == Z_STREAM_END &&
             s.total_out == PLAIN_SIZE &&
             memcmp(decoded, expected, PLAIN_SIZE) == 0);

    inflateEnd(&s);
    return out;
}

static void print_arm(const char *name, arm_result a) {
    printf("%s_Q=%d\n", name, a.q);
    printf("%s_R=%d\n", name, a.r);
    printf("%s_G_INIT=%d\n", name, a.g_init);
    printf("%s_G_INPUT=%d\n", name, a.g_input);
    printf("%s_G_OUTPUT=%d\n", name, a.g_output);
    printf("%s_H_DICT_LEN=%u\n", name, a.h_len);
    printf("%s_RC=%d\n", name, a.rc);
    printf("%s_OUT_LEN=%lu\n", name, a.out_len);
    printf("%s_Y=%d\n", name, a.y);
}

int main(void) {
    unsigned char dict[DICT_SIZE];
    unsigned char plain[PLAIN_SIZE];
    unsigned char comp[COMP_SIZE];
    uLong comp_len = 0;

    fill_dictionary(dict);
    memcpy(plain, dict + (DICT_SIZE - PLAIN_SIZE), PLAIN_SIZE);

    int crc = compress_with_dictionary(dict, plain, comp, &comp_len);
    if (crc != Z_OK) {
        fprintf(stderr, "compression failed rc=%d\n", crc);
        return 2;
    }

    printf("ZLIB_VERSION_RUNTIME=%s\n", zlibVersion());
    printf("COMPRESSED_LEN=%lu\n", comp_len);
    printf("PLAIN_LEN=%d\n", PLAIN_SIZE);

    arm_result with_dict = decode_arm(dict, 1, comp, comp_len, plain);
    arm_result no_dict = decode_arm(dict, 0, comp, comp_len, plain);

    print_arm("WITH_DICT", with_dict);
    print_arm("NO_DICT", no_dict);

    int same_z =
        with_dict.q == no_dict.q &&
        with_dict.r == no_dict.r &&
        with_dict.g_init == no_dict.g_init &&
        with_dict.g_input == no_dict.g_input &&
        with_dict.g_output == no_dict.g_output;

    printf("SAME_Z=%d\n", same_z);
    printf("H_DIFF=%d\n", with_dict.h_len != no_dict.h_len);
    printf("Y_DIFF=%d\n", with_dict.y != no_dict.y);

    return 0;
}
