#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 5000) — the number of test cases. For each test case, the first line contains a single integer n (1 ≤ n ≤ 50) — the number of integers written on the whiteboard is 2n. The second line of each test case contains 2n integers a_1,a_2,…,a_{2n} (1 ≤ a_i ≤ 10^7) — the numbers written on the whiteboard.
    num = input()
    out = []
    for numbers in range(int(num)):
        list2 = []
        
        list1 = []
        
        a = input()
        
        a = int(a)
        
        b = input('')
        
        list1 = b.split()
        
        list1.sort()
        
        for i in range(a):
            list2.append(int(list1[2 * i]))
        
        out.append(sum(list2))
        
        del list1[:]
        
        del list2[:]
        
    #State: stdin is empty, num is an empty string, out is a list of integers where each integer is the sum of the elements at even indices of a sorted list of integers.
    for outputs in out:
        print(outputs)
        
    #State: stdin is empty, num is an empty string, out is an empty list of integers.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a number of integers written on a whiteboard. It sorts these integers, selects the elements at even indices, sums them up, and prints the result for each test case. The function processes all test cases, emptying the standard input, and produces a list of sums, one for each test case, which are then printed to the console.

