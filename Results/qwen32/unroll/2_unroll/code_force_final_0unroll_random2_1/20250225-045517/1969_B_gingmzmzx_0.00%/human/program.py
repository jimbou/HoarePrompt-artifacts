# LUOGU_RID: 160729345
def main():
    n = int(input())
    for _ in range(n):
        s = list(map(int, input().strip()))
        zeroes = s.count(0)
        cnt = [0, 0]
        ans = 0
        for c in s:
            cnt[c] += 1
            if c == 0:
                ans += 1 if cnt[1] > 0 else 0
            else:
                ans += (zeroes - cnt[0])
        print(ans)