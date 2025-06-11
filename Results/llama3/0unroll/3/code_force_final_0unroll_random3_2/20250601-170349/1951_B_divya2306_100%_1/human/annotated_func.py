#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two space-separated integers: n and k (2 <= n <= 10^5, 1 <= k <= n). The second line contains n space-separated integers: a_1, a_2, ..., a_n (1 <= a_i <= 10^9) that are pairwise different.
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: wins is the number of elements in the list a that are less than or equal to the element at index k-1, and i is equal to the index of the first element in a that is greater than the element at index k-1, or n if no such element exists.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: at least k-1
        return
        #The program returns nothing because there is no return value specified in the code snippet.
    #State: *wins is the number of elements in the list a that are less than or equal to the element at index k-1, and i is equal to the index of the first element in a that is greater than the element at index k-1, or n if no such element exists. wins is less than k
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: Output State: `win_with_swap` is equal to the maximum value of `wins + 1` and `k`, and `i` is equal to the index of the first element in `a` that is greater than the element at index `k-1`, or `k` if no such element exists.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: max(wins - 1, win_with_swap - wins - 1 + (wins != 0)) (where wins is the number of wins, win_with_swap is the maximum value of wins + 1 and k, and k is an integer)

#Overall this is what the function does:This function determines the maximum number of wins that can be achieved in a game where a player can win by having a score less than or equal to the score of the k-th player. The function takes as input a list of scores and an integer k, and prints the maximum number of wins that can be achieved either by the player's current score or by swapping the player's score with the score of the k-th player. If the player's current score is already less than or equal to the score of the k-th player, the function prints the number of wins minus one. Otherwise, it prints the maximum number of wins that can be achieved by swapping the scores.

