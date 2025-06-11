#State of the program right berfore the function call: stdin contains multiple test cases. The first line of each test case contains a single integer n (1 ≤ n ≤ 3 * 10^5) — the length of array a. The second line of each test case contains n integers a_1,a_2,…,a_{n} (1 ≤ a_i ≤ 10^9) — the elements of array a.
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: `n` is an integer equal to the length of array `a` in the current test case, `a` is a list of integers containing the elements of array `a` in the current test case where each element `a[i]` is incremented by `i + 1`, stdin contains multiple test cases minus one, `i` is `n - 1`.
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
        
    #State: n is an integer equal to the length of array a, a is a sorted list of unique integers containing the elements of array a in the current test case where each element a[i] is incremented by i + 1, counter is a dictionary containing the frequency of each element in the original list a, cur is 0, cnt is 0, ans is a list containing all the values from the original list a in ascending order, and i is 0.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: Output State: `n` is an integer equal to the length of array `a`, `a` is a sorted list of unique integers containing the elements of array `a` in the current test case where each element `a[i]` is incremented by `i + 1`, `counter` is a dictionary containing the frequency of each element in the original list `a`, `cur` is 0, `cnt` is 0, `ans` is a list containing all the values from the original list `a` in ascending order except the last `cnt` elements where each element is decreased by 1 from the previous element, and `i` is 0.
    #
    #In natural language, the output state after the loop executes all the iterations is that the list `ans` will contain all the values from the original list `a` in ascending order, except for the last `cnt` elements, which will be a sequence of decreasing numbers, each decreased by 1 from the previous element. The other variables remain unchanged.
    print(*ans)
    #This is printed: The list of numbers from the original list `a` in ascending order, except for the last `cnt` elements, which are a sequence of decreasing numbers, each decreased by 1 from the previous element.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n representing the length of an array a, followed by n integers representing the elements of array a. It then increments each element in the array by its 1-based index, removes duplicates, sorts the array in descending order, and constructs a new list ans by iterating through the sorted array and appending elements in ascending order, except for the last cnt elements, which are a sequence of decreasing numbers, each decreased by 1 from the previous element. Finally, it prints the constructed list ans.

