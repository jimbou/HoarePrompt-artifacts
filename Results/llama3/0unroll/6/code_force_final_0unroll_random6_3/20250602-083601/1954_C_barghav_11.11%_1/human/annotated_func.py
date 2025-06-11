#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t pairs of integers x and y, where x and y are strings of digits from 1 to 9 and have the same length.
    a = list(input())
    b = list(input())
    for i in range(len(a)):
        if i <= len(a) // 2 - 1:
            n = min(a[i], b[i])
            m = max(a[i], b[i])
            a[i] = m
            b[i] = n
        else:
            n = min(a[i], b[i])
            m = max(a[i], b[i])
            a[i] = n
            b[i] = m
        
    #State: Output State: The first half of the list a contains the maximum digit from the corresponding pairs of digits from the initial lists a and b, and the second half of the list a contains the minimum digit from the corresponding pairs of digits from the initial lists a and b. The first half of the list b contains the minimum digit from the corresponding pairs of digits from the initial lists a and b, and the second half of the list b contains the maximum digit from the corresponding pairs of digits from the initial lists a and b.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: Output State: The first half of the list a contains the maximum digit from the corresponding pairs of digits from the initial lists a and b, and the second half of the list a contains the minimum digit from the corresponding pairs of digits from the initial lists a and b. The first half of the list b contains the minimum digit from the corresponding pairs of digits from the initial lists a and b, and the second half of the list b contains the maximum digit from the corresponding pairs of digits from the initial lists a and b.
    print()
    #This is printed: The first half of the list a contains the maximum digit from the corresponding pairs of digits from the initial lists a and b, and the second half of the list a contains the minimum digit from the corresponding pairs of digits from the initial lists a and b. The first half of the list b contains the minimum digit from the corresponding pairs of digits from the initial lists a and b, and the second half of the list b contains the maximum digit from the corresponding pairs of digits from the initial lists a and b.
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: Output State: The first half of the list a contains the maximum digit from the corresponding pairs of digits from the initial lists a and b, and the second half of the list a contains the minimum digit from the corresponding pairs of digits from the initial lists a and b. The first half of the list b contains the minimum digit from the corresponding pairs of digits from the initial lists a and b, and the second half of the list b contains the maximum digit from the corresponding pairs of digits from the initial lists a and b, and the digits of list b are printed in order.
    print()
    #This is printed: The digits of list b, where the first half of the list contains the minimum digit from the corresponding pairs of digits from the initial lists a and b, and the second half of the list contains the maximum digit from the corresponding pairs of digits from the initial lists a and b, in order.

#Overall this is what the function does:This function takes two lists of digits as input, swaps the digits in the first half of the lists to ensure the maximum digit is in the first list and the minimum digit is in the second list, and swaps the digits in the second half of the lists to ensure the minimum digit is in the first list and the maximum digit is in the second list. It then prints the modified first list followed by the modified second list.

