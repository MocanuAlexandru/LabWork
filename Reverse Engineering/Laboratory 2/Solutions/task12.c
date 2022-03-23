#include <stdint.h>

uint64_t length_string(char* a)
{
    uint64_t i=0;
    while (a[i] != '\0')
    {
        i++;
    }
    return i;
}

