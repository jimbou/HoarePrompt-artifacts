#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by 2t lines, where each pair of lines contains two integers x and y of the same length, consisting of digits from 1 to 9.
    for _ in range(int(input())):
        a = list(map(int, list(input())))
        
        b = list(map(int, list(input())))
        
        new = [None] * len(a)
        
        new2 = [None] * len(a)
        
        mid = len(a) // 2
        
        i = 0
        
        while i < mid:
            new[i] = max(a[i], b[i])
            new2[i] = min(a[i], b[i])
            i += 1
        
        while i < len(a):
            new[i] = min(a[i], b[i])
            new2[i] = max(a[i], b[i])
            i += 1
        
        print(''.join(str(x) for x in new))
        
        print(''.join(str(x) for x in new2))
        
    #State: The output state will contain 2t lines, where each pair of lines contains two integers of the same length as the input integers, consisting of digits from 1 to 9. The first integer in each pair will have the maximum digits from the corresponding positions in the input integers up to the middle, and the minimum digits from the corresponding positions in the input integers after the middle. The second integer in each pair will have the minimum digits from the corresponding positions in the input integers up to the middle, and the maximum digits from the corresponding positions in the input integers after the middle.

#Overall this is what the function does:This function takes an integer t as input, followed by 2t pairs of integers, each consisting of digits from 1 to 9. It then generates two new integers for each pair, where the first integer has the maximum digits from the corresponding positions in the input integers up to the middle, and the minimum digits after the middle. The second integer has the minimum digits from the corresponding positions in the input integers up to the middle, and the maximum digits after the middle. The function prints these 2t pairs of new integers, with each pair on separate lines.

