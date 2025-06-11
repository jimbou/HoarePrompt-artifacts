#State of the program right berfore the function call: stdin contains multiple test cases. The first line of each test case contains a single integer n (1 ≤ n ≤ 3 * 10^5) — the length of array a. The second line of each test case contains n integers a_1,a_2,…,a_{n} (1 ≤ a_i ≤ 10^9) — the elements of array a.
    n = int(input())
    arr = list(map(int, input().split()))
    st = set()
    for i in range(n):
        st.add(arr[i] + i + 1)
        
    #State: `n` is an integer between 1 and 3 * 10^5, `arr` is a list of `n` integers between 1 and 10^9, `st` is a set containing `n` elements which are `arr[0] + 1`, `arr[1] + 2`, ..., `arr[n-1] + n`, `i` is `n-1`, stdin contains multiple test cases minus one.
    print(*sorted(st, reverse=True))
    #This is printed: arr[n-1] + n, arr[n-2] + (n-1), ..., arr[0] + 1 (where arr[i] is the ith element of the list arr and n is the number of elements in the list arr)

#Overall this is what the function does:This function reads a test case from standard input, where the first line contains the length of an array and the second line contains the array elements. It then creates a set of elements by adding the index plus one to each array element, and finally prints the elements of the set in descending order. The function processes one test case at a time, and it assumes that multiple test cases are provided in the standard input.

