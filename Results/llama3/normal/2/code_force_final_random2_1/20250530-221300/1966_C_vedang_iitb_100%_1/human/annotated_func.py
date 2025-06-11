#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The first integer is a positive integer and represents the number of piles in the game. The list of integers represents the initial number of stones in each pile and contains the same number of elements as the first integer. Each element in the list is a positive integer.
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
        
    #State: `t` is a positive integer, `tc` is `t-1`, `n` is a positive integer, `a` is a sorted list of positive integers, `maxsize` is the maximum value in `a`, `sz` is the last element in the list `a`, and `mexsize` is the smallest positive integer that is not in the list `a`. Either 'Alice' or 'Bob' is printed depending on whether `mexsize` is even or odd, regardless of whether `mexsize` is greater than `maxsize` or less than or equal to `maxsize`.

#Overall this is what the function does:This function determines the winner of a game based on the number of stones in each pile. It accepts multiple test cases as input, where each test case consists of a positive integer representing the number of piles and a list of positive integers representing the initial number of stones in each pile. The function sorts the list of stones, finds the maximum number of stones, and determines the smallest positive integer that is not in the list (mexsize). It then prints 'Alice' if mexsize is even or 'Bob' if mexsize is odd, regardless of whether mexsize is greater than the maximum number of stones or not.

