#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (2 <= n <= 10^5, 1 <= k <= n). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). It is guaranteed that a_i 's are pairwise different.
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: Output State: `n` is an integer between 2 and 10^5 inclusive, `k` is an integer between 1 and `n` inclusive, `a` is a list of `n` unique integers between 1 and 10^9 inclusive, `wins` is between 0 and `n` inclusive, `stdin` contains multiple test cases minus 1, `i` is `n`.
    #
    #The loop will execute until it has iterated over all elements in the list `a` or until it finds an element that is greater than `a[k - 1]`. At this point, the loop will break, and the value of `wins` will be the number of elements in `a` that are less than or equal to `a[k - 1]`. The value of `i` will be `n` because the loop iterates `n` times.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is between 0 and n inclusive and is greater than or equal to k)
        return
        #The program returns nothing, as there is no explicit return statement. The value of `wins - 1` is printed, which is an integer between -1 and n-1 inclusive, where n is an integer between 2 and 10^5 inclusive, and `wins` is an integer between 0 and n inclusive, and is greater than or equal to k, which is an integer between 1 and n inclusive.
    #State: *`n` is an integer between 2 and 10^5 inclusive, `k` is an integer between 1 and `n` inclusive, `a` is a list of `n` unique integers between 1 and 10^9 inclusive, `wins` is between 0 and `n` inclusive, `stdin` contains multiple test cases minus 1, `i` is `n`. The number of elements in `a` that are less than or equal to `a[k - 1]` is less than `k`.
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: `n` is an integer between 2 and 10^5 inclusive, `k` is an integer between 1 and `n` inclusive, `win_with_swap` is between `k` and `n+1` inclusive, `a` is a list of `n` unique integers between 1 and 10^9 inclusive, `wins` is between 0 and `n` inclusive, `i` is `k`, and stdin contains multiple test cases minus 1. If `a[i]` is greater than `a[k - 1]`, then we break out of the most internal loop or if statement.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: the maximum value between wins - 1 and win_with_swap - wins - 1 + (wins != 0)

#Overall this is what the function does:This function determines the maximum number of wins that can be achieved in a game where a player can either win or lose. The game consists of multiple test cases, each with two lines of input. The first line contains two integers n and k, where n is the number of elements in the game and k is the target number of wins. The second line contains n unique integers representing the elements in the game. The function calculates the number of wins that can be achieved without swapping any elements and the number of wins that can be achieved with a single swap. It then prints the maximum of these two values. If the number of wins without swapping is greater than or equal to k, the function prints wins - 1. Otherwise, it calculates the number of wins that can be achieved with a swap and prints the maximum of wins - 1 and the number of wins with a swap minus the number of wins without a swap plus 1, if wins is not zero.

