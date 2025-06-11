#State of the program right berfore the function call: n and m are odd integers such that 3 <= n, m <= 99.
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
        
    #State: Output State: The grid is populated with n lines of input from stdin, each line split into a list of elements. The elements dictionary is updated with the positions of all non-'..' elements in the grid. The allPlayers dictionary contains all player elements from the grid with their initial state set to False. The goal list contains the positions of all 'G' elements in the grid, separated by team ('B' or 'W'). The values of n, m, and points remain unchanged.
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
        
    #State: The grid and elements dictionary are updated to reflect the final positions of all non-'..' elements after t iterations. The allPlayers dictionary contains the final state of all player elements, with True indicating a player has been freed and False indicating a player has been caught or is still in prison. The goal list and points remain unchanged. The values of n, m, and t are unchanged.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where points[0] is the first element of the points list and points[1] is the second element of the points list)

#Overall this is what the function does:This function simulates a game where players move around a grid, interact with each other, and score points. The game starts with an initial grid configuration read from standard input, where players and other elements are placed. The function then processes a series of commands, also read from standard input, which determine the actions taken by players and other elements. The game state is updated after each command, and the function prints out messages to indicate significant events, such as players being eliminated, goals being scored, or the golden snitch being caught. The game ends after a specified number of iterations, and the final score is printed out. The function does not return any value but prints the final score to the console.

#State of the program right berfore the function call: pos is a pair of integers representing a position on the field, and goal is a list of two lists of pairs of integers, where each pair represents a goal position on the field, with the first list containing the red goals and the second list containing the blue goals.
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns res, which is 0 if pos is in the red goals, 1 if pos is in the blue goals, and -1 otherwise.

#Overall this is what the function does:Determines the goal status of a given position on a field. It checks if the position is in the red goals, blue goals, or neither, and returns a corresponding value: 0 for red goals, 1 for blue goals, and -1 for no goal.

#State of the program right berfore the function call: el is a string of length 2, where the first character is either 'B', 'R', or '.', and the second character is either a digit from 0 to 9 or 'G' or 'Q'.
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns a boolean value indicating whether the first character of the string 'el' is 'B' or 'R' and the second character is not 'G'.

#Overall this is what the function does:Determines whether a given 2-character string meets specific conditions, returning True if the first character is 'B' or 'R' and the second character is not 'G', and False otherwise.

