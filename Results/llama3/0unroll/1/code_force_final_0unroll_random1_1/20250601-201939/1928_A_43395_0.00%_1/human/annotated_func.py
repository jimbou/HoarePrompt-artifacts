#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4). Each of the following t lines contains two integers a and b (1 <= a, b <= 10^9).
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif (a - b == -a, a) or (b - a == -b, b):
            print('no')
        elif (a - b) % 2 > 0 or (a - b) % 2 < 0:
            print('yes')
        else:
            print('no')
        
    #State: The output will contain 't' number of lines, where 't' is the input integer. Each line will contain either 'yes' or 'no' depending on the values of 'a' and 'b' in each iteration.

#Overall this is what the function does:This function reads input from stdin, where the first line contains an integer 't' representing the number of test cases. For each test case, it reads two integers 'a' and 'b', and then determines whether a specific condition is met based on the parity of 'a' and 'b' and their difference. The function prints 'yes' if the condition is met and 'no' otherwise, repeating this process 't' times. The output will contain 't' lines, each containing either 'yes' or 'no'.

