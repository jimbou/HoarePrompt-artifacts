#State of the program right berfore the function call: t is a positive integer, cas_de_test is a list of lists of three integers each, each integer is between 0 and 30 inclusive, and the three integers in each sublist are non-decreasing.
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
        
    #State: `t` is a positive integer, `cas_de_test` is an empty list, `p1`, `p2`, `p3` are undefined, `total_points`, `total_matchs`, `egalites` are undefined, `resultats` is a list containing either -1 or `egalites // 2` for each sublist in the initial `cas_de_test` list.
    return resultats
    #The program returns a list of sublists, where each sublist contains either -1 or the value of `egalites // 2`, and `egalites` is an undefined variable.

#Overall this is what the function does:This function takes a list of test cases, where each test case is a list of three integers between 0 and 30, and returns a list of results. For each test case, it calculates the total points and checks if it's an even number. If it's not, it appends -1 to the results list. If it is, it calculates the total matches and checks if it's within a valid range. If it's not, it appends -1 to the results list. If it is, it calculates the number of equalities and checks if it's non-negative. If it's not, it appends -1 to the results list. If it is, it appends the number of equalities divided by 2 to the results list. The function returns the list of results, where each result is either -1 or a non-negative integer.

