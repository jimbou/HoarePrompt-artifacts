#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains two space-separated integers: the number of cows (n) and the index of the cow (k). The second line contains n space-separated integers representing the Cowdeforces ratings of the cows.
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: Output State: The value of wins is the number of elements in the list a that are less than or equal to the element at index k-1. The value of i is the index of the first element in the list a that is greater than the element at index k-1, or n if no such element exists. The values of n, k, and a remain unchanged.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: k-1 or more (where k-1 is the value of k minus 1)
        return
        #The program returns nothing, as there is no explicit return statement. The current state of the program remains unchanged, with the values of wins, i, n, k, and a remaining the same. The value of wins is still greater than or equal to k, and the value of wins minus one has been printed.
    #State: *The value of wins is the number of elements in the list a that are less than or equal to the element at index k-1. The value of i is the index of the first element in the list a that is greater than the element at index k-1, or n if no such element exists. The values of n, k, and a remain unchanged. The value of wins is less than k.
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: Output State: The value of `win_with_swap` is the number of elements in the list `a` that are less than or equal to the element at index `k-1`, plus the number of elements in the list `a` that are greater than the element at index `k-1` but are still less than or equal to the element at index `i-1`, the value of `i` is the index of the first element in the list `a` that is greater than the element at index `k-1`, or `n` if no such element exists, the values of `n`, `k`, and `a` remain unchanged, and the value of `win_with_swap` is less than or equal to `k`.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: The maximum of two values: (wins - 1) and (win_with_swap - wins - 1 + (wins != 0))

#Overall this is what the function does:This function determines the maximum number of wins a cow can achieve in a competition, considering the possibility of swapping the cow's rating with the rating of another cow. The function takes as input the number of cows (n), the index of the cow (k), and the ratings of all cows. It calculates the number of wins the cow can achieve without swapping and the number of wins it can achieve with swapping. The function then prints the maximum of these two values, which represents the maximum number of wins the cow can achieve. If the cow can achieve k-1 or more wins without swapping, the function prints k-1. Otherwise, it prints the maximum of the number of wins without swapping minus one and the number of wins with swapping minus the number of wins without swapping minus one, plus one if the cow can achieve at least one win without swapping.

