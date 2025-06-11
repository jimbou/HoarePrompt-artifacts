#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (3 <= n <= 3*10^5) and then a string a of length n, consisting only of 0 and 1.
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
        
    #State: `t` is 0, `n` is an integer and large enough to satisfy the conditions, `s` is a string, `mid` is an integer and greater than 0, `i` is equal to `n`, `leftMove` is 0, `rightZero` is incremented by `(n-mid)` times plus the number of '0's in the substring `s[mid-1:mid-1+left]`, `trightZero` is less than `(n - mid + 1) // 2`, `trightOne` is less than `(n - mid + 1) // 2`, `stdin` is empty. If `right` is equal to `n`, then if `left` is not equal to 0, the current value of `left` is being printed. Otherwise, if the current value of `rightOne` is greater than or equal to `(n + 1) // 2`, the value of `left` which is 0 is being printed. Otherwise, the value of `right` which is equal to `n` is being printed. If `right` is not equal to `n`, then the value of `right` is being printed if `left` is 0. Otherwise, the value of `left` or `right` is printed, depending on whether the absolute difference between the middle index `((n + 1) // 2)` and `left` is less than or equal to the absolute difference between the middle index `((n + 1) // 2)` and `right`.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a string s of length n containing only 0s and 1s. It then finds the index that splits the string into two parts with the most balanced distribution of 0s and 1s. If there are multiple such indices, it prints the one closest to the middle of the string. The function prints the index for each test case.

