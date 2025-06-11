#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n (2 <= n <= 10^5), followed by (n - 2) lines, each containing two integers u and v (1 <= u, v <= n, u != v) representing the ends of the edge that was removed from the graph.
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
        
    #State: vx is an empty set, ops is an empty list, p1 is a list containing all integers from 1 to the first integer in the test case, p2 is an empty list, _ is equal to the number of test cases, stdin is empty, and this is printed: "! " followed by the concatenation of the reversed lists p1 and p2, with elements separated by spaces, which is equivalent to "! " followed by the concatenation of the reversed list p1, with elements separated by spaces.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains an integer n followed by (n - 2) lines of edge information. It then performs a series of queries and operations to reconstruct the original graph, and finally prints the reconstructed graph in a specific format. The function accepts no parameters and returns no value, but instead prints the reconstructed graph to standard output. The final state of the program is that all input has been consumed, and the reconstructed graph has been printed to standard output.

