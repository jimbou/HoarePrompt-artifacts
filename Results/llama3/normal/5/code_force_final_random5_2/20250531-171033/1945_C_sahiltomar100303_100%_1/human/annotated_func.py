#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (3 <= n <= 3*10^5) and then a string a of length n, consisting only of 0 and 1.
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
        
    #State: The program prints the value of either `left` or `right` based on the conditions. If `left` is 0, the program prints the value of `right` if `right` is not equal to `n`, or prints the value of `left` if `right` is equal to `n` and `rightOne` is less than (n + 1) // 2, or prints the value of `right` if `right` is equal to `n` and `rightOne` is greater than or equal to (n + 1) // 2. If `left` is not 0, the program prints the value of `left` if `right` is equal to `n` and `leftZero` is less than (n + 1) // 2, or prints the value of `right` if `right` is equal to `n` and `leftZero` is greater than or equal to (n + 1) // 2, or prints the value that is closer to the middle index of string `s` if `right` is not equal to `n`.

#Overall this is what the function does:This function takes multiple test cases as input, where each test case consists of an integer n and a string s of length n containing only 0s and 1s. It then calculates the indices 'left' and 'right' based on the number of 0s and 1s in the string, and prints the value of either 'left' or 'right' based on certain conditions. If 'left' is 0, it prints 'right' if 'right' is not equal to n, or prints 'left' if 'right' is equal to n and the number of 1s on the right is less than half of n, or prints 'right' if 'right' is equal to n and the number of 1s on the right is greater than or equal to half of n. If 'left' is not 0, it prints 'left' if 'right' is equal to n and the number of 0s on the left is less than half of n, or prints 'right' if 'right' is equal to n and the number of 0s on the left is greater than or equal to half of n, or prints the value that is closer to the middle index of the string if 'right' is not equal to n.

