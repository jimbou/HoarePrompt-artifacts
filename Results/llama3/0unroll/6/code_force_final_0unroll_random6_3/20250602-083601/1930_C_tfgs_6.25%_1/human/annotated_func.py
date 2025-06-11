#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains a single integer n (1 <= n <= 3 * 10^5). The second line contains n integers a_1,a_2,...,a_{n} (1 <= a_i <= 10^9). The sum of n over all test cases does not exceed 3 * 10^5.
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: Output State: The list 'a' contains n integers where each element at index i is incremented by i + 1, and n remains unchanged.
    counter = Counter(a)
    a = list(set(a))
    a.sort(reverse=True)
    cnt = n - len(a)
    ans = []
    for i in range(len(a)):
        if i > 0:
            adv = min(a[i - 1] - a[i] - 1, cnt, counter[a[i - 1]])
            for j in range(adv):
                ans.append(a[i - 1] - j - 1)
            cnt -= adv
            counter[a[i - 1]] -= adv
        
        ans.append(a[i])
        
        counter[a[i]] -= 1
        
    #State: Output State: The list 'a' remains unchanged, 'counter' contains the frequency of each integer in the original list 'a' minus the number of times each integer was appended to 'ans', 'cnt' is 0, 'ans' contains all integers from the original list 'a' and the missing integers between each pair of adjacent integers in 'a', and n remains unchanged.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: Output State: The list 'a' remains unchanged, 'counter' contains the frequency of each integer in the original list 'a' minus the number of times each integer was appended to 'ans', 'cnt' is 0, 'ans' contains all integers from the original list 'a' and the missing integers between each pair of adjacent integers in 'a', and n remains unchanged.
    print(*ans)
    #This is printed: all integers from the original list 'a' and the missing integers between each pair of adjacent integers in 'a'

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It increments each integer by its 1-based index, removes duplicates, and sorts the list in descending order. Then, it reconstructs the original list by inserting missing integers between each pair of adjacent integers. Finally, it prints the reconstructed list, which includes all original integers and the missing integers between each pair of adjacent integers.

