//crypto.c

#include <string.h>
#include <stdlib.h>
#include "crypto.h"

char* xor_crypt(const char* plaintext, const char* key) {
    size_t len_key = strlen(key);
    size_t length = strlen(plaintext);
    char* ciphertext = malloc(length * sizeof(char) + 1);

    for (size_t i = 0; i < length; i++) {
        ciphertext[i] = plaintext[i] ^ key[i % len_key];
    }

    ciphertext[length] = '\0';
    return ciphertext;
}

void destroy(char* ptr) {
    free(ptr);
}