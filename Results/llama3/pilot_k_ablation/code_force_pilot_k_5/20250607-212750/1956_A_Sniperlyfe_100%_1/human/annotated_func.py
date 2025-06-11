#State of the program right berfore the function call: p is a list of distinct integers such that 1 <= p[0] < p[1] < ... < p[len(p)-1] <= 100.
    max_n = 100
    remaining_players = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        cur_n = n
        
        while cur_n >= min(p):
            count = bisect.bisect_right(p, cur_n)
            cur_n -= count
        
        remaining_players[n] = cur_n
        
    #State: p is a list of distinct integers such that 1 <= p[0] < p[1] < ... < p[len(p)-1] <= 100, max_n is 100, remaining_players is a list of 101 integers where remaining_players[n] is the number of integers in the range [1, n] that are not in p, n is 100, cur_n is the number of integers in the range [1, max_n] that are not in p.
    return remaining_players
    #The program returns a list of 101 integers where each integer at index n represents the number of integers in the range [1, n] that are not in list p, where p is a list of distinct integers such that 1 <= p[0] < p[1] < ... < p[len(p)-1] <= 100.

#Overall this is what the function does:This function takes a list of distinct integers p as input, where each integer is between 1 and 100, and returns a list of 101 integers representing the count of integers in the range [1, n] that are not in p for each n from 1 to 100. The function effectively computes the complement of the input list p with respect to the range [1, 100].

#State of the program right berfore the function call: p is a list of distinct integers, sorted in ascending order, qs is a list of non-negative integers, and the length of p is equal to k.
    t = int(input())
    results = []
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        remaining_players = func_1(p)
        
        res = [remaining_players[n] for n in qs]
        
        results.append(' '.join(map(str, res)))
        
    #State: p is a list of distinct integers, sorted in ascending order, qs is a list of non-negative integers, t is 0, results is a list containing t strings, stdin is empty, k is an integer, q is an integer, remaining_players is a list of integers, res is a list of integers.
    return results
    #The program returns a list of strings containing 0 strings.

#Overall this is what the function does:The function takes a list of distinct integers in ascending order and a list of non-negative integers as input, processes the list of integers using the func_1 function, and returns a list of strings containing the results of querying the processed list at specified indices. The function repeats this process for a specified number of test cases, consuming all input from stdin, and returns a list of strings containing the results of all test cases.

