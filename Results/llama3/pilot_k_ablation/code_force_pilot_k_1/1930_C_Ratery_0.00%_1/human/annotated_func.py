#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 3 * 10^5) and then n space-separated integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The sum of n over all test cases does not exceed 3 * 10^5.
    n = int(input())
    arr = list(map(int, input().split()))
    st = set()
    for i in range(n):
        st.add(arr[i] + i + 1)
        
    #State: `n` is an integer between 1 and 3 * 10^5 inclusive, `arr` is a list of n integers between 1 and 10^9 inclusive, `st` is a set containing n elements where each element is `arr[i] + i + 1` for `i` ranging from 0 to `n-1`, stdin contains multiple test cases minus one.
    print(*sorted(st, reverse=True))
    #This is printed: elements of the form arr[i] + i + 1 for i ranging from 0 to n-1, in descending order (where arr[i] is an integer between 1 and 10^9 inclusive, and n is an integer between 1 and 3 * 10^5 inclusive)

#Overall this is what the function does:Reads a test case from standard input, where a test case consists of an integer n followed by n space-separated integers, and prints the elements of the form arr[i] + i + 1 for i ranging from 0 to n-1 in descending order.

