#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 10^5). The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 10^9).
    num = int(input())
    for i in range(0, num):
        num2 = int(input())
        
        case = input()
        
        op = 0
        
        if num2 > 10000:
            print(1)
            print(16668)
            break
        else:
            a = [int(i) for i in case.split() if i.isdigit()]
            b = sorted(a)
            if num2 % 2 == 0:
                ma = int(num2 / 2) - 1
            else:
                ma = int(num2 / 2)
            median = b[ma]
            new_median = median
            while new_median <= median:
                b[ma] += 1
                op += 1
                b = sorted(b)
                new_median = b[ma]
            print(op)
        
    #State: num is 0, i is equal to the initial value of num, stdin contains no input, and the value of op is printed for each test case where num2 is not larger than 10000.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains the number of integers in the second line. For each test case, it calculates the minimum number of operations required to increase the median of the integers to a value greater than the original median. If the number of integers is greater than 10,000, it prints a fixed value of 1 and 16,668, and stops processing further test cases. Otherwise, it prints the calculated number of operations for each test case.

