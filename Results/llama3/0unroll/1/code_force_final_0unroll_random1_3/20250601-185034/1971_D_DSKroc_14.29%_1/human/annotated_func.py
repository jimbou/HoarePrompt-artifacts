#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings, each consisting of characters '0' and '1' with a length between 1 and 500 (inclusive).
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i + 1]):
                count += 1
        
        print(count + 1)
        
    #State: The output state will contain `t` integers, each representing the number of segments in the corresponding input string where the digit at the current position is greater than the digit at the next position, plus one. The value of `t` remains unchanged.

#Overall this is what the function does:The function reads an integer t from standard input, followed by t strings consisting of '0' and '1' characters. It then calculates the number of segments in each string where the current digit is greater than the next digit, adds 1 to this count, and prints the result for each string. The function does not modify the input strings or the value of t.

