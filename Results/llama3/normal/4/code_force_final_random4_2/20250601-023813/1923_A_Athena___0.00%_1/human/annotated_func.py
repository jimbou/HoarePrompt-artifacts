#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n space-separated integers (0 <= a_i <= 1).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        res = 0
        
        while a and a[0] == 0:
            a.pop(0)
        
        while a and a[-1] == 0:
            a.pop()
        
        print(a)
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: t is an integer between 1 and 1000 (inclusive) and equals 0, n is an integer, a is an empty list of integers, res is the total number of zeros in a, _ is t, stdin contains 0 test cases, i is -1, and the total number of zeros in the list a which is res has been printed

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the total number of zeros in each test case after removing leading and trailing zeros. It accepts no parameters and returns no values, instead printing the results directly. The function iterates through each test case, removes leading and trailing zeros from the input list, counts the remaining zeros, and prints the count. After processing all test cases, the function concludes, leaving the input variables in a modified state.

