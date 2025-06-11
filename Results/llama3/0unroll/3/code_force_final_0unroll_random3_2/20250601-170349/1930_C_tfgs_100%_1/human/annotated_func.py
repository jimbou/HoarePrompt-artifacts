#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 ≤ n ≤ 3 * 10^5). The second line contains n integers a_1,a_2,...,a_{n} (1 ≤ a_i ≤ 10^9). The sum of n over all test cases does not exceed 3 * 10^5.
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: Output State: The list 'a' has been modified such that each element at index 'i' has been incremented by 'i + 1'. The value of 'n' remains unchanged.
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
        
    #State: Output State: The list 'a' remains unchanged, 'counter' contains the count of each element in 'a' after it was modified, 'cur' is the total count of all elements in 'a', 'cnt' is 0, and 'ans' contains all elements from the original list 'a' in descending order, with each element repeated the same number of times as it appeared in the original list, and the missing elements in between each pair of adjacent elements in 'a' are filled in descending order.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: Output State: The list 'a' remains unchanged, 'counter' contains the count of each element in 'a' after it was modified, 'cur' is the total count of all elements in 'a', 'cnt' is 0, and 'ans' contains all elements from the original list 'a' in descending order, with each element repeated the same number of times as it appeared in the original list, and the missing elements in between each pair of adjacent elements in 'a' are filled in descending order, and 'cnt' number of elements are appended to 'ans' with each element being one less than the last element in 'ans'.
    print(*ans)
    #This is printed: all elements from the original list 'a' in descending order, with each element repeated the same number of times as it appeared in the original list, and the missing elements in between each pair of adjacent elements in 'a' are filled in descending order, and 'cnt' number of elements are appended to 'ans' with each element being one less than the last element in 'ans'

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the result. It accepts multiple test cases, each containing an integer n and a list of n integers. The function modifies the list by incrementing each element by its index plus one, removes duplicates, sorts the list in descending order, and fills in missing elements between each pair of adjacent elements. It then appends additional elements to the end of the list, each being one less than the last element. The function prints the resulting list.

