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
            
        #State: `t` is 0, `stdin` is empty, `n` is an integer, `x` is an integer, `y` is 0, `arr` is a sorted list of `x` distinct integers from 1 to `n`, `ans` is the number of pairs of consecutive integers in `arr` that have a difference of 2 for the last test case
    #State: The program has processed all test cases from stdin. For each test case, it has read three integers n, x, and y, and a sorted list of x distinct integers from 1 to n. The program has calculated the number of pairs of consecutive integers in the list that have a difference of 2 for the last test case, and stored this value in the variable ans. If there are no test cases (i.e., t is 0), stdin is empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, x, y) followed by a list of x distinct integers from 1 to n. It calculates the number of pairs of consecutive integers in the list that have a difference of 2 and prints this value for each test case. The function processes all test cases and empties the standard input.

