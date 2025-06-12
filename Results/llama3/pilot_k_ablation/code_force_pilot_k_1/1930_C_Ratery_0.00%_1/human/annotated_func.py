#State of the program right berfore the function call: stdin contains multiple test cases. The first line of each test case contains a single integer n (1 ≤ n ≤ 3 * 10^5) — the length of array a. The second line of each test case contains n integers a_1,a_2,...,a_{n} (1 ≤ a_i ≤ 10^9) — the elements of array a. The sum of n over all test cases does not exceed 3 * 10^5.
    n = int(input())
    arr = list(map(int, input().split()))
    st = set()
    for i in range(n):
        st.add(arr[i] + i + 1)
        
    #State: `n` is an integer between 1 and 3 * 10^5, `i` is `n-1`, `arr` is a list of n integers between 1 and 10^9, `st` is a set containing n integers between 2 and 10^9 + n, stdin contains multiple test cases minus 2 lines of input for each test case.
    print(*sorted(st, reverse=True))
    #This is printed: the elements of st in descending order, separated by spaces, where each element is an integer between 2 and 10^9 + n

#Overall this is what the function does:Reads a sequence of test cases from standard input, where each test case consists of an integer n followed by a list of n integers. For each test case, it calculates a new set of integers by adding each element of the list to its 1-based index, then prints the elements of this set in descending order, separated by spaces.

