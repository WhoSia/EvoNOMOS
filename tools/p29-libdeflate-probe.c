#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "lib_common.h"
#include "libdeflate.h"
#include "x86/cpu_features.h"

int main(void) {
    static const uint8_t input[] = "EvoNOMOS P29 common action oracle";
    const size_t input_size = sizeof(input) - 1;
    struct libdeflate_compressor *compressor = libdeflate_alloc_compressor(6);
    struct libdeflate_decompressor *decompressor = libdeflate_alloc_decompressor();
    uint32_t features = get_x86_cpu_features();
    const uint32_t advanced = X86_CPU_FEATURE_PCLMULQDQ |
        X86_CPU_FEATURE_AVX | X86_CPU_FEATURE_AVX2 | X86_CPU_FEATURE_BMI2 |
        X86_CPU_FEATURE_ZMM | X86_CPU_FEATURE_AVX512BW |
        X86_CPU_FEATURE_AVX512VL | X86_CPU_FEATURE_VPCLMULQDQ |
        X86_CPU_FEATURE_AVX512VNNI | X86_CPU_FEATURE_AVXVNNI;
    uint8_t compressed[256], output[128];
    size_t compressed_size = sizeof(compressed), output_size = 0;
    int q = compressor != NULL && decompressor != NULL;
    size_t produced = q ? libdeflate_zlib_compress(compressor, input, input_size,
                                                    compressed, compressed_size) : 0;
    int g = produced >= 2 && (compressed[0] & 0x0f) == 8 &&
            ((((unsigned)compressed[0] << 8) | compressed[1]) % 31) == 0;
    enum libdeflate_result result = LIBDEFLATE_BAD_DATA;
    if (q && g) {
        result = libdeflate_zlib_decompress(decompressor, compressed, produced,
                                            output, sizeof(output), &output_size);
    }
    int y = result == LIBDEFLATE_SUCCESS && output_size == input_size &&
            memcmp(output, input, input_size) == 0;
    int r = (features & advanced) != 0;
    printf("{\"Q\":%d,\"R\":%d,\"G\":%d,\"Y\":%d,\"features\":%u,\"compressed_size\":%zu}\n",
           q, r, g, y, features, produced);
    libdeflate_free_compressor(compressor);
    libdeflate_free_decompressor(decompressor);
    return (q && g && y) ? 0 : 2;
}
