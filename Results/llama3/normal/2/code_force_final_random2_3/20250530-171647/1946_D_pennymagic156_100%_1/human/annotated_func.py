#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were provided as input through stdin, where each integer was separated by a space.

#Overall this is what the function does:Reads a space-separated list of integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains one input: an integer.
    return int(input())
    #The program returns an integer that was provided as input.

#Overall this is what the function does:Reads an integer from standard input and returns it as is, without any modifications or additional processing.

#State of the program right berfore the function call: stdin contains one input: a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a list of integers, where each integer is a value from the space-separated list of integers provided as input through stdin.

#Overall this is what the function does:The function reads a space-separated list of integers from standard input, converts each integer to an integer type, and returns a map object containing the list of integers.

#State of the program right berfore the function call: stdin contains a string
    return input().strip()
    #The program returns a string that is read from the standard input, with leading and trailing whitespace removed.

#Overall this is what the function does:Reads a string from standard input, removes leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: n is a positive integer, x is a non-negative integer less than 2^30, and a is a list of non-negative integers less than 2^30.
    n, x = func_3()
    a = func_1()
    t, ans = [], -1
    for i in range(29, -1, -1):
        u, v = x >> i & 1, sum([(val >> i & 1) for val in a])
        
        if u == v == 0:
            continue
        
        if u == 0:
            if v % 2:
                return ans
            else:
                op = ai = 0
                for val in a:
                    op ^= val >> i & 1
                    ai ^= val
                    if not op:
                        t.append(ai)
                        ai = 0
                a, t = t, []
        elif v % 2:
            continue
        elif v:
            op = cnt = 0
            for val in a:
                op ^= val >> i & 1
                if not op:
                    cnt += 1
            ans = max(ans, cnt)
        else:
            break
        
    #State: n is a positive integer, x is a non-negative integer less than 2^30, a is a list of non-negative integers less than 2^30, t is a list containing the result of ai XOR val if op is 0, otherwise t is an empty list, ans is the maximum number of times op is False, i is -1, u is the 0th bit of x, v is the sum of the 0th bits of all elements in the list a.
    return max(ans, len(a))
    #The program returns the maximum value between the maximum number of times op is False and the number of non-negative integers less than 2^30 in list a.

#Overall this is what the function does:This function takes no explicit parameters but uses the values of n, x, and a from the outer scope. It performs bit manipulation operations on x and the elements of list a, iterating through the bits of x from most significant to least significant. For each bit position, it checks the parity of the corresponding bits in x and the elements of a. If the parities match, it continues to the next bit position. If the parities do not match and the bit in x is 0, it returns the current maximum count of non-matching parities. If the parities do not match and the bit in x is 1, it updates the maximum count of non-matching parities and continues to the next bit position. Finally, it returns the maximum value between the maximum count of non-matching parities and the number of non-negative integers less than 2^30 in list a.

