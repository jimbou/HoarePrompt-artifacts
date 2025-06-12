#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains three integers a, b, c (0 <= a, b, c <= 10^9) representing the number of introverts, extroverts, and universals, respectively.
    for line in [*open(0)][1:]:
        p, q, r = map(int, line.split())
        
        q += r
        
        print((p - q // 3, -1)[r < q % 3])
        
    #State: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). The file object has been exhausted, line is the last line in the file object, p, q, r are the last values of introverts, extroverts plus universals, universals respectively. The loop has printed t lines, each containing either (p - q // 3, -1) if r is greater than or equal to q % 3, or -1 if r is less than q % 3.

#Overall this is what the function does:The function reads input from stdin, processes it line by line, and prints the result of a calculation based on the number of introverts, extroverts, and universals. It takes no parameters and returns no value, instead printing the results directly. The function exhausts the file object, reading all lines from stdin, and prints a total of t lines, where t is the number of test cases specified in the first line of input. Each printed line contains either the difference between the number of introverts and the number of extroverts plus universals divided by 3, or -1, depending on whether the number of universals is greater than or equal to the remainder of the division of the number of extroverts plus universals by 3.

