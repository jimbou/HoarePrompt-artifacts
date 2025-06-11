#State of the program right berfore the function call: t is a positive integer, cas_de_test is a list of lists of three integers each, each integer is between 0 and 30 inclusive, and the integers in each sublist are sorted in non-decreasing order.
    resultats = []
    for (p1, p2, p3) in cas_de_test:
        total_points = p1 + p2 + p3
        
        if total_points % 2 != 0:
            resultats.append(-1)
            continue
        
        total_matchs = total_points // 2
        
        if total_matchs > 3 or p3 > total_matchs:
            resultats.append(-1)
            continue
        
        egalites = total_points - 2 * (p3 - p2) - 2 * (p3 - p1)
        
        if egalites < 0:
            resultats.append(-1)
        else:
            resultats.append(egalites // 2)
        
    #State: Output State: `t` is a positive integer, `cas_de_test` is a list of lists of three integers each, each integer is between 0 and 30 inclusive, and the integers in each sublist are sorted in non-decreasing order, `resultats` is a list of integers, where each integer is either -1 or a non-negative integer less than or equal to 15.
    return resultats
    #The program returns a list of integers, where each integer is either -1 or a non-negative integer less than or equal to 15.

#Overall this is what the function does:This function takes a list of lists of three integers each as input, where each integer is between 0 and 30 inclusive, and the integers in each sublist are sorted in non-decreasing order. It calculates the number of possible draws in a series of matches, given the total points earned by each team. If the total points are odd or if the number of matches is invalid, it returns -1 for that case. Otherwise, it returns the number of draws, which is a non-negative integer less than or equal to 15. The function returns a list of these results, one for each case in the input list.

