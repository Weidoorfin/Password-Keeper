//crypto.h

#ifndef CRYPTO_H
#define CRYPTO_H

char* xor_crypt(const char* plaintext, const char* key);

void destroy(char* ptr);

#endif