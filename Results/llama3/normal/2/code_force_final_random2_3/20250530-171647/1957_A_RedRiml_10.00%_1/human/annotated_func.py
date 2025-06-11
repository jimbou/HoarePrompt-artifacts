#State of the program right berfore the function call: stdin contains t+1 lines of input, where t is an integer (1 <= t <= 100). The first line contains t. Each of the following t lines contains an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 100).
    w = int(input())
    for _ in range(w):
        ln = int(input())
        
        palka = list(map(int, input().split()))
        
        pl = []
        
        d = {}
        
        for i in palka:
            if d.get(i) == None:
                d[i] = 1
            else:
                d[i] += 1
            if i not in pl:
                pl.append(i)
        
        shapes = 0
        
        for j in pl:
            if d[j] >= 3:
                shapes += 1
        
        print(shapes)
        
    #State: w is an integer between 0 and 100 inclusive, stdin is empty, ln is an integer between 1 and 100 inclusive, palka is an empty list, pl is a list containing all unique integers from the input, d is a dictionary where each key is an integer from the input and its corresponding value is the frequency of that integer in the input, and shapes is equal to the number of integers in the input that have a frequency of 3 or more.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the number of integers that appear three or more times in each set of input integers. It accepts no parameters and returns no value, but instead prints the result for each set of input integers. The function reads t+1 lines of input, where t is an integer between 1 and 100, and each of the following t lines contains an integer n followed by n integers. It then counts the frequency of each integer in each set and prints the number of integers that have a frequency of 3 or more. After processing all input, the function leaves stdin empty and does not modify any external state.

