#State of the program right berfore the function call: n and m are odd integers such that 3 <= n, m <= 99, grid is a 2D list of strings representing the game field, elements is a dictionary mapping entity names to their positions on the grid, allPlayers is a dictionary mapping player names to a boolean indicating whether they are carrying the Quaffle, goal is a list of lists of goal positions for each team, points is a list of integers representing the scores of each team, t is a non-negative integer representing the number of steps in the game, comand is a list of strings representing the commands for each step, obj is a string representing the entity performing the action, com is a string representing the action to be performed, el is a string representing the entity being interacted with (if applicable), mov is a dictionary mapping action strings to movement vectors, GoalName is a list of strings representing the names of the teams, isPlayer is a function that takes a string and returns a boolean indicating whether it represents a player, goalIn is a function that takes a position and returns the team number of the goal at that position (or -1 if no goal is present).
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
        
    #State: Output State: n is an odd integer between 3 and 99, m is an odd integer between 3 and 99, grid is a list of n lists of strings, elements is a dictionary with key-value pairs: '.B' maps to (-1, -1), and other key-value pairs where keys are strings from the input and values are pairs of integers, allPlayers is a dictionary with key-value pairs where keys are strings from the input and values are boolean values, goal is a list of two lists of pairs of integers, points is a list of two integers: [0, 0], t is a non-negative integer, comand is a list of strings, obj is a string, com is a string, el is a string, mov is a dictionary mapping action strings to movement vectors, GoalName is a list of strings, isPlayer is a function, goalIn is a function, stdin is empty.
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
        
    #State: The state of the game after t iterations, where t is the number of commands read from the input. The state includes the updated positions of the players and the ball, the points scored by each team, and the status of each player (active or eliminated). The game state is represented by the variables: elements (a dictionary mapping player and ball names to their positions), allPlayers (a dictionary mapping player names to their status), points (a list of two integers representing the points scored by each team), and GoalName (a list of two strings representing the names of the goals).
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where points[0] and points[1] are the points scored by each team)

#Overall this is what the function does:Simulates a game of Quidditch, processing a series of commands to update the game state, including player positions, ball position, points scored, and player status (active or eliminated), and prints the final score.

#State of the program right berfore the function call: pos is a pair of integers representing a position on the field, and goal is a list of two lists of pairs of integers, where each pair represents a goal position on the field, with the first list representing the goals of the red team and the second list representing the goals of the blue team.
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns the value of 'res', which is 0 if the position 'pos' is in the goals of the red team, 1 if the position 'pos' is in the goals of the blue team, and -1 otherwise.

#Overall this is what the function does:Determines the team affiliation of a given position on a field, returning 0 if the position is a goal of the red team, 1 if it's a goal of the blue team, and -1 if it's neither.

#State of the program right berfore the function call: el is a string of length 2, where the first character is either 'B', 'R', or '.' and the second character is either a digit from 0 to 9, 'G', or 'Q'.
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns a boolean value `res` that is `True` if the first character of the string `el` is either 'B' or 'R' and the second character is not 'G', otherwise it is `False`.

#Overall this is what the function does:This function evaluates a given 2-character string `el` and returns `True` if the first character is either 'B' or 'R' and the second character is not 'G', otherwise it returns `False`.

