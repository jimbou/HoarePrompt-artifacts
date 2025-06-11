#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 3 * 10^5) and then a list of n integers a_1,a_2,...,a_{n} (1 <= a_i <= 10^9). The sum of n over all test cases does not exceed 3 * 10^5.
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: stdin contains multiple test cases minus one test case, n is an integer between 1 and 3 * 10^5 inclusive, a is a list of n integers each between 2 and 10^9 + 3 * 10^5 inclusive.
    counter = Counter(a)
    cur = 0
    a = list(set(a))
    a.sort(reverse=True)
    cnt = n - len(a)
    ans = []
    for i in range(len(a)):
        if i > 0:
            adv = min(a[i - 1] - a[i] - 1, cnt, cur)
            for j in range(adv):
                ans.append(a[i - 1] - j - 1)
            cnt -= adv
            cur -= adv
        
        ans.append(a[i])
        
        counter[a[i]] -= 1
        
        cur += counter[a[i]]
        
    #State: After the loop executes all the iterations, the output state will be: n remains unchanged, counter will have all its values decremented by 1, cur will be 0, a remains unchanged, cnt will be 0, and ans will contain all the integers from the original list a, including duplicates, in descending order, with the duplicates inserted in the correct positions to maintain the sorted order.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: After the loop executes all the iterations, the output state will be: n remains unchanged, counter will have all its values decremented by 1, cur will be 0, a remains unchanged, cnt will be 0, and ans will contain all the integers from the original list a, including duplicates, in descending order, with the duplicates inserted in the correct positions to maintain the sorted order.
    print(*ans)
    #This is printed: All the integers from the original list a, including duplicates, in descending order, with the duplicates inserted in the correct positions to maintain the sorted order.

#Overall this is what the function does:This function reads a test case from standard input, where the test case consists of an integer n and a list of n integers. It then modifies the list by adding the 1-based index to each element, removes duplicates while preserving the original order, and sorts the list in descending order. The function then inserts duplicates back into the list in the correct positions to maintain the sorted order. Finally, it prints the modified list in descending order, with duplicates inserted in the correct positions.

