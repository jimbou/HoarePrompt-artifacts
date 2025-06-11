#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 2*10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    t = int(input())
    for tc in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        maxsize = max(a)
        
        a.sort()
        
        mexsize = 1
        
        for sz in a:
            if sz == mexsize:
                mexsize = mexsize + 1
        
        if mexsize > maxsize:
            print('Alice' if mexsize % 2 == 0 else 'Bob')
        else:
            print('Alice' if mexsize % 2 == 1 else 'Bob')
        
    #State: The output state will be a list of strings, where each string is either 'Alice' or 'Bob', depending on the value of mexsize for each test case. The length of the output list will be equal to the value of t. The output list will be in the same order as the input test cases.

#Overall this is what the function does:This function determines the winner of a game based on the size of a set of integers. It takes as input a list of integers and outputs a string indicating whether 'Alice' or 'Bob' wins. The function iterates over multiple test cases, each consisting of a list of integers, and outputs a list of strings, one for each test case, indicating the winner. The winner is determined by the minimum excluded size (mexsize) of the set, which is the smallest positive integer not present in the set. If mexsize is greater than the maximum size of the set, the winner is determined by the parity of mexsize; otherwise, the winner is determined by the parity of mexsize minus one.

