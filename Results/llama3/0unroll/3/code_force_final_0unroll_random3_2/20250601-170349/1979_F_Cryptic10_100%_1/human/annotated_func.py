#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n (2 <= n <= 10^5).
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
        
    #State: Output State: The output state after the loop executes all the iterations is that the function q has been called multiple times with different inputs, and the standard output contains multiple lines, each starting with '! ' followed by a sequence of space-separated integers. The number of lines in the output is equal to the number of test cases in the input. The sequence of integers in each line represents the final order of the elements in the set vx after the loop has finished executing. The order of the elements is determined by the operations performed in the loop, which involve removing elements from the set vx and appending them to the lists p1 and p2 in a specific order. The final order of the elements is the reverse of the order in which they were appended to p1 and p2.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains an integer n (2 <= n <= 10^5). For each test case, it generates a sequence of integers representing the final order of elements in the set vx after performing a series of operations. The operations involve removing elements from the set vx and appending them to lists p1 and p2 in a specific order. The final order of the elements is the reverse of the order in which they were appended to p1 and p2. The function then prints the final order of elements for each test case to standard output, with each sequence starting with '! ' followed by a sequence of space-separated integers.

