#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three lines: the first line contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4), and the third line contains a string s of length n consisting of characters 'L' and 'R'.
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        arr = list(map(int, input().split()))
        
        s = input()
        
        l = 0
        
        r = n - 1
        
        for k in s:
            if k == 'L':
                l += 1
            else:
                r -= 1
        
        p = 1
        
        ans = []
        
        for strr in s[::-1]:
            if strr == 'R':
                r += 1
                p = p * arr[r] % m
            else:
                l -= 1
                p = p * arr[l] % m
            ans.append(p)
        
        print(*ans[::-1])
        
    #State: n is an integer, m is an integer, arr is a list of integers, s is a string, l is equal to 0, r is equal to n - 1 minus the number of 'R' characters in the string s, p is the product of the original value of p and the value of arr at index l or r modulo m, ans is a list containing the product of the original value of p and the value of arr at index l or r modulo m, stdin is empty, and the elements of the list ans are printed in reverse order.

#Overall this is what the function does:The function reads input from stdin, processes it, and prints the result. It accepts no parameters and returns no value. The input is expected to contain an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three lines: the first line contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4), and the third line contains a string s of length n consisting of characters 'L' and 'R'. The function processes each test case by iterating over the string s in reverse order, updating the product p by multiplying it with the value of arr at index l or r modulo m, and appending the updated product to the list ans. Finally, it prints the elements of the list ans in reverse order.

