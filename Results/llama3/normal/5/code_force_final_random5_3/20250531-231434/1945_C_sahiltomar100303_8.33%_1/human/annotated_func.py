#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (n) and then a string (a) of length n, consisting only of 0 and 1. n is an integer such that 3 <= n <= 3*10^5. The sum of n over all test cases does not exceed 3*10^5.
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
            if tleftZero >= (n + 1) // 2:
                print(right)
            else:
                print(left)
        elif abs((n + 1) // 2 - left) <= abs((n + 1) // 2 - right):
            print(left)
        else:
            print(right)
        
    #State: The program prints the value of either `left` or `right`, depending on the values of `right`, `left`, `rightOne`, `tleftZero`, and `n`. If `left` is equal to 0, then if `right` is not equal to `n`, the program prints the value of `right`. If `right` is equal to `n`, the program prints the value of `left` if `rightOne` is greater than or equal to half of `(n + 1)`, otherwise it prints the value of `right`, which is equal to `n`. If `left` is not equal to 0, then if `right` equals `n`, the program prints the value of `right` if `tleftZero` is greater than or equal to half of the value of `n` plus one, otherwise it prints the value of `left`. If `right` does not equal `n`, the program prints the value of `left` if the absolute difference between the middle index `(n + 1) // 2` and `left` is less than or equal to the absolute difference between the middle index `(n + 1) // 2` and `right`, otherwise it prints the value of `right`.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer (n) and a string (a) of length n containing only 0s and 1s. It calculates the number of 0s and 1s in the left and right halves of the string and then adjusts the boundaries of these halves based on certain conditions. The function prints the index of the adjusted boundary that is closer to the middle of the string, or the index of the right boundary if the left boundary is at the start of the string and the right boundary is not at the end, or the index of the left boundary if the right boundary is at the end of the string and the number of 0s in the left half is greater than or equal to half of the string length plus one.

