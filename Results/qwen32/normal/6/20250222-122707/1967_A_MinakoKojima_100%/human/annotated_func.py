#State of the program right berfore the function call: Each test case consists of two integers n (1 ≤ n ≤ 2 · 10^5) and k (0 ≤ k ≤ 10^12), representing the number of distinct types of cards and the number of coins, respectively. The second line of each test case contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^12), where a_i represents the number of cards of type i initially available. The number of test cases t (1 ≤ t ≤ 100) is provided at the beginning, and the sum of n over all test cases does not exceed 5 · 10^5.
def func():
    ans_list = []
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        ans = a[0]
        
        res = n - 1
        
        for i in range(n - 1):
            dif = a[i + 1] - a[i]
            if dif == 0:
                res -= 1
            if dif != 0:
                if k >= dif * (i + 1):
                    ans += dif
                    k -= dif * (i + 1)
                    res -= 1
                else:
                    ans += k // (i + 1)
                    if i != 0:
                        res += k % (i + 1)
                    k = 0
                    break
                if k == 0:
                    break
        
        if k != 0:
            ans += k // n
            res += k % n
        
        ans += (ans - 1) * (n - 1)
        
        ans += res
        
        ans_list.append(ans)
        
    #State: ans_list
    for a in ans_list:
        print(a)
        
    #State: ans_list is a list that has been fully traversed, and all elements have been printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of card types `n` and a number of coins `k`, along with a list of integers representing the initial count of each card type. For each test case, it calculates a value based on the distribution of card counts and the number of coins available, and prints this value.

