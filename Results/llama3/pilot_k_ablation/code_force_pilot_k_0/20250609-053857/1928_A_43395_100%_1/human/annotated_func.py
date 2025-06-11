#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 10^4). Each of the following t lines contains two integers a and b (1 ≤ a, b ≤ 10^9).
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif a % 2 == 0 and a / 2 != b or b % 2 == 0 and b / 2 != a:
            print('yes')
        else:
            print('no')
        
    #State: The output will contain t lines, each containing either 'yes' or 'no'. 'yes' will be printed if both a and b are even, or if one is even and the other is half of the even number. 'no' will be printed otherwise.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains the number of test cases (t) and each subsequent line contains two integers (a and b). It then checks each pair of integers to determine if both are even, or if one is even and the other is half of the even number. Based on this check, it prints 'yes' if the condition is met, and 'no' otherwise, resulting in t lines of output.

