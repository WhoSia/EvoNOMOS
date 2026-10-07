#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include "blake3.h"
#include "blake3_impl.h"

int main(void) {
  const char *msg = "EvoNOMOS-P28-BLAKE3-X1";
  uint8_t out[BLAKE3_OUT_LEN];
  blake3_hasher h;
  blake3_hasher_init(&h);
  blake3_hasher_update(&h, msg, strlen(msg));
  blake3_hasher_finalize(&h, out, sizeof(out));
  printf("SIMD_DEGREE=%zu\n", blake3_simd_degree());
  printf("DIGEST=");
  for (size_t i = 0; i < sizeof(out); ++i) printf("%02x", out[i]);
  printf("\n");
  return 0;
}
