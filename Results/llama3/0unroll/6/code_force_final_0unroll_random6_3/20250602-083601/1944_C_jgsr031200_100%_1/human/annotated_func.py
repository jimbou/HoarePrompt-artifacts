#State of the program right berfore the function call: arr is a list of non-negative integers.
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: Output State: `arr` is a list of non-negative integers, `freq` is a list where the value at each index `i` represents the frequency of `i` in `arr`.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: Output State: The loop will print the smallest number that appears at most once in `arr` and then terminate. The value of `cou` will be 1 plus the number of numbers that appear exactly once in `arr` and are smaller than the printed number. The value of `freq` will remain unchanged.

#Overall this is what the function does:The function takes a list of non-negative integers and prints the smallest number that appears at most once in the list. If no such number exists, it prints the smallest number in the list. The function does not modify the input list.

