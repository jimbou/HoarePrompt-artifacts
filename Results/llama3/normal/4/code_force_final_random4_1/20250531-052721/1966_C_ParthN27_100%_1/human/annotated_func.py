#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2*10^5) and then n space-separated integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: The loop has finished executing, and the output state is determined by the final values of the variables in the loop head and body. The variable 'ans' will be either 0 or 1, depending on the number of times the loop iterated and the values of the input array 'arr'. If 'ans' is 1, the output will be 'Alice', otherwise it will be 'Bob'. The variable 'n' will be the length of the sorted list 's', which is the number of unique integers in 'arr' plus 1. The variable 'i' will be the last index of the loop, which is 'n-1'. The variable 's' will be the sorted list of unique integers from 'arr' with a 0 prepended to it. The variable 'arr' will be the original list of integers. The stdin will contain the remaining test cases minus the number of iterations of the loop.

#Overall this is what the function does:Determines the winner of a game based on a list of integers. The function accepts a list of integers as input, removes duplicates, sorts the list, and then checks for consecutive integers. If the list contains only two unique integers, the function outputs 'Alice'. Otherwise, it iterates through the list, checking for gaps between consecutive integers. If a gap is found, the function outputs 'Bob'. If no gaps are found, the function outputs 'Alice' if the number of iterations is odd, and 'Bob' if it's even. The function processes multiple test cases from standard input.

