#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were provided as input in the stdin, separated by spaces.

#Overall this is what the function does:Reads a space-separated list of integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains one input: an integer.
    return int(input())
    #The program returns an integer that was provided as input from stdin.

#Overall this is what the function does:Reads an integer from standard input and returns it as an integer value.

#State of the program right berfore the function call: stdin contains a space-separated list of integers
    return map(int, input().split())
    #The program returns a map object that contains a list of integers that were space-separated in the standard input.

#Overall this is what the function does:Reads a space-separated list of integers from standard input and returns a map object containing the list of integers.

#State of the program right berfore the function call: stdin contains a string
    return input().strip()
    #The program returns a string that is read from the standard input, with leading and trailing whitespace removed.

#Overall this is what the function does:Reads a string from standard input, removes leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: n and x are non-negative integers such that 0 <= n <= 10^5 and 0 <= x < 2^30. a is a list of non-negative integers such that 0 <= a_i < 2^30 for all i from 1 to n.
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
        
    #State: n is a non-negative integer such that 0 <= n <= 10^5, x is a non-negative integer such that 0 <= x < 2^30, a is a list of non-negative integers such that 0 <= a_i < 2^30 for all i from 1 to n, t is a list if v is true otherwise t is an empty list, ans is the maximum number of elements in a that have the same bit pattern as x, i is -1, u is 0, and v is the sum of the 0th bits of all elements in a.
    return max(ans, len(a))
    #The program returns the maximum value between the maximum number of elements in list 'a' that have the same bit pattern as integer 'x' and the total number of elements in list 'a'.

#Overall this is what the function does:This function determines the maximum number of elements in a list 'a' that have the same bit pattern as a given non-negative integer 'x'. It iterates through the bits of 'x' from most significant to least significant, and for each bit, it checks if the corresponding bits in the elements of 'a' are the same. If they are, it counts the number of elements with the same bit pattern. If not, it splits the list 'a' into two parts based on the bit pattern and continues the process recursively. The function returns the maximum value between the maximum number of elements with the same bit pattern and the total number of elements in the list 'a'.

