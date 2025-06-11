#State of the program right berfore the function call: t is a positive integer, cas_de_test is a list of lists of three integers each, where each integer is between 0 and 30 (inclusive), and the integers in each sublist are sorted in non-decreasing order.
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
        
    #State: Output State: The value of `t` remains unchanged, `cas_de_test` remains unchanged, and `resultats` is a list of integers where each integer is either -1 or a non-negative integer less than or equal to 30.
    return resultats
    #The program returns a list of integers named 'resultats' where each integer in the list is either -1 or a non-negative integer less than or equal to 30.

#Overall this is what the function does:This function takes a list of test cases, where each test case is a list of three integers between 0 and 30, and returns a list of integers. For each test case, it calculates the total points and checks if it's even. If it's not, it appends -1 to the result list. If it is, it calculates the total matches and checks if it's within a valid range. If it's not, it appends -1 to the result list. If it is, it calculates the number of equalities and appends it to the result list if it's non-negative, otherwise appends -1. The function returns a list of integers, where each integer is either -1 or a non-negative integer less than or equal to 30, without modifying the input list.

