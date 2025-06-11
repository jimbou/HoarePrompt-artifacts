#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t pairs of integers x and y, where x and y are strings of digits from 1 to 9 and have the same length.
    for _ in range(int(input())):
        a = list(map(int, list(input())))
        
        b = list(map(int, list(input())))
        
        new = [None] * len(a)
        
        new2 = [None] * len(a)
        
        i = 0
        
        while i < len(a) and a[i] == b[i]:
            new[i] = max(a[i], b[i])
            new2[i] = min(a[i], b[i])
            i += 1
        
        if i != len(a):
            new[i] = max(a[i], b[i])
            new2[i] = min(a[i], b[i])
            i += 1
            while i < len(a):
                new[i] = min(a[i], b[i])
                new2[i] = max(a[i], b[i])
                i += 1
        
        print(''.join(str(x) for x in new))
        
        print(''.join(str(x) for x in new2))
        
    #State: a is a list of integers with at least t elements, the first element equal to the first element of b, the second element equal to the second element of b, the third element equal to the third element of b, the fourth element equal to the fourth element of b, b is a list of integers, new is a list of integers with the first element equal to the maximum of the first elements of a and b, the second element equal to the maximum of the second elements of a and b, the third element equal to the maximum of the third elements of a and b, and the rest of the elements equal to the minimum of the corresponding elements of a and b, except for the elements from index 0 to i-1 which are now equal to the minimum of the corresponding elements of a and b if i is not equal to the length of a, otherwise the rest of the elements are equal to the minimum of the corresponding elements of a and b, new2 is a list of integers with the first element equal to the minimum of the first elements of a and b, the second element equal to the minimum of the second elements of a and b, the third element equal to the minimum of the third elements of a and b, and the rest of the elements equal to the maximum of the corresponding elements of a and b, except for the elements from index 0 to i-1 which are now equal to the maximum of the corresponding elements of a and b if i is not equal to the length of a, otherwise the rest of the elements are equal to the maximum of the corresponding elements of a and b, i is equal to the length of a, t is greater than the current length of a, stdin contains 0 pairs of integers x and y, where x and y are strings of digits from 1 to 9 and have the same length, and this is printed: a string of digits representing the elements of the new2 list, where the first three elements are the minimum of the corresponding elements of a and b, and the rest of the elements are the maximum of the corresponding elements of a and b.

#Overall this is what the function does:This function reads pairs of integers from standard input, where each pair represents two strings of digits with the same length. It then generates two new strings by comparing the corresponding digits of the input strings. The first new string has the maximum digit at the first differing position and the minimum digits at all other positions, while the second new string has the minimum digit at the first differing position and the maximum digits at all other positions. The function prints these two new strings for each pair of input strings.

