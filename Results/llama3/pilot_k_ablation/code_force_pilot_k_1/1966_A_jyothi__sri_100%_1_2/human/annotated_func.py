#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 100, 2 <= k <= 100). The second line contains n integers c_1, c_2, ..., c_n (1 <= c_i <= 100).
    t = int(input())
    while t > 0:
        n, k = map(int, input().split())
        
        arrC = list(map(int, input().split()))
        
        hashmap = {}
        
        ans = n
        
        for i in arrC:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
            if hashmap[i] >= k:
                ans = k - 1
        
        print(ans)
        
        t -= 1
        
    #State: `t` is 0, `stdin` is empty, `n` and `k` are the values from the last test case, `arrC` is the list of integers from the last test case, `hashmap` is a dictionary where each key is an element from the last test case and its corresponding value is the frequency of that element in the last test case, and `ans` is an integer equal to `k-1` if any element in the last test case has a frequency greater than or equal to `k`, otherwise `ans` is equal to `n`.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the result for each case. It takes no parameters and returns no value. For each test case, it reads two integers n and k, followed by n integers. It then counts the frequency of each integer and prints k-1 if any integer appears at least k times, otherwise it prints n. The function continues this process until all test cases have been processed, at which point stdin is empty and the function terminates.

