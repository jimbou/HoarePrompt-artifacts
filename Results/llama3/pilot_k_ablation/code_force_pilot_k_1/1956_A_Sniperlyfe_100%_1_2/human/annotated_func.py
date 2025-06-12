#State of the program right berfore the function call: p is a list of unique integers such that 1 <= p[0] < p[1] < ... < p[len(p)-1] <= 100.
    max_n = 100
    remaining_players = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        cur_n = n
        
        while cur_n >= min(p):
            count = bisect.bisect_right(p, cur_n)
            cur_n -= count
        
        remaining_players[n] = cur_n
        
    #State: `p` is a list of unique integers such that 1 <= p[0] < p[1] < ... < p[len(p)-1] <= 100, `max_n` is 100, `remaining_players` is a list of 101 integers where `remaining_players[n]` is `n` minus the number of elements in `p` that are less than or equal to `n` for all `n` in range 1 to `max_n`, `n` is `max_n`.
    return remaining_players
    #The program returns a list of 101 integers where each integer at index `n` represents the number of players remaining for the game with number `n`, calculated by subtracting the number of elements in list `p` that are less than or equal to `n` from `n` itself, for all `n` in the range 1 to 100.

#Overall this is what the function does:Calculates the number of players remaining for each game from 1 to 100, given a list of unique integers representing player positions, and returns a list of 101 integers where each integer at index `n` represents the number of players remaining for the game with number `n`.

#State of the program right berfore the function call: p is a list of distinct integers in ascending order, and func_1 is a function that takes a list of integers and returns a list of integers.
    t = int(input())
    results = []
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        remaining_players = func_1(p)
        
        res = [remaining_players[n] for n in qs]
        
        results.append(' '.join(map(str, res)))
        
    #State: p is a list of distinct integers in ascending order, func_1 is a function that takes a list of integers and returns a list of integers, results is a list of strings, stdin is empty, t is 0, k is an integer, q is an integer, remaining_players is a list of integers, qs is a list of integers, res is a list of integers.
    return results
    #The program returns a list of strings named 'results'.

#Overall this is what the function does:The function takes a series of inputs from the user, including the number of test cases, and for each test case, it takes a list of distinct integers in ascending order and a list of queries. It applies a given function (func_1) to the list of integers, then uses the resulting list to answer the queries. The function returns a list of strings, where each string contains the answers to the queries for a test case, in the order they were asked.

