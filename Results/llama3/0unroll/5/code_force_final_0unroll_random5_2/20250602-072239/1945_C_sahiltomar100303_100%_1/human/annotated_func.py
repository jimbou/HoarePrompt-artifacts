#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (greater than or equal to 3) and then a string consisting only of 0 and 1, with a length equal to the integer.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        mid = n // 2
        
        leftZero = 0
        
        rightZero = 0
        
        leftOne = 0
        
        rightOne = 0
        
        tleftZero = 0
        
        trightZero = 0
        
        tleftOne = 0
        
        trightOne = 0
        
        for i in range(mid):
            if s[i] == '0':
                leftZero += 1
                tleftZero += 1
            else:
                leftOne += 1
                tleftOne += 1
        
        for i in range(mid, n):
            if s[i] == '0':
                rightZero += 1
                trightZero += 1
            else:
                rightOne += 1
                trightOne += 1
        
        left = mid
        
        leftMove = 0
        
        while left > 0 and (leftZero < (left + 1) // 2 or rightOne < (n - left + 1) //
            2):
            if s[left - 1] == '0':
                leftZero -= 1
                rightZero += 1
            else:
                leftOne -= 1
                rightOne += 1
            left -= 1
        
        right = mid
        
        while right < n and (tleftZero < (right + 1) // 2 or trightOne < (n - right +
            1) // 2):
            if s[right] == '0':
                tleftZero += 1
                trightZero -= 1
            else:
                tleftOne += 1
                trightOne -= 1
            right += 1
        
        if left == 0:
            if right != n:
                print(right)
            elif rightOne >= (n + 1) // 2:
                print(left)
            else:
                print(right)
        elif right == n:
            if left != 0:
                print(left)
            elif tleftZero >= (n + 1) // 2:
                print(right)
            else:
                print(left)
        elif abs((n + 1) // 2 - left) <= abs((n + 1) // 2 - right):
            print(left)
        else:
            print(right)
        
    #State: The loop will print the minimum number of positions to move the left and right pointers to make the left half of the string have at least (n+1)//2 zeros and the right half have at least (n+1)//2 ones, or -1 if it's impossible. The value of t will be 0, and the stdin will be empty.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer (n) and a string (s) of length n containing only 0s and 1s. It then calculates the minimum number of positions to move the left and right pointers to make the left half of the string have at least (n+1)//2 zeros and the right half have at least (n+1)//2 ones, or prints -1 if it's impossible. The function prints the result for each test case and continues until all test cases have been processed, leaving the standard input empty.

