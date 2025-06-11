#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were provided as a space-separated list in the standard input.

#Overall this is what the function does:Reads a space-separated list of integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains one input: an integer
    return int(input())
    #The program returns an integer that was provided as input from stdin

#Overall this is what the function does:The function reads an integer from standard input and returns it as an integer value, effectively passing the input integer through without modification.

#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a number from the space-separated list of integers provided in the standard input.

#Overall this is what the function does:Reads a space-separated list of integers from standard input and returns a map object containing the sequence of integers.

#State of the program right berfore the function call: stdin contains a string.
    return input().strip()
    #The program returns a string that is the input from stdin with leading and trailing whitespace removed.

#Overall this is what the function does:The function reads a string from standard input, removes leading and trailing whitespace, and returns the resulting string.

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
        
    #State: Output State: The value of ans is either -1 or the maximum number of pairs of elements in a that have the same i-th bit set to 1 for some i, the value of x is unchanged, the value of n is unchanged, the list a is either unchanged or contains only the elements that had the i-th bit set to 1 for some i, and the list t is empty.
    return max(ans, len(a))
    #The program returns the maximum number of pairs of elements in a that have the same i-th bit set to 1 for some i, or -1 if no such pairs exist, while the value of x remains unchanged, the value of n remains unchanged, the list a is either unchanged or contains only the elements that had the i-th bit set to 1 for some i, and the list t is empty.

#Overall this is what the function does:This function determines the maximum number of pairs of elements in a list that have the same bit set to 1 at a specific position, or returns -1 if no such pairs exist. It takes no direct parameters but uses the values of n, x, and list a, which are assumed to be set before the function call. The function returns the maximum number of pairs or -1, while leaving the value of x unchanged and the value of n unchanged. The list a is either left unchanged or modified to contain only the elements that had the i-th bit set to 1 for some i, and the list t is always left empty.

