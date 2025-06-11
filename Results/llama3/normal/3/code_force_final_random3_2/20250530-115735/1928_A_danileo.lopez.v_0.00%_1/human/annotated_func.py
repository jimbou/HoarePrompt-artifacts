#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4), the number of test cases. Each of the following lines contains two integers a and b (1 <= a, b <= 10^9), the size of Bob's rectangle.
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: `t` is 0, `_` is equal to the initial value of `t`, stdin is empty, and 'Yes' or 'No' has been printed for each pair of integers that were initially in stdin.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains the number of test cases, and each subsequent line contains two integers representing the size of a rectangle. It then prints 'Yes' if either dimension of the rectangle is even, and 'No' otherwise, repeating this process for each test case. After processing all test cases, the function leaves stdin empty and prints a 'Yes' or 'No' result for each input rectangle.

