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
            
        #State: t is 0, stdin is empty, n is an integer greater than or equal to 4, x is an integer greater than or equal to 2 and less than or equal to min(n, 2 * 10^5), y is an integer, arr is a sorted list of x distinct integers from 1 to n, i is x, ans is the number of pairs of consecutive integers in arr plus x - 2, and the number of pairs of consecutive integers in arr plus x - 2 is printed.
    #State: The program reads an integer t from stdin, followed by t test cases. Each test case consists of three integers n, x, and y, and a list of x distinct integers from 1 to n. If the program is run as the main module, it processes the test cases and prints the number of pairs of consecutive integers in the list plus x - 2. If the program is not run as the main module, it does nothing.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, x, y) and a list of x distinct integers from 1 to n. It processes each test case by sorting the list of integers, counting the number of pairs of consecutive integers, and printing the count plus x - 2. The function continues processing test cases until all input has been read.

