#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains six integers: h, w, x_a, y_a, x_b, y_b, where h and w are positive integers representing the dimensions of the board, and x_a, y_a, x_b, y_b are positive integers representing the initial positions of Alice's and Bob's chips, respectively, such that 1 <= x_a, x_b <= h and 1 <= y_a, y_b <= w.
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
        
    #State: `test_cases` is a non-negative integer, `answers` is a list of strings where each string is either 'Draw', 'Bob', or 'Alice', and the length of `answers` is equal to `test_cases`. If `test_cases` is 0, `answers` is an empty list.
    for j in answers:
        print(j)
        
    #State: `test_cases` is a non-negative integer, `answers` is a list of strings where each string is either 'Draw', 'Bob', or 'Alice', and the length of `answers` is equal to `test_cases`, and all answers in the list have been printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains six integers representing the dimensions of a board and the initial positions of two chips, Alice's and Bob's. It then determines the outcome of a game based on the positions of the chips and the dimensions of the board, and appends the result ('Draw', 'Alice', or 'Bob') to a list. The function repeats this process for each test case and finally prints all the results.

