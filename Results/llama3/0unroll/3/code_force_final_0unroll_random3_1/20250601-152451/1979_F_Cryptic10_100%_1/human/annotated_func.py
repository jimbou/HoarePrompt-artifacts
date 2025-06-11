#State of the program right berfore the function call: stdin contains one input: an integer (1 <= integer <= 1000) representing the number of test cases. For each test case, stdin contains one input: an integer (2 <= integer <= 10^5) representing the number of vertices in the graph.
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
        
    #State: Output State: The loop has executed all its iterations, and the output state is as follows: The set `vx` is empty, the list `ops` contains all the operations performed during the loop, and the lists `p1` and `p2` contain the final ordering of vertices. The output has been printed to the console in the format '! %s' % ' '.join(map(str, p1[::-1] + p2)), where `p1` and `p2` are the final ordering of vertices. The function `q` has been called multiple times with different inputs, and its output has been used to update the sets and lists. The input from stdin has been consumed, and the loop has terminated.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output to the console. It accepts no parameters and returns no value. The function reads an integer from stdin representing the number of test cases, then for each test case, it reads another integer representing the number of vertices in a graph. It performs a series of operations on the graph, including removing vertices and updating lists, and finally prints the final ordering of vertices to the console in a specific format. The function consumes all input from stdin and terminates after processing all test cases.

