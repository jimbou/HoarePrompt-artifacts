#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 10^4) — the number of test cases. Each test case consists of a single line containing six integers h, w, x_a, y_a, x_b, y_b (1 <= x_a, x_b <= h <= 10^6, 1 <= y_a, y_b <= w <= 10^9) — the dimensions of the board and the initial positions of Alice's and Bob's chips. It is guaranteed that either x_a != x_b or y_a != y_b.
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
        
    #State: `test_cases` is an integer between 1 and 10^4, `answers` is a list containing either the string 'Draw', 'Bob', or 'Alice' for each test case, `clues` is a list of integers, `i` is equal to `test_cases`, stdin contains no test cases. The length of `answers` is equal to `test_cases`.
    for j in answers:
        print(j)
        
    #State: `test_cases` is an integer between 1 and 10^4, `answers` is a list containing either the string 'Draw', 'Bob', or 'Alice' for each test case, `clues` is a list of integers, `i` is equal to `test_cases`, stdin contains no test cases, and all elements of the `answers` list which are either 'Draw', 'Bob', or 'Alice' have been printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of six integers representing the dimensions of a board and the initial positions of two chips, Alice's and Bob's. It then determines the winner of a game based on the positions of the chips and the dimensions of the board, and prints the result for each test case. The possible outcomes are 'Draw', 'Bob', or 'Alice', indicating whether the game is a draw or which player wins. The function processes all test cases and prints the results in the order they were input.

