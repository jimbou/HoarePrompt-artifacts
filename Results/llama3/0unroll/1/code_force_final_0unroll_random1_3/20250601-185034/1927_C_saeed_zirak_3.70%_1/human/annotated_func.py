#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains three integers n, m, and k, where n and m are the lengths of arrays a and b, respectively, and k is an even number. The second line contains n integers a_1, a_2, ..., a_n, and the third line contains m integers b_1, b_2, ..., b_m. All integers are between 1 and 10^6.
    for t in range(int(input())):
        n, m, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        aOnes = 0
        
        bOnes = 0
        
        newk = k // 2
        
        i = 1
        
        while i <= k:
            if i in a and i in b:
                if aOnes < bOnes:
                    aOnes += 1
                else:
                    bOnes += 1
            elif i in a and aOnes <= newk:
                aOnes += 1
            elif i in b and bOnes <= newk:
                bOnes += 1
            else:
                break
            i += 1
        
        if aOnes == newk and bOnes == newk:
            print('yes')
        else:
            print('no')
        
    #State: The loop will execute for the number of test cases specified in the input, and for each test case, it will print 'yes' if it is possible to make the number of ones in arrays a and b equal to k/2 by incrementing the count of ones in either array, and 'no' otherwise.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of three lines: the first line contains three integers (n, m, and k), and the next two lines contain n and m integers, respectively. The function then attempts to balance the count of ones in the two arrays by incrementing the count of ones in either array, up to a maximum of k/2. If it is possible to make the counts equal, it prints 'yes'; otherwise, it prints 'no'. The function repeats this process for each test case specified in the input.

