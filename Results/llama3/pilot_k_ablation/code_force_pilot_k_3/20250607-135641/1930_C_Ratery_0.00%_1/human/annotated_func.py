#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= n <= 3 * 10^5) and then a list of n integers (1 <= a_i <= 10^9).
    n = int(input())
    arr = list(map(int, input().split()))
    st = set()
    for i in range(n):
        st.add(arr[i] + i + 1)
        
    #State: n is an integer between 0 and 3 * 10^5, arr is a list of n integers between 1 and 10^9, st is a set containing n elements which are arr[0] + 1, arr[1] + 2, ..., arr[n-1] + n, i is n-1, stdin contains multiple test cases minus one.
    print(*sorted(st, reverse=True))
    #This is printed: elements of st in descending order (where st is a set containing elements that are the sum of each element in the list arr and its 1-based index)

#Overall this is what the function does:The function reads a test case from standard input, where the first input is an integer n representing the number of elements, followed by a list of n integers. It then creates a set of elements by adding each integer in the list to its 1-based index, and finally prints the elements of the set in descending order.

