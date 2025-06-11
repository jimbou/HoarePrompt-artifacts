#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by 2n integers a_1, a_2, ..., a_2n (1 <= a_i <= 10^7).
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
        
    #State: num is an integer, out is a list of sums of the smallest n integers from each test case.
    for outputs in out:
        print(outputs)
        
    #State: Output State: The variable "outputs" has taken the value of the last element in the list "out", and the variable "out" remains unchanged.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by 2n integers. It then sorts the integers in each test case, selects the smallest n integers, calculates their sum, and stores these sums in a list. Finally, it prints each sum in the list. The function does not modify the input values or store any results beyond printing the sums.

