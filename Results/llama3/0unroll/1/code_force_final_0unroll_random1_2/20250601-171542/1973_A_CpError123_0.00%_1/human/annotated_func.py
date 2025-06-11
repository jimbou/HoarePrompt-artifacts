#State of the program right berfore the function call: t is a positive integer, cas_de_test is a list of lists of three non-negative integers each, sorted in non-decreasing order.
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
        
    #State: Output State: `t` is a positive integer, `cas_de_test` is a list of lists of three non-negative integers each, sorted in non-decreasing order, `resultats` is a list of integers.
    return resultats
    #The program returns a list of integers 'resultats'

#Overall this is what the function does:This function takes a positive integer `t` and a list of lists `cas_de_test`, where each sublist contains three non-negative integers in non-decreasing order. It calculates the number of possible equalities in a series of matches, where the total points are distributed among three teams. If the total points are odd or the number of matches is invalid, it returns -1 for that case. Otherwise, it calculates the number of equalities based on the points distribution and returns the result as a list of integers. The function returns a list of integers, where each integer represents the number of possible equalities for each case in the input list, or -1 if the case is invalid.

