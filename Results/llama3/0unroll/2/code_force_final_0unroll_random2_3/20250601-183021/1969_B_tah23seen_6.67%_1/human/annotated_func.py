#State of the program right berfore the function call: sChar is a string consisting of only 0-s and/or 1-s and has a length between 2 and 2 * 10^5 (inclusive).
    s = []
    for i in sChar:
        s.append(i)
        
    #State: Output State: `s` is a list of characters where each character is either '0' or '1', and has the same length as `sChar`. `sChar` remains unchanged.
    left = 0
    cost = 0
    right = 1
    while left <= right and right < len(s) and (left < len(s)):
        if s[right] == '0' and s[left] == '1':
            s[right], s[left] = s[left], s[right]
            cost += right - left + 1
        
        while right < len(s) and s[right] != '0':
            right += 1
        
        while left < len(s) and s[left] != '1':
            left += 1
        
    #State: left is the index of the last '1' in s, right is the index of the last '0' in s, cost is the total number of swaps made, and s is sorted such that all '0's are on the right and all '1's are on the left.
    return cost
    #The program returns the total number of swaps made to sort the string s such that all '0's are on the right and all '1's are on the left.

#Overall this is what the function does:Functionality: This function takes a string of binary digits (0s and 1s) as input and returns the minimum number of swaps required to sort the string such that all 0s are on the right and all 1s are on the left. The function does not modify the original input string. It creates a copy of the input string, sorts it in-place, and counts the number of swaps performed during the sorting process. The function returns the total number of swaps made to achieve the sorted state.

