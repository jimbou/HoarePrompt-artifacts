#State of the program right berfore the function call: stdin contains one input: an integer (1 <= t <= 1000), followed by t inputs: integers (2 <= n <= 10^5).
    q = lambda d: print('? %d' % d, flush=True) or map(int, input().split())
    for _ in range(int(input())):
        vx, ops = set(i for i in range(1, int(input()) + 1)), []
        
        while len(vx) > 2:
            v1, v2 = q(len(vx) - 2)
            vx.remove(v1)
            if v2 > 0:
                ops += [(v1, v2)]
            else:
                v3, _ = q(0)
                vx.remove(v3)
                ops += [(v3, 0), (v1, 0)]
        
        p1, p2 = list(vx), []
        
        for v1, v2 in ops[::-1]:
            (p2 if p1[-1] == v2 else p1).append(v1)
        
        print('! %s' % ' '.join(map(str, p1[::-1] + p2)), flush=True)
        
    #State: vx is an empty set, ops is an empty list, p1 is a list containing all the integers from 1 to n, p2 is an empty list, stdin is empty, and the output "! " followed by the concatenation of the reversed list p1 and list p2, with all elements converted to strings and separated by spaces, is printed.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer represents the number of test cases (t) and each subsequent integer represents the number of elements (n) in a sequence. For each sequence, the function generates a series of queries to determine the correct order of the elements, and then prints the sorted sequence in the format "! <sorted_sequence>" to standard output. The function repeats this process for each test case, ultimately consuming all input from standard input and producing a series of sorted sequences as output.

