#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case contains an integer n (1 <= n <= 50) followed by 2n integers a_1,a_2,\ldots,a_{2n} (1 <= a_i <= 10^7).
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
        
    #State: `n` is an integer greater than or equal to 0, `s` is equal to the sum of all elements in `list2` which are integers from `list1` in ascending order, `list2` contains all integers from `list1` in ascending order, `final` is a list containing the sum of all elements in `list2`, `num` is equal to `n`, `stdin` contains t-(n+1) test cases, `a` is a string from the last line of input, `list1` is not empty, `str` is the last string in the original `list1` which is an integer, `i` is equal to the length of `list2`.
    for fin in final:
        print(fin)
        
    #State: `n` is an integer greater than or equal to 0, `s` is equal to the sum of all elements in `list2` which are integers from `list1` in ascending order, `list2` contains all integers from `list1` in ascending order, `final` is a list containing the sum of all elements in `list2`, `num` is equal to `n`, `stdin` contains t-(n+1) test cases, `a` is a string from the last line of input, `list1` is not empty, `str` is the last string in the original `list1` which is an integer, `i` is equal to the length of `list2`, and all elements in the `final` list have been printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the results. It expects the input to start with an integer t (1 <= t <= 5000) representing the number of test cases. Each test case consists of an integer n (1 <= n <= 50) followed by 2n integers. The function sorts these integers in ascending order, sums up every other integer starting from the first one, and stores these sums in a list. After processing all test cases, it prints out the sums stored in the list. The function does not return any value but instead prints the results directly.

