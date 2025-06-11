#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 5000) followed by t test cases. Each test case contains an integer n (1 ≤ n ≤ 50) followed by 2n integers a_1,a_2,...,a_{2n} (1 ≤ a_i ≤ 10^7).
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
        
    #State: stdin is empty, num is a string representing an integer 0, out is a list of integers representing the sum of the smallest n integers in each test case.
    for outputs in out:
        print(outputs)
        
    #State: stdin is empty, num is a string representing an integer 0, out is a list of integers representing the sum of the smallest n integers in each test case.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It reads an integer t, representing the number of test cases, followed by t test cases. Each test case consists of an integer n and 2n integers. The function sorts the 2n integers, selects the smallest n integers, calculates their sum, and stores the sum in a list. After processing all test cases, the function prints the sums of the smallest n integers for each test case. The function does not modify the input variables and does not have any side effects other than printing the output.

