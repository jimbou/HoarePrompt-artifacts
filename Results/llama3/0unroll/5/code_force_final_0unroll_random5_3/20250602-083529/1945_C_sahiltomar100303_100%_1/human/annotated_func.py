#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (greater than or equal to 3) and then a string of the same length consisting only of 0 and 1.
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
        
    #State: The loop has executed all iterations, and the output state is the result of the last iteration. The variables `n`, `s`, `mid`, `leftZero`, `rightZero`, `leftOne`, `rightOne`, `tleftZero`, `trightZero`, `tleftOne`, `trightOne`, `left`, `leftMove`, `right` have been updated according to the loop body. The variable `t` has been decremented by 1. The stdin contains no test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (n) and a string (s) of length n containing only 0s and 1s. It then analyzes the string to find the optimal position to split it into two parts, such that the number of 0s in the left part and the number of 1s in the right part are as close to half of the total length as possible. The function prints the position of the split point for each test case. If there are multiple possible split points, it chooses the one that is closer to the middle of the string. If all possible split points are equally distant from the middle, it prints the position of the leftmost split point.

