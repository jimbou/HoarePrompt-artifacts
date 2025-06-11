#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then t blocks of two lines each. The first line of each block contains an integer n (1 <= n <= 2 * 10^5). The second line of each block contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 10^9) such that the sum of a_i is divisible by n.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        arr.sort()
        
        if all(arr[i] <= arr[i + 1] for i in range(n - 1)):
            print('YES')
        else:
            print('NO')
        
    #State: t is an integer between 0 and 10^4 (inclusive), stdin contains 0 blocks of two lines each, n is an integer between 1 and 2 * 10^5 (inclusive), arr is a sorted list of n integers a_1, a_2, ..., a_n (0 <= a_i <= 10^9) such that the sum of a_i is divisible by n, _ is t. If arr is a sorted list where each element is less than or equal to the next element, 'YES' is printed. Otherwise, if there exists at least one pair of adjacent elements in arr that are not in non-decreasing order, 'NO' is printed.

#Overall this is what the function does:This function reads a series of input blocks from standard input, where each block contains an integer n followed by a list of n integers. It sorts each list of integers and checks if the list is in non-decreasing order. If the list is sorted, it prints 'YES'; otherwise, it prints 'NO'. The function processes multiple blocks of input, as specified by the initial integer t, and does not return any value.

