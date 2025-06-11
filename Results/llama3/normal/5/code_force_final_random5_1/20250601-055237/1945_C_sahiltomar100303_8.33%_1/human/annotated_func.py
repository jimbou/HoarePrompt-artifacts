#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains an integer t (1 <= t <= 2*10^4), which is the number of test cases. Each test case consists of two lines. The first line of each test case contains an integer n (3 <= n <= 3*10^5), which is the number of houses. The second line of each test case contains a string a of length n, consisting only of 0 and 1, which represents the preferences of the residents.
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
        
    #State: right equals n, tleftZero is less than or equal to half of mid plus the number of '0' characters in the second half of s, tleftOne is less than or equal to half of mid plus the number of '1' characters in the second half of s, trightZero is 0, and trightOne is 0. If left is 0, then if right is not equal to n, the value of right which is equal to the initial value of n is printed. If right equals n, then if the current value of rightOne is greater than or equal to half of n plus 1, divided by 2, then the value of left which is 0 is printed. Otherwise, the value of right which is n is printed. If left is not equal to 0, then if right equals n, the value of either right or left is printed based on the condition tleftZero >= (n + 1) // 2. If tleftZero is greater than or equal to half of n plus 1, the value of right which is n is printed. Otherwise, the value of left is printed. If right is not equal to n, the value of either left or right is printed, whichever is closer to or at the same distance from the middle index ((n + 1) // 2).

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n (the number of houses) and a string s of length n (representing the preferences of the residents). It then calculates the number of '0' and '1' characters in the first and second halves of the string and adjusts the boundaries of the halves based on certain conditions. Finally, it prints the index of the boundary that is closer to or at the same distance from the middle index of the string, or the index of the boundary that meets certain conditions if one of the boundaries is at the start or end of the string.

