#State of the program right berfore the function call: p is a list of distinct integers such that 1 <= min(p) <= max(p) <= 100.
    max_n = 100
    remaining_players = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        cur_n = n
        
        while cur_n >= min(p):
            count = bisect.bisect_right(p, cur_n)
            cur_n -= count
        
        remaining_players[n] = cur_n
        
    #State: p is a list of distinct integers such that min(p) is greater than or equal to 100 and max(p) is less than or equal to 100, max_n is 100, n is 101, cur_n is 0, remaining_players is a list of 101 integers where remaining_players[n] is 0 for all n.
    return remaining_players
    #The program returns a list of 101 integers, where each integer is 0, representing the remaining players.

#Overall this is what the function does:This function takes a list of distinct integers p as input, where each integer is between 1 and 100, and returns a list of 101 integers representing the remaining players after a process. The function initializes a list of 101 integers, remaining_players, and iterates over the range from 1 to 100. For each number n in this range, it calculates the number of players remaining by subtracting the count of players in p that are greater than or equal to n, and stores this value in remaining_players[n]. The function returns the list remaining_players, where each integer represents the number of remaining players for the corresponding number n.

#State of the program right berfore the function call: p is a list of integers representing the sequence a, and it is sorted in ascending order.
    t = int(input())
    results = []
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        remaining_players = func_1(p)
        
        res = [remaining_players[n] for n in qs]
        
        results.append(' '.join(map(str, res)))
        
    #State: p is a list of integers representing the sequence a, and it is sorted in ascending order, t is an integer that must be 0, results is a list containing t strings, qs is a list of integers, k is an integer, q is an integer, remaining_players is a list of integers, res is a list of integers, stdin is empty, _ is t-1
    return results
    #The program returns a list of t strings.

#Overall this is what the function does:The function takes a sequence of integers as input, processes it, and returns a list of strings. The input sequence is sorted in ascending order, and the function performs some operations on it, resulting in a new list of integers called 'remaining_players'. The function then uses this list to generate a list of strings, where each string is a subset of 'remaining_players' based on the input queries 'qs'. The function returns a list of these strings, with each string containing the corresponding subset of 'remaining_players' for each query.

