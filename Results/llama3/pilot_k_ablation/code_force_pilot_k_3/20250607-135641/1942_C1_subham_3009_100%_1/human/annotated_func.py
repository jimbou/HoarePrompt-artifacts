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
            
        #State: t is 0, stdin is empty, n is an integer between 4 and 10^9, x is an integer between 2 and min(n, 2 * 10^5) and x is greater than 0, y is 0, arr is a sorted list of x distinct integers from 1 to n, ans is either x - 2 or x - 1 or x, i is x, and ans is printed which is either x - 2 or x - 1 or x.
    #State: *stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two lines. The first line contains three integers n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), y = 0). The second line contains x distinct integers from 1 to n. After the execution of the program, for each test case, the output is either x - 2 or x - 1 or x.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of three integers (n, x, y) followed by x distinct integers. It then sorts the integers and checks for pairs of consecutive integers with a difference of 2. The function prints the count of such pairs plus x-2 for each test case. The function continues this process until all test cases have been processed, at which point the standard input is empty.

