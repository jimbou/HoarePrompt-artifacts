#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 3 * 10^5). The second line contains n integers a_1,a_2,...,a_{n} (1 <= a_i <= 10^9). The sum of n over all test cases does not exceed 3 * 10^5.
    n = int(input())
    arr = list(map(int, input().split()))
    st = set()
    for i in range(n):
        st.add(arr[i] + i + 1)
        
    #State: `n` is an integer between 1 and 3 * 10^5, `arr` is a list of n integers between 1 and 10^9, `st` is a set containing n elements which are `arr[i] + i + 1` for all i from 0 to n-1, stdin contains multiple test cases minus 2 lines for each test case.
    print(*sorted(st, reverse=True))
    #This is printed: the elements of the set st in descending order (where st contains elements of the form arr[i] + i + 1 for all i from 0 to n-1)

#Overall this is what the function does:Reads a test case from standard input, where the first line contains the number of elements (n) and the second line contains n integers. It then creates a set of elements by adding each integer with its 1-based index plus one, and prints the elements of the set in descending order.

