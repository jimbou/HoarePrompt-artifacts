#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (2 <= n <= 500), then n-1 integers x_2,...,x_n (1 <= x_i <= 500).
    t = int(input())
    while t:
        t = t - 1
        
        n = int(input())
        
        line = input('')
        
        T = list(map(int, line.split()))
        
        a = [1000]
        
        for i in range(1, n):
            a.append(a[i - 1] + T[i - 1])
        
        result = ' '.join(map(str, a))
        
        print(result)
        
    #State: The loop will execute 't' number of times, and for each execution, it will print a list of 'n' integers, where each integer is the sum of the previous integer and the corresponding input integer from the list 'T'. The initial value of the list 'a' is [1000], and for each iteration of the loop, the list 'a' is updated by appending the sum of the last element of 'a' and the corresponding input integer from 'T'.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by n-1 integers. For each test case, it generates a list of n integers, where each integer is the cumulative sum of the previous integer and the corresponding input integer, starting with an initial value of 1000. The function then prints the generated list for each test case.

