#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains six integers: h, w, x_a, y_a, x_b, y_b. 1 <= x_a, x_b <= h <= 10^6, 1 <= y_a, y_b <= w <= 10^9. x_a != x_b or y_a != y_b.
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
        
    #State: `clues` is a list of integers from the input, `test_cases` is 0, `answers` is a list containing either 'Draw', 'Bob', or 'Alice', `i` is equal to the initial value of `test_cases`, stdin is empty.
    for j in answers:
        print(j)
        
    #State: `clues` is a list of integers from the input, `test_cases` is 0, `answers` is a list containing either 'Draw', 'Bob', or 'Alice' that must have at least 3 answers, `i` is equal to the initial value of `test_cases`, j is the last answer in the list, stdin is empty, and the last answer in the list which is either 'Draw', 'Bob', or 'Alice' is being printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of six integers: h, w, x_a, y_a, x_b, and y_b. It then determines the winner of a game based on the given coordinates and prints the result for each test case. The possible outcomes are 'Draw', 'Bob', or 'Alice'. The function processes all test cases and prints the corresponding results in the order they were received.

