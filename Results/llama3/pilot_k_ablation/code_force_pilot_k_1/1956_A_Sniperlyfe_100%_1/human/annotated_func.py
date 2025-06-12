#State of the program right berfore the function call: p is a list of distinct integers such that 1 <= min(p) <= max(p) <= 100 and p is sorted in ascending order.
    max_n = 100
    remaining_players = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        cur_n = n
        
        while cur_n >= min(p):
            count = bisect.bisect_right(p, cur_n)
            cur_n -= count
        
        remaining_players[n] = cur_n
        
    #State: `p` is a list of distinct integers such that 1 <= min(p) <= max(p) <= 100 and `p` is sorted in ascending order, `max_n` is 100, `remaining_players` is a list of 101 integers where the value at index `n` is the number of players remaining after the players in `p` have been removed from the range `[1, n]` for each `n` from 1 to `max_n`.
    return remaining_players
    #The program returns a list of 101 integers where the value at index `n` is the number of players remaining after the players in `p` have been removed from the range `[1, n]` for each `n` from 1 to 100. The list `p` contains distinct integers between 1 and 100, inclusive, and is sorted in ascending order.

#Overall this is what the function does:This function calculates the number of players remaining in a range from 1 to 100 after removing players specified in the input list `p`. It takes a sorted list of distinct integers between 1 and 100 as input and returns a list of 101 integers, where each value at index `n` represents the number of players remaining after removing players in `p` from the range `[1, n]`. The function effectively updates the state of the program by providing the remaining players count for each range from 1 to 100, considering the removed players in `p`.

#State of the program right berfore the function call: p is a list of distinct integers in ascending order, and the values in p are between 1 and 100 (inclusive).
    t = int(input())
    results = []
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        remaining_players = func_1(p)
        
        res = [remaining_players[n] for n in qs]
        
        results.append(' '.join(map(str, res)))
        
    #State: p is a list of distinct integers in ascending order, and the values in p are between 1 and 100 (inclusive), t is 0, results is a list of strings, each string is a space-separated list of integers, stdin is empty.
    return results
    #The program returns a list of strings, where each string is a space-separated list of integers, and the list is empty since no operations were performed on it.

#Overall this is what the function does:This function takes a list of distinct integers in ascending order (between 1 and 100 inclusive) and a list of queries as input, processes the list using the func_1 function, and returns a list of strings where each string is a space-separated list of integers corresponding to the queries. The function performs this operation for a specified number of test cases (t) and returns the results as a list of strings.

