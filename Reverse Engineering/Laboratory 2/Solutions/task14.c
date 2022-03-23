#include <stdint.h>

uint64_t fibonacci(uint64_t n)
{
    if (n > 1) {
        return myst4(n-1) + myst4(n-2);
    }
    else {
        return n;
    }
}

