#State of the program right berfore the function call: stdin contains multiple inputs: first two integers (n and m) separated by a space, then n lines of m pairs of characters separated by spaces, then an integer t, and then t lines each containing a command. The commands are either a pair of characters (obj and com) or a pair of characters and another pair of characters (obj, com, and el). The pair of characters obj represents an entity on the field, com represents the action to be performed, and el represents another entity on the field. The actions are either 'U', 'D', 'L', 'R', 'C', or 'T'. The entities are either players (represented by 'R0' to 'R9' and 'B0' to 'B9'), goals (represented by 'RG' and 'BG'), or the Quaffle (represented by '.Q').
    n, m = map(int, stdin.readline().strip().split())
    grid = []
    elements = {'.B': (0, 0)}
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
        
    #State: `n` is an integer, `m` is an integer, `grid` is a list of `n` lines each containing `m` pairs of characters, `elements` is a dictionary containing the key '.B' with the value (0, 0) and the keys of all non '..' elements in `grid` with their respective positions, `allPlayers` is a dictionary containing the keys of all players in `grid` with the value False, `goal` is a list containing two lists, the first list contains the positions of all 'BG' elements in `grid` and the second list contains the positions of all 'WG' elements in `grid`, `points` is a list containing two zeros, `stdin` contains `t` lines each containing a command.
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
        
    #State: `n` is an integer, `m` is an integer, `grid` is a list of `n` lines each containing `m` pairs of characters, `elements` is a dictionary containing the key '.B' with the value (0, 0) and the keys of all non '..' elements in `grid` with their respective positions, `goal` is a list containing two lists, the first list contains the positions of all 'BG' elements in `grid` and the second list contains the positions of all 'WG' elements in `grid`, `points` is a list containing two values, `t` is an integer, `stdin` is empty, `time` is `t-1`. `allPlayers` is a dictionary containing the keys of all players in `grid` with the value True if the player has caught the Golden Snitch, False otherwise. The values of `elements`, `points`, and `allPlayers` depend on the commands in `stdin`.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where points[0] and points[1] are the scores of the first and second players respectively, based on the commands in stdin and the state of the game)

#Overall this is what the function does:Simulates a Quidditch game based on input commands, tracking player movements, goals, and Golden Snitch catches, and outputs the final score.

#State of the program right berfore the function call: pos is a position on the field and goal is a list of two lists of positions, where the first list contains the positions of the red goals and the second list contains the positions of the blue goals.
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns the value of res, which is 0 if pos is in the red goals, 1 if pos is in the blue goals, and -1 otherwise.

#Overall this is what the function does:Determines the goal status of a given position on a field. It checks if the position is in the red goals, blue goals, or neither, and returns a corresponding value: 0 for red goals, 1 for blue goals, and -1 for positions not in any goal.

#State of the program right berfore the function call: el is a string of length 2, where the first character is either 'B', 'R', or '.' and the second character is either a digit from 0 to 9 or 'G' or 'Q'.
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns a boolean value indicating whether the first character of the string 'el' is either 'B' or 'R' and the second character is not 'G'.

#Overall this is what the function does:The function evaluates a given 2-character string 'el' and returns True if the first character is either 'B' or 'R' and the second character is not 'G', otherwise it returns False.

