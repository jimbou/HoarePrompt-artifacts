#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers: n, x, and y, where n is a positive integer greater than or equal to 4, x is a positive integer greater than or equal to 2 and less than or equal to the minimum of n and 2 * 10^5, and y is 0. The second line contains x distinct integers from 1 to n.
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: Output State: `__name__` is `'__main__'`, `t` is `0`, stdin contains no test cases.
        #
        #In this output state, the loop has finished executing all its iterations. The value of `t` has been decremented to `0` after each iteration, and the stdin contains no more test cases. The other variables in the precondition, `__name__`, remain unchanged.
    #State: The program has executed all test cases from stdin. If the program is run as the main module, the program has finished executing all its iterations and stdin contains no more test cases. Otherwise, the program has not executed any test cases.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: n, x, and y, and the second line contains x distinct integers from 1 to n. The function then prints the value of x minus 2 for each test case. The function continues to read and process test cases until there are no more cases in the standard input.

