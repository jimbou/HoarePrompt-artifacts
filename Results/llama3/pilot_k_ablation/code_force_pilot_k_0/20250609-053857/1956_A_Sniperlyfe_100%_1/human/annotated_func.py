#State of the program right berfore the function call: p is a list of unique integers such that 1 <= p[i] <= 100 and p[i] < p[i+1] for all i in range(len(p)-1).
    max_n = 100
    remaining_players = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        cur_n = n
        
        while cur_n >= min(p):
            count = bisect.bisect_right(p, cur_n)
            cur_n -= count
        
        remaining_players[n] = cur_n
        
    #State: Output State: The list remaining_players contains the number of players remaining after each iteration of the loop, where the number of players remaining is calculated by subtracting the count of players that have been eliminated from the current number of players. The list p remains unchanged, and max_n remains 100.
    return remaining_players
    #The program returns a list of integers representing the number of players remaining after each iteration of the loop, calculated by subtracting the count of eliminated players from the current number of players, while the list p and max_n remain unchanged at 100.

#Overall this is what the function does:Calculates the number of players remaining after each iteration of a game, where players are eliminated based on a given list of unique integers, and returns a list of these remaining player counts, while preserving the original list of integers and the maximum number of players (100).

#State of the program right berfore the function call: p is a list of distinct integers such that 1 <= p[0] < p[1] < ... < p[len(p)-1] <= 100, and len(p) is a non-negative integer.
    t = int(input())
    results = []
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        remaining_players = func_1(p)
        
        res = [remaining_players[n] for n in qs]
        
        results.append(' '.join(map(str, res)))
        
    #State: Output State: The list "results" will contain t sublists, each containing the remaining players in the list "p" at the indices specified by the list "qs". The list "p" will be the same as the last list of players input, and the variable "t" will be 0.
    return results
    #The program returns an empty list "results" because "t" is 0, and the list "p" is the same as the last list of players input.

#Overall this is what the function does:This function takes no arguments and returns a list of lists containing the remaining players in a game. It first reads an integer t, representing the number of test cases, and then for each test case, it reads an integer k (not used in the function), an integer q, a list of distinct integers p, and a list of indices qs. It then calls another function func_1 with the list p as an argument, and uses the result to create a list of remaining players at the indices specified by qs. The function returns a list of these results for all test cases. If t is 0, the function returns an empty list.

