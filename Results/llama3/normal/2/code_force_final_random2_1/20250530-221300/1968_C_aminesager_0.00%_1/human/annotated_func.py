#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (2 <= n <= 500) and then n-1 integers x_2,...,x_n (1 <= x_i <= 500).
    t = int(input())
    while t:
        t = t - 1
        
        n = int(input())
        
        line = input('')
        
        T = list(map(int, line.split()))
        
        a = [1000]
        
        for i in range(1, n):
            a.append(a[i - 1] - T[i - 1])
        
        a = a[::-1]
        
        result = ' '.join(map(str, a))
        
        print(result)
        
    #State: t is 0, n is an integer between 2 and 500 inclusive, T is a list of n-1 integers between 1 and 500 inclusive, a is a list containing n integers: the first integer is 1000, and the remaining integers are the result of subtracting the corresponding element in T from the previous integer in a, but in reverse order, i is n-1, stdin is empty, result is a string containing the elements of a in reverse order, separated by spaces, and this is printed: "[a[0]] [a[1]] ... [a[n-1]]"

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n and n-1 integers x_2 to x_n. It then calculates a list of n integers, starting with 1000 and subtracting each x_i from the previous integer, and prints the resulting list in reverse order, separated by spaces. The function continues to read and process test cases until the initial input t, which represents the number of test cases, reaches 0.

