#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n, m <= 2 * 10^5, k is an even integer such that 2 <= k <= 2 * min(n, m). a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6. b is a list of m integers where each integer b_j satisfies 1 <= b_j <= 10^6. The sum of all n and m across all test cases does not exceed 4 * 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        len_a, len_b = len(a), len(b)
        
        count_a, count_b = 0, 0
        
        d = k // 2
        
        for i in range(max(len_a, len_b)):
            if len_a > i + 1:
                if a[i] <= k:
                    count_a += 1
            if len_b > i + 1:
                if b[i] <= k:
                    count_b += 1
        
        print('YES' if count_a >= d and count_b >= d else 'NO')
        
    #State: A series of 'YES' or 'NO' printed for each test case based on the conditions specified.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two lists of integers and an even integer. For each test case, it determines if at least half of the elements in each list are less than or equal to the given even integer. It prints 'YES' if this condition is met for both lists, otherwise it prints 'NO'.

