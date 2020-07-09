#include <cstdio>
#include <algorithm>

#define MAX_N 10000
#define MAX_Y 30000

using namespace std;

struct node
{
    int x, y1, y2, z;
};

bool cmp(node a, node b)
{
    return a.x < b.x;
}

int n, seg[4 * MAX_Y], cnt[4 * MAX_Y], last, res;
node arr[2 * MAX_N];

void update(int lo, int hi, int val, int node, int x, int y)
{
    if (y < lo || hi < x)
        return;
    if (lo <= x && y <= hi)
        cnt[node] += val;
    else
    {
        int mid = (x + y) >> 1;
        update(lo, hi, val, node * 2, x, mid);
        update(lo, hi, val, node * 2 + 1, mid + 1, y);
    }

    if (cnt[node])
        seg[node] = y - x + 1;
    else
    {
        if (x == y)
            seg[node] = 0;
        else
            seg[node] = seg[node * 2] + seg[node * 2 + 1];
    }
}

int main(void)
{
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        int x1, y1, x2, y2;
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        arr[i] = {x1, y1, y2 - 1, 1};
        arr[i + n] = {x2, y1, y2 - 1, -1};
    }

    sort(arr, arr + 2 * n, cmp);

    for (int i = 0; i <= 4; i++)
        printf("%d %d %d %d\n", arr[i].x, arr[i].y1, arr[i].y2, arr[i].z);

    for (int i = 0; i < 2 * n; i++)
    {
        if (i)
        {
            int dx = arr[i].x - last;
            res += dx * seg[1];
        }
        update(arr[i].y1, arr[i].y2, arr[i].z, 1, 0, MAX_Y);
        last = arr[i].x;
    }

    printf("%d\n", res);

    return 0;
}