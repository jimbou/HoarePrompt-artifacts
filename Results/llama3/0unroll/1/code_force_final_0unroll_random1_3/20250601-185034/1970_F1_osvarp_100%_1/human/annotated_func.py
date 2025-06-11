#State of the program right berfore the function call: n and m are positive integers such that 3 <= n, m <= 99 and n and m are odd.
    n, m = map(int, stdin.readline().strip().split())
    grid = []
    elements = {'.B': (-1, -1)}
    allPlayers = {}
    goal = [[], []]
    points = [0, 0]
    for i in range(n):
        line = stdin.readline().strip().split()
        
        grid.append(line)
        
        for ind in range(len(line)):
            if line[ind] != '..':
                elements[line[ind]] = i, ind
                if isPlayer(line[ind]):
                    allPlayers[line[ind]] = False
                elif line[ind][1] == 'G':
                    tmp = 0 if line[ind][0] == 'B' else 1
                    goal[tmp].append((i, ind))
        
    #State: Output State: The grid is populated with n lines of input from stdin, where each line is a list of strings. The elements dictionary is updated to include the positions of all non-'..' elements in the grid. The allPlayers dictionary is populated with player elements from the grid, initially set to False. The goal list contains lists of positions of 'G' elements in the grid, separated by player ('B' or 'W'). The values of n, m, stdin, and points remain unchanged.
    t = int(stdin.readline().strip())
    for time in range(t):
        comand = stdin.readline().strip().split()
        
        if len(comand) == 3:
            obj, com, el = comand
            if el == '.Q':
                allPlayers[obj] = True
            elif el == '.S':
                team = 1 if obj[0] == 'B' else 0
                points[team] += 10
                print('%d %s CATCH GOLDEN SNITCH' % (time, GoalName[team]))
        else:
            obj, com = comand
            pos = elements[obj]
            nxt = pos[0] + mov[com][0], pos[1] + mov[com][1]
            if obj == '.B' and isPlayer(grid[nxt[0]][nxt[1]]) or isPlayer(obj
                ) and elements['.B'] == nxt:
                player = obj if isPlayer(obj) else grid[nxt[0]][nxt[1]]
                print('%d %s ELIMINATED' % (time, player))
            elif com == 'T':
                allPlayers[obj] = False
                if goalIn(pos) != -1:
                    team = goalIn(pos)
                    print('%d %s GOAL' % (time, GoalName[team]))
                    points[team] += 1
            elif isPlayer(obj):
                elements[obj] = nxt
            if obj == '.B':
                elements[obj] = nxt
        
    #State: The grid has been updated to reflect the final positions of all elements after t iterations. The elements dictionary contains the final positions of all non-'..' elements in the grid. The allPlayers dictionary has been updated to reflect the final status of each player (True if they have been eliminated, False otherwise). The goal list remains unchanged. The points list has been updated to reflect the final score of each team. The values of n, m, stdin, and mov remain unchanged.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where points[0] and points[1] are the final scores of the two teams)

#Overall this is what the function does:This function simulates a game where two teams, 'B' and 'W', compete to score points by moving elements on a grid. The game starts with an initial grid configuration, where each team has a player and a goal. The function reads a series of commands from standard input, which specify movements or actions for the elements on the grid. The function updates the grid and the elements' positions accordingly, keeping track of the score and the status of each player. The game ends after a specified number of iterations, and the final score is printed to the console. The function also prints messages to the console when a player is eliminated, a goal is scored, or a player catches the golden snitch.

#State of the program right berfore the function call: pos is a position on the field, goal is a list of two lists of positions, where the first list contains the positions of the red goals and the second list contains the positions of the blue goals.
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns the value of 'res', which is 0 if the position 'pos' is in the red goals, 1 if the position 'pos' is in the blue goals, and -1 otherwise.

#Overall this is what the function does:Determines the goal status of a given position on a field. It checks if the position is in the red goals, blue goals, or neither, and returns a corresponding value: 0 for red goals, 1 for blue goals, and -1 for any other position.

#State of the program right berfore the function call: el is a string of length 2, where the first character is either 'B', 'R', or '.', and the second character is either a digit from 0 to 9 or 'G' or 'Q'.
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns a boolean value indicating whether the first character of the string 'el' is either 'B' or 'R' and the second character is not 'G'.

#Overall this is what the function does:This function evaluates a given 2-character string 'el' and returns True if the first character is either 'B' or 'R' and the second character is not 'G', otherwise it returns False.

