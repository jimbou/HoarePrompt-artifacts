#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 2⋅10^5). The second line contains n integers a_1, a_2, … a_n (1 ≤ a_i ≤ 10^9).
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = map(int, input().split())
        
        lis = sorted(set(l))
        
        if 1 not in lis or len(lis) == 1:
            print('Alice')
        else:
            test = True
            for j in range(1, len(lis)):
                if lis[j] - lis[j - 1] > 1:
                    if j % 2 == 1:
                        print('Bob')
                    else:
                        print('Alice')
                    test = False
                    break
            if test == True:
                if len(lis) % 2 == 1:
                    print('Alice')
                else:
                    print('Bob')
        
    #State: The output state after the loop executes all the iterations is a series of 'Alice' or 'Bob' printed to the console, each corresponding to the result of a test case. The number of outputs is equal to the initial value of t. The output for each test case depends on the sequence of integers in the input. If the sequence contains a 1 and has more than one distinct element, the output is determined by the differences between consecutive distinct elements in the sorted sequence. If any difference is greater than 1, the output is 'Bob' if the index of the larger element is odd, and 'Alice' otherwise. If all differences are 1, the output is 'Alice' if the length of the sequence is odd, and 'Bob' otherwise. If the sequence does not contain a 1 or has only one distinct element, the output is 'Alice'.

#Overall this is what the function does:This function determines the winner of a game based on a sequence of integers provided as input. It processes multiple test cases, each containing a sequence of integers. For each test case, it checks if the sequence contains a 1 and has more than one distinct element. If so, it analyzes the differences between consecutive distinct elements in the sorted sequence. If any difference is greater than 1, it declares 'Bob' as the winner if the index of the larger element is odd, and 'Alice' otherwise. If all differences are 1, it declares 'Alice' as the winner if the length of the sequence is odd, and 'Bob' otherwise. If the sequence does not contain a 1 or has only one distinct element, it declares 'Alice' as the winner. The function prints the winner for each test case to the console.

