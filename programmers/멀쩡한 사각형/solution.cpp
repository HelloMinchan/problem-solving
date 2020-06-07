#include <algorithm>

using namespace std;

long long solution(int w, int h)
{
    return (long)w * h - (w + h - __gcd(w, h));
}