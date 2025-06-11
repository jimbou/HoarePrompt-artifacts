#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by 2n integers a_1,a_2,\ldots,a_{2n} (1 <= a_i <= 10^7).
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: The output state is the sum of the smallest n numbers in each test case, where n is the number of pairs of integers in the test case. The output is printed for each test case.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the sum of the smallest n numbers in each test case, where n is the number of pairs of integers in the test case. It accepts no parameters and returns no value, instead printing the results directly to the console.

