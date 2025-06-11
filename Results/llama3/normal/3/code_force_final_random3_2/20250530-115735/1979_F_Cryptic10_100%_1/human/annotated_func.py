#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains one input: an integer (between 2 and 10^5 inclusive).
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
        
    #State: `q` is a function that takes an integer `d` and returns a list of integers from the input, after printing '? %d' % d and flushing the output, `_` is equal to the number of test cases minus one, `vx` is an empty set, `ops` is an empty list, `p1` is a list of integers from 1 to the input integer (exclusive) with all `v1` appended if `p1[-1] != v2`, otherwise `p1` remains the same, `p2` is a list of integers with all `v1` appended if `p1[-1] == v2`, otherwise `p2` remains an empty list, `v1` is the first element of the first tuple in `ops`, `v2` is the second element of the first tuple in `ops`, and the following is printed: "! [p1 elements in reverse order followed by p2 elements]"

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains an integer between 2 and 10^5 inclusive. It then performs a series of operations on the input integer, including removing elements from a set, appending elements to lists, and printing output in a specific format. The function ultimately prints the final state of the program, which includes the remaining elements in the set and the appended lists, in a specific order.

