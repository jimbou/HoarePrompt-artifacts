#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains six space-separated integers: h, w, x_a, y_a, x_b, y_b. h and w are positive integers. x_a, y_a, x_b, y_b are positive integers such that 1 <= x_a, x_b <= h and 1 <= y_a, y_b <= w.
    test_cases = int(input())
    answers = []
    for i in range(test_cases):
        clues = list(map(int, input().split(' ')))
        
        if clues[2] > clues[4] or clues[0] == 1:
            answers.append('Draw')
        elif clues[2] % 2 == 0 and clues[4] % 2 == 0 or clues[2] % 2 != 0 and clues[4
            ] % 2 != 0:
            if clues[3] == clues[5]:
                answers.append('Bob')
            elif clues[3] < clues[5]:
                if clues[5] - 1 > abs((clues[2] - clues[4]) // 2):
                    answers.append('Draw')
                else:
                    answers.append('Bob')
            elif clues[3] > clues[5]:
                if clues[1] - clues[5] > abs((clues[2] - clues[4]) // 2):
                    answers.append('Draw')
                else:
                    answers.append('Bob')
        elif clues[3] == clues[5]:
            answers.append('Alice')
        elif abs(clues[3] - clues[5]) == 1:
            answers.append('Alice')
        elif clues[3] < clues[5]:
            if clues[1] - clues[3] > abs((clues[2] - clues[4]) // 2):
                answers.append('Draw')
            else:
                answers.append('Alice')
        elif clues[3] > clues[5]:
            if clues[3] - 1 > abs((clues[2] - clues[4]) // 2):
                answers.append('Draw')
            else:
                answers.append('Alice')
        
    #State: `test_cases` is 0, `answers` is a list containing `test_cases` strings, `stdin` is empty, `i` is `test_cases`, `clues` is a list of integers containing the last test case.
    for j in answers:
        print(j)
        
    #State: `test_cases` is 0, `answers` is an empty list, `stdin` is empty, `i` is `test_cases`, `clues` is a list of integers containing the last test case, and all strings in the list `answers` have been printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of six space-separated integers representing the dimensions of a grid and the positions of two players. It then determines the winner of a game based on the positions of the players and the dimensions of the grid, and appends the result to a list. After processing all test cases, it prints the results for each test case. The function handles various scenarios, including cases where the players are in the same row or column, or where the distance between them is within a certain range. The function ultimately produces a list of strings indicating the winner of each test case, which are then printed to the console.

