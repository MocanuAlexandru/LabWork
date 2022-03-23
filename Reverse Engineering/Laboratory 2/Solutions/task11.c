#include <stdint.h>

uint64_t sum_first_n_squares(uint64_t n) {
    uint64_t sum = 0;
    uint64_t i;
    for(i = 0 ; i < n ; i ++)
        sum += i * i;
    return sum;
}
