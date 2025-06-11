#State of the program right berfore the function call: sChar is a binary string (a string consisting of only 0-s and/or 1-s) of length at least 2 and at most 2 * 10^5.
    s = []
    for i in sChar:
        s.append(i)
        
    #State: Output State: `sChar` is a binary string of length at least 2 and at most 2 * 10^5, `s` is a list containing all the characters from `sChar`.
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
        
    #State: left is the index of the last '1' in s, right is the index of the last '0' in s, cost is the total number of swaps performed to move all '0's to the right of all '1's, s is the modified list with all '0's to the right of all '1's.
    return cost
    #The program returns the total number of swaps performed to move all '0's to the right of all '1's in the modified list s.

#Overall this is what the function does:This function takes a binary string `sChar` as input, converts it into a list `s`, and then rearranges the elements in `s` to move all '0's to the right of all '1's by swapping elements. The function returns the total number of swaps performed to achieve this rearrangement.

