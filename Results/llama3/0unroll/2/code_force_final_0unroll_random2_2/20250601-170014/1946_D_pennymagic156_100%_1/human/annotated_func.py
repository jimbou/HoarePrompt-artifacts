#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were provided as input through stdin, where each integer was separated by a space.

#Overall this is what the function does:The function reads a space-separated list of integers from standard input, converts them into a list of integers, and returns this list.

#State of the program right berfore the function call: stdin contains one input: an integer
    return int(input())
    #The program returns an integer that was provided as input through stdin.

#Overall this is what the function does:Reads an integer from standard input and returns it.

#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a list of integers, where each integer is a value from the space-separated list of integers provided in the standard input (stdin).

#Overall this is what the function does:Reads a space-separated list of integers from standard input and returns a map object containing the integers.

#State of the program right berfore the function call: stdin contains a string
    return input().strip()
    #The program returns a string that is read from the standard input, with leading and trailing whitespace removed.

#Overall this is what the function does:Reads a string from standard input and returns it with leading and trailing whitespace removed.

#State of the program right berfore the function call: n is a positive integer, x is a non-negative integer less than 2^30, and a is a list of n non-negative integers less than 2^30.
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
        
    #State: Output State: ans is the maximum number of pairs of elements in a that have the same i-th bit, t is an empty list, a is a list of n non-negative integers less than 2^30, x is a non-negative integer less than 2^30, n is a positive integer.
    return max(ans, len(a))
    #The program returns the maximum value between the maximum number of pairs of elements in list 'a' that have the same i-th bit and the total number of non-negative integers less than 2^30 in list 'a'.

#Overall this is what the function does:Functionality: This function takes no parameters and returns the maximum value between the maximum number of pairs of elements in a list 'a' that have the same i-th bit and the total number of non-negative integers less than 2^30 in list 'a'. It operates on a list of non-negative integers less than 2^30 and a non-negative integer less than 2^30, and modifies the list by potentially splitting it into pairs of elements with the same i-th bit. The function returns an integer value representing the maximum of these two quantities.

