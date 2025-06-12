#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two lines. The first line contains three integers n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), y = 0). The second line contains x distinct integers from 1 to n.
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            arr.sort()
            
            arr.append(n + arr[0])
            
            ans = x - 2
            
            for i in range(1, x + 1):
                if arr[i] - arr[i - 1] == 2:
                    ans += 1
            
            print(ans)
            
        #State: t is 0, stdin is empty, n, x, and y are the values from the last test case, arr is a sorted list of x integers from the last test case, ans is the last calculated answer which is x-2 plus the number of pairs of consecutive elements in arr that have a difference of 2
    #State: *The program has processed all test cases from the input. For each test case, it has calculated the answer as x-2 plus the number of pairs of consecutive elements in the sorted list of x integers that have a difference of 2. The program has also updated the values of n, x, and y to the values from the last test case, and the input is now empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, x, y) followed by a list of x distinct integers. It calculates the answer for each test case as x-2 plus the number of pairs of consecutive elements in the sorted list of x integers that have a difference of 2, and prints the answer. The function processes all test cases and updates the values of n, x, and y to the values from the last test case, leaving the input empty.

