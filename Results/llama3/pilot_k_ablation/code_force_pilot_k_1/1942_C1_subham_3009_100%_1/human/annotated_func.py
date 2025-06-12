#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers: n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), y = 0). The second line contains x distinct integers from 1 to n. The number of test cases is a positive integer.
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
            
        #State: t is 0, stdin is empty, n, x, y, arr, and ans are not defined as they are local variables within the loop and are reinitialized in each iteration, the output of the program is the sum of the number of pairs of consecutive elements with a difference of 2 in each test case plus x - 2 for each test case
    #State: *The program processes multiple test cases from stdin. For each test case, it reads three integers n, x, and y, and x distinct integers from 1 to n. The program then calculates the sum of the number of pairs of consecutive elements with a difference of 2 in each test case plus x - 2 for each test case, and outputs this sum. If the program is not run as the main module, it does not process any test cases.

#Overall this is what the function does:This function processes multiple test cases from standard input. For each test case, it reads three integers (n, x, and y) and a list of x distinct integers from 1 to n. It then calculates the sum of the number of pairs of consecutive elements with a difference of 2 in the sorted list plus x - 2, and outputs this sum. The function repeats this process until all test cases have been processed, at which point the standard input is empty.

