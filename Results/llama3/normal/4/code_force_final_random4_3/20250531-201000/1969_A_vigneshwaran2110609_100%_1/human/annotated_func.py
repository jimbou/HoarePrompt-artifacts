#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == i + 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: n is an integer between 2 and 50 (inclusive), i is equal to n, x is an integer greater than or equal to 0, l is a list of integers equal to the second input. If the element at index l[i] - 1 in list l is equal to i + 1 at any point during the loop, then flag is True and the number 2 is printed. Otherwise, the number 3 is printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints output based on the conditions met in each test case. It accepts no parameters and returns no value. The function iterates over the test cases, reads the number of integers and the integers themselves, and checks if any integer at a specific index matches the index plus one. If a match is found, it prints 2; otherwise, it prints 3. The function's purpose is to evaluate the given test cases and provide output based on the specified conditions.

