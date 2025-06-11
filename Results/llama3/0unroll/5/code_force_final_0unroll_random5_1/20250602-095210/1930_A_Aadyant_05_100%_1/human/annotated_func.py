#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by 2n integers a_1,a_2,...,a_{2n} (1 <= a_i <= 10^7).
    n = input()
    final = []
    for num in range(int(n)):
        s = 0
        
        list2 = []
        
        a = input()
        
        list1 = []
        
        b = input()
        
        list1 = b.split()
        
        for str in list1:
            list2.append(int(str))
        
        list2.sort()
        
        for i in range(0, len(list2), 2):
            s = s + int(list2[i])
        
        final.append(s)
        
    #State: Output State: The final list contains the sum of the smallest numbers in each pair of the 2n input integers for each test case.
    for fin in final:
        print(fin)
        
    #State: Output State: The final list contains the sum of the smallest numbers in each pair of the 2n input integers for each test case.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts a series of test cases, where each test case consists of an integer n followed by 2n integers. The function sorts these 2n integers, pairs them up, and calculates the sum of the smallest number in each pair. It then prints the sum for each test case. The function does not return any value but instead prints the results directly.

