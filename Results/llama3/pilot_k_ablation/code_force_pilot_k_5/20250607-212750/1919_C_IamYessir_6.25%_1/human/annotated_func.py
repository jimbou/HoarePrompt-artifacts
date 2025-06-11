#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2*10^5) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
    for _ in range(int(input())):
        n = int(input())
        
        lit = list(map(int, input().split()))
        
        a, b = [lit[0]], []
        
        cp = 0
        
        for i in range(1, n):
            if a[-1] < lit[i]:
                b.append(lit[i])
            else:
                a.append(lit[i])
        
        s = 0
        
        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                s += 1
        
        for i in range(1, len(b)):
            if b[i] > b[i - 1]:
                s += 1
        
        print(s)
        
    #State: The loop has finished executing all iterations, and the final output state is that `n` is an integer, `lit` is a list of integers, `a` is a list containing the first `n` integers of `lit` if the first element of `lit` is less than the second element of `lit`, otherwise `a` is a list containing the first `n` integers of `lit` where the last element of `a` is less than the next element of `lit` if it exists, `b` is a list containing the remaining elements of `lit` if the first element of `lit` is less than the second element of `lit`, otherwise `b` is a list containing the remaining elements of `lit` where the last element of `a` is not less than the next element of `lit` if it exists and is empty, `cp` is 0, `i` is `len(b) - 1`, `_` is not defined, `s` is the number of times `a[i]` is greater than `a[i - 1]` for `i` in range(1, len(a)) plus the number of times `b[i]` is greater than `b[i - 1]` for `i` in range(1, len(b)), `stdin` is empty, and the number of times `a[i]` is greater than `a[i - 1]` for `i` in range(1, len(a)) plus the number of times `b[i]` is greater than `b[i - 1]` for `i` in range(1, len(b)) which is `s` is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then processes the list of integers by splitting it into two lists, a and b, based on the condition that the last element of a is less than the next element of the list. The function then counts the number of times an element in a is greater than its previous element, and the number of times an element in b is greater than its previous element. Finally, it prints the total count of these occurrences for each test case.

