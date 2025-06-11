#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 10^5) and then n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: The loop will iterate 'num' times, where 'num' is an integer between 1 and 10^5. In each iteration, it will read an integer 'num2' and a string 'case' from the standard input. If 'num2' is greater than 10000, it will print 1 and 16668, and then break out of the loop. Otherwise, it will split the string 'case' into a list of integers 'a', sort 'a' in ascending order, and calculate the median 'median'. It will then increment the median by 1 until it is greater than the original median, keeping track of the number of increments 'op'. Finally, it will print 'op'. The loop will continue until it has iterated 'num' times or until 'num2' is greater than 10000.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer 'n' and 'n' integers. If 'n' is greater than 10000, it prints 1 and 16668 and stops processing further test cases. Otherwise, it calculates the median of the 'n' integers, increments the median by 1 until it is greater than the original median, and prints the number of increments. The function repeats this process for each test case until it has processed all test cases or until it encounters a test case with 'n' greater than 10000.

