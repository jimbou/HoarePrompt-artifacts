#State of the program right berfore the function call: p is a list of distinct integers such that 1 <= p[0] < p[1] < ... < p[len(p)-1] <= 100
    max_n = 100
    remaining_players = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        cur_n = n
        
        while cur_n >= min(p):
            count = bisect.bisect_right(p, cur_n)
            cur_n -= count
        
        remaining_players[n] = cur_n
        
    #State: `p` is a list of distinct integers such that 1 <= p[0] < p[1] < ... < p[len(p)-1] <= 100, `max_n` is 100, `remaining_players` is a list of 101 integers where `remaining_players[n]` is the number of players remaining after removing players with numbers less than or equal to `n` for all `n` from 1 to 100, `n` is 100, `cur_n` is the number of players remaining after removing players with numbers less than or equal to `max_n`.
    return remaining_players
    #The program returns a list of 101 integers where each integer at index n represents the number of players remaining after removing players with numbers less than or equal to n, for all n from 1 to 100.

#Overall this is what the function does:This function calculates the number of players remaining after removing players with numbers less than or equal to a given number, for all numbers from 1 to 100. It takes a list of distinct integers representing player numbers and returns a list of 101 integers, where each integer at index n represents the number of players remaining after removing players with numbers less than or equal to n. The function assumes that the input list is sorted in ascending order and contains numbers between 1 and 100.

#State of the program right berfore the function call: p is a list of integers, qs is a list of integers, and the values in qs are indices of the list returned by func_1(p).
    t = int(input())
    results = []
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        remaining_players = func_1(p)
        
        res = [remaining_players[n] for n in qs]
        
        results.append(' '.join(map(str, res)))
        
    #State: p is a list of integers, qs is a list of integers, t is 0, results is a list of strings where each string is a space-separated list of integers, stdin is empty, k is an integer, q is an integer, remaining_players is a list of integers.
    return results
    #The program returns a list of strings where each string is a space-separated list of integers.

#Overall this is what the function does:The function accepts a series of inputs: the number of test cases, and for each test case, the number of players, the number of queries, a list of player scores, and a list of query indices. It processes these inputs by applying the func_1 function to the player scores, then uses the query indices to extract specific scores from the result. The function returns a list of strings, where each string contains the extracted scores for a test case, separated by spaces.

