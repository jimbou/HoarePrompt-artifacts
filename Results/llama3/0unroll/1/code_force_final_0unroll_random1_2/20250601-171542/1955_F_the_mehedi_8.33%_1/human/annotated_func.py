#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] == a[1] == a[2] and a[0] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: The output state will be the sum of the counts for each iteration of the loop, where the count is calculated as the sum of the integer division of each number in the input by 2, plus 1 if all three numbers are equal and odd.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four integers. For each test case, it calculates a count by adding 1 if the first three numbers are equal and odd, then adding the integer division of each number by 2. The function prints the calculated count for each test case.

