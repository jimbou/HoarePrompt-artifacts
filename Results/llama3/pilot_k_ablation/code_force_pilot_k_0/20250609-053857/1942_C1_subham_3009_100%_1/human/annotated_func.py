#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers: n, x, and y, where n is a positive integer greater than or equal to 4, x is a positive integer less than or equal to n and 2 * 10^5, and y is 0. The second line contains x distinct integers from 1 to n. The number of test cases is a positive integer less than or equal to 10^4.
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
            
        #State: The program has finished executing all test cases and has printed the maximum number of pairs of adjacent integers that can be formed from the given array for each test case. The value of t is 0, and the values of n, x, y, arr, and ans have been updated for each test case.
    #State: The program has executed all test cases, printing the maximum number of pairs of adjacent integers that can be formed from the given array for each test case, and has updated the values of t, n, x, y, arr, and ans accordingly.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: n, x, and y, where n is a positive integer greater than or equal to 4, x is a positive integer less than or equal to n and 2 * 10^5, and y is 0. The second line contains x distinct integers from 1 to n. For each test case, the function sorts the integers, appends n + the first integer to the end of the array, and then counts the maximum number of pairs of adjacent integers that can be formed from the given array. The function prints the count for each test case. After executing all test cases, the function updates the values of t, n, x, y, arr, and ans accordingly.

