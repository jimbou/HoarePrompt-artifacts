#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then n space-separated integers. n is a positive integer and each of the n integers is a positive integer.
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
        
    #State: The output state will contain t lines, each containing either 'Alice' or 'Bob'. The output will be 'Alice' if the number of elements in the set s is 2, or if the XOR of the differences between consecutive elements in the sorted list s (excluding the first element) is 1. Otherwise, the output will be 'Bob'.

#Overall this is what the function does:This function determines the winner of a game based on a set of integers. It takes a series of test cases as input, where each test case consists of a positive integer n followed by n space-separated positive integers. The function processes each test case by removing duplicates, sorting the numbers, and then checking the differences between consecutive numbers. If the number of unique elements is 2, or if the XOR of the differences between consecutive numbers (excluding the first element) is 1, the function outputs 'Alice' as the winner. Otherwise, it outputs 'Bob'. The function repeats this process for all test cases and prints the winner for each case.

