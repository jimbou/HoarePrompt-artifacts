#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains six integers h, w, x_a, y_a, x_b, y_b. h and w are positive integers. x_a, y_a, x_b, y_b are positive integers such that 1 <= x_a, x_b <= h and 1 <= y_a, y_b <= w. Either x_a != x_b or y_a != y_b.
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
                if abs(clues[3] - clues[5]) > 1:
                    if clues[3] - 1 >= abs((clues[2] - clues[4]) // 2) or clues[5
                        ] - clues[3] >= abs((clues[2] - clues[4]) // 2):
                        answers.append('Draw')
                    else:
                        answers.append('Bob')
                elif clues[3] - 1 > abs((clues[2] - clues[4]) // 2) or clues[5
                    ] - clues[3] > abs((clues[2] - clues[4]) // 2):
                    answers.append('Draw')
                else:
                    answers.append('Bob')
            elif clues[3] > clues[5]:
                if abs(clues[3] - clues[5]) > 1:
                    if clues[1] - clues[3] >= abs((clues[2] - clues[4]) // 2) or clues[
                        3] - clues[5] >= abs((clues[2] - clues[4]) // 2):
                        answers.append('Draw')
                    else:
                        answers.append('Bob')
                elif clues[1] - clues[3] > abs((clues[2] - clues[4]) // 2) or clues[3
                    ] - clues[5] > abs((clues[2] - clues[4]) // 2):
                    answers.append('Draw')
                else:
                    answers.append('Bob')
        elif clues[3] == clues[5]:
            answers.append('Alice')
        elif clues[3] < clues[5]:
            if abs(clues[3] - clues[5]) > 1:
                if clues[1] - clues[5] > abs((clues[2] - clues[4]) // 2) or clues[5
                    ] - clues[3] > abs((clues[2] - clues[4]) // 2):
                    answers.append('Draw')
                else:
                    answers.append('Alice')
            elif clues[1] - clues[5] - 1 > abs((clues[2] - clues[4]) // 2) or clues[5
                ] - clues[3] - 1 > abs((clues[2] - clues[4]) // 2):
                answers.append('Draw')
            else:
                answers.append('Alice')
        elif clues[3] > clues[5]:
            if abs(clues[3] - clues[5]) > 1:
                if clues[5] - 1 > abs((clues[2] - clues[4]) // 2) or clues[3] - clues[5
                    ] > abs((clues[2] - clues[4]) // 2):
                    answers.append('Draw')
                else:
                    answers.append('Alice')
            elif clues[5] - 1 - 1 > abs((clues[2] - clues[4]) // 2) or clues[3
                ] - clues[5] - 1 > abs((clues[2] - clues[4]) // 2):
                answers.append('Draw')
            else:
                answers.append('Alice')
        
    #State: `test_cases` is an integer greater than or equal to 0, `answers` is a list containing either 'Draw', 'Bob', or 'Alice', `i` is equal to `test_cases`, `clues` is a list of two integers, stdin contains no test cases.
    for j in answers:
        print(j)
        
    #State: `test_cases` is an integer greater than or equal to 0, `answers` is a list containing either 'Draw', 'Bob', or 'Alice' that must have at least as many answers as `test_cases`, `i` is equal to `test_cases`, `clues` is a list of two integers, stdin contains no test cases, j is the last answer in the list, and the last answer in the list which is either 'Draw', 'Bob', or 'Alice' is being printed.

#Overall this is what the function does:This function determines the winner of a game based on the positions of two players, Alice and Bob, on a grid. It takes multiple test cases as input, where each test case consists of six integers: the height and width of the grid, and the x and y coordinates of Alice and Bob. The function then analyzes the positions and determines the winner of each game, either Alice, Bob, or a draw. The results are stored in a list and printed out at the end. The function handles various scenarios, including cases where the players are on the same row or column, and where the distance between them is greater than the difference in their x or y coordinates.

