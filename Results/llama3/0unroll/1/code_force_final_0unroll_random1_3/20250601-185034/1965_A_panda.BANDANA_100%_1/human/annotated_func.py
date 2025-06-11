#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then a list of n integers. n is a positive integer and each integer in the list is a positive integer.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = map(int, input().split())
        
        lis = sorted(set(l))
        
        if 1 not in lis or len(lis) == 1:
            print('Alice')
        else:
            test = True
            for j in range(1, len(lis)):
                if lis[j] - lis[j - 1] > 1:
                    if j % 2 == 1:
                        print('Bob')
                    else:
                        print('Alice')
                    test = False
                    break
            if test == True:
                if len(lis) % 2 == 1:
                    print('Alice')
                else:
                    print('Bob')
        
    #State: The output state after the loop executes all the iterations is a list of strings, where each string is either 'Alice' or 'Bob', depending on the input test cases. The length of the output list is equal to the initial value of `t`. The output list contains the results of the game for each test case, where 'Alice' means Alice wins and 'Bob' means Bob wins. The initial value of `t` is not changed, and the input test cases are consumed by the loop, leaving the stdin empty.

#Overall this is what the function does:Determines the winner of a game for each test case in the input, where the game is played with a list of distinct positive integers, and prints the result as either 'Alice' or 'Bob'. The function consumes the input test cases and produces a list of strings representing the game results, without modifying the initial number of test cases.

