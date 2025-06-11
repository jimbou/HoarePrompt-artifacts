#State of the program right berfore the function call: num is a list of integers, num[0] is the number of test cases, each test case is a list of integers, the first two integers of each test case are the number of integers in the list and the parameter determining when Sasha wins, the rest of the integers in each test case are the list that Sasha gave to Anna.
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: Output State: `num` is a list of integers, `num[0]` is the number of test cases, each test case is a list of integers, the first two integers of each test case are the number of integers in the list and the parameter determining when Sasha wins, the rest of the integers in each test case are the list that Sasha gave to Anna, `counter` is 0.
    return counter
    #The program returns counter which is 0

#Overall this is what the function does:This function takes a list of integers as input, where the first element represents the number of test cases, and each test case is a list of integers. The function iterates through the input list in reverse order, counting the number of trailing zeros. It returns the count of trailing zeros. The input list remains unchanged.

