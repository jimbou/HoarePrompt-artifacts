#State of the program right berfore the function call: stdin contains one input: an integer (1 <= t <= 1000), then for each test case, stdin contains one input: an integer (2 <= n <= 10^5).
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
        
    #State: Output State: The loop will execute once, and it will print a list of integers from 1 to n (where n is the input integer) in a specific order, followed by a '!' character and the same list in reverse order. The output will be flushed to ensure it is printed immediately. The function q will be called twice, once with the argument n-2 and once with the argument 0, and it will print '? %d' % d and return a list of integers from the input. The sets vx and ops will be empty after the loop finishes. The list p1 will contain the last two elements of the original list, and the list p2 will contain the remaining elements in reverse order.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n. For each test case, it generates a specific permutation of the numbers from 1 to n and prints it to standard output, followed by the same permutation in reverse order. The function also prints intermediate queries to standard output and reads responses from standard input. The function repeats this process for each test case.

