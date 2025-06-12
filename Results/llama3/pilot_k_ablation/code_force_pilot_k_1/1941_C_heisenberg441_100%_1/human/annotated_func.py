#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters.
    ans = 0
    i = 0
    n = len(s)
    while i < n:
        if s[i:i + 5] == 'mapie':
            ans += 1
            i += 5
        elif s[i:i + 3] == 'map':
            ans += 1
            i += 3
        elif s[i:i + 3] == 'pie':
            ans += 1
            i += 3
        else:
            i += 1
        
    #State: `s` is a string consisting of lowercase Latin letters, `n` is the length of `s`, `i` is equal to `n`, `ans` is the number of non-overlapping occurrences of 'mapie', 'map', or 'pie' in `s`.
    return ans
    #The program returns the number of non-overlapping occurrences of 'mapie', 'map', or 'pie' in string `s` that consists of lowercase Latin letters.

#Overall this is what the function does:Counts the number of non-overlapping occurrences of 'mapie', 'map', or 'pie' in a given string of lowercase Latin letters and returns the count.

