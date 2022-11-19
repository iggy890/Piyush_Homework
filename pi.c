#include <stdio.h>
#include <float.h>

void get_pi(int precision) {
    long long k = 1L;
    float s = 0;

    for (long i = 0; i <= precision; i++) {
        if (i % 2 == 0) {
            s += 4 / k;
        } else {
            s -= 4 / k;
        }

        k += 2;
    }

    printf("%f", s);
}

int main() {
    get_pi(10);
}