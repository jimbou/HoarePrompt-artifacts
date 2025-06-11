#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then a list of n integers. n is a positive integer and each integer in the list is a positive integer.
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        s = set()
        
        for i in range(n):
            s.add(arr[i])
        
        s = list(s)
        
        s.sort()
        
        s = [0] + s
        
        ans = 1
        
        n = len(s)
        
        if n == 2:
            print('Alice')
        else:
            for i in range(1, n - 1):
                if s[i] - s[i - 1] > 1:
                    break
                else:
                    ans ^= 1
            if ans:
                print('Alice')
            else:
                print('Bob')
        
    #State: The output state will contain t lines, each containing either 'Alice' or 'Bob'. The output will depend on the input values of n and the list of integers. For each test case, if the length of the set of unique integers is 2, the output will be 'Alice'. Otherwise, the output will be 'Alice' if the XOR of the differences between consecutive unique integers is 1, and 'Bob' otherwise.

#Overall this is what the function does:This function determines the winner of a game based on a list of unique integers. It takes a list of integers as input, removes duplicates, sorts the list, and then checks the differences between consecutive integers. If the length of the list is 2, the function outputs 'Alice'. Otherwise, it calculates the XOR of the differences between consecutive integers and outputs 'Alice' if the result is 1, and 'Bob' otherwise. The function processes multiple test cases and outputs the winner for each case.

