#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == l[i] - 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: n is greater than or equal to 0, x is greater than or equal to 0, i is equal to x, l is a list of integers, stdin contains no test cases, flag is either True or False. If l[l[i] - 1] equals l[i] - 1 at any point during the loop, then flag is True and the number 2 is printed. Otherwise, the number 3 is printed.

#Overall this is what the function does:This function reads input from stdin, processes test cases, and prints results. It accepts an integer t (1 <= t <= 5000) followed by t test cases, each consisting of an integer n (2 <= n <= 50) and n distinct integers. The function checks if any integer in the list matches its 1-based index and prints 2 if a match is found, otherwise prints 3. The function processes all test cases and leaves the input stream empty.

