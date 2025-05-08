//crypto.h

#ifndef CRYPTO_H
#define CRYPTO_H

char* encrypt(const char* plaintext, const char* key);

char* decrypt(const char* ciphertext, const char* key);

void free_str(char* ptr);

#endif