#State of the program right berfore the function call: stdin contains a sequence of lines. The first line contains an integer t (1 ≤ t ≤ 10^4). Each of the following t lines contains an integer n (2 ≤ n ≤ 500), followed by n-1 integers x_2, ..., x_n (1 ≤ x_i ≤ 500).
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
        
    #State: The output state is a series of lines, each containing a sequence of integers. The number of lines is equal to the initial value of `t`. Each line contains `n` integers, where `n` is the first integer in the corresponding line of the input. The integers in each line are the result of subtracting the corresponding integers in the input line from 1000, in reverse order.

#Overall this is what the function does:This function reads a sequence of lines from standard input, where the first line contains an integer t, and each of the following t lines contains an integer n followed by n-1 integers. It then processes each line by subtracting the integers from 1000 in reverse order and prints the resulting sequence of integers, one line per input line, with the number of lines equal to the initial value of t.

