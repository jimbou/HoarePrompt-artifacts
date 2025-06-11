#State of the program right berfore the function call: t is a positive integer, cas_de_test is a list of lists of three integers each, where each integer is between 0 and 30 inclusive, and the integers in each sublist are sorted in non-decreasing order.
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
        
    #State: t is a positive integer, cas_de_test is a list of lists of three integers each, where each integer is between 0 and 30 inclusive, and the integers in each sublist are sorted in non-decreasing order, and the list must have at least t sublists, p1, p2, p3 are the first three integers in the t-th sublist, total_points is equal to p1 + p2 + p3, total_matchs is equal to p1 + p2 + p3 // 2, egalites is equal to p1 + p2 + p3 - 2 * (p3 - p2) - 2 * (p3 - p1), resultats is a list containing t elements, where each element is either -1 or egalites // 2, depending on the values of total_points, total_matchs, and egalites.
    return resultats
    #The program returns a list of t elements, where each element is either -1 or the integer division of egalites by 2, depending on the values of total_points, total_matchs, and egalites, which are calculated based on the first three integers in the t-th sublist of cas_de_test, where each integer is between 0 and 30 inclusive, and the integers in each sublist are sorted in non-decreasing order.

#Overall this is what the function does:This function calculates the number of equalities for each set of three integers in a list of test cases. It takes a list of lists of three integers each, where each integer is between 0 and 30 inclusive, and the integers in each sublist are sorted in non-decreasing order. For each set of three integers, it calculates the total points, total matches, and equalities. If the total points are odd, or the total matches are more than 3, or the third integer is greater than the total matches, it returns -1. Otherwise, it returns the integer division of equalities by 2. The function returns a list of results, one for each set of three integers in the input list.

