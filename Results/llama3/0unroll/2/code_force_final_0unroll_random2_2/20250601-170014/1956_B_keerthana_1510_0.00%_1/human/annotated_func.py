#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the number of cards you and Nene receive in the beginning of the game), and then a space-separated list of integers (the integers on the cards in your hand). The list of integers is of the same length as the first integer, and each integer in the list is between 1 and the first integer (inclusive), and each integer from 1 through the first integer appears in the list at most 2 times.
    for line in [*open(0)][2::2]:
        elements = line.split()
        
        print(sum(elements.count(item) // 3 for item in {*elements}))
        
    #State: The output will be the sum of the counts of each integer in the list divided by 3, rounded down, for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (number of cards) followed by a space-separated list of integers (card values). It then calculates and prints the sum of the counts of each integer in the list divided by 3, rounded down, for each test case.

