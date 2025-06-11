#State of the program right berfore the function call: stdin contains multiple test cases. The first line of input contains a single integer t (1 ≤ t ≤ 100) — the number of test cases. Each test case contains two integers n and m (1 ≤ n, m ≤ 100).
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: *`n` and `m` are integers between 1 and 100, there are `t-1` test cases left, and stdin contains `t-1` test cases. If the difference between `n` and `m` is even and greater than or equal to 0, 'Yes' is printed. Otherwise, if the difference is odd or less than 0, 'No' is printed.

#Overall this is what the function does:This function reads two integers, `n` and `m`, from standard input and determines if their difference is even and non-negative. If the difference is even and non-negative, it prints 'Yes'; otherwise, it prints 'No'. The function processes multiple test cases, where the number of test cases is specified in the first line of input. After processing each test case, the function leaves the remaining test cases in the standard input.

