#State of the program right berfore the function call: n and m are odd integers such that 3 <= n, m <= 99.
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
        
    #State: `n` is an odd integer such that 3 <= n <= 99, `m` is an odd integer such that 3 <= m <= 99, `grid` is a list of n lists of strings, `elements` is a dictionary with key-value pairs for each element in the grid that is not '..', `allPlayers` is a dictionary with key-value pairs for each player in the grid, `goal` is a list of two lists containing the positions of 'B.G' and 'W.G' respectively, `points` is a list with two elements, both initialized to 0, `stdin` is not empty, `i` is n-1.
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
        
    #State: `n` is an odd integer such that 3 <= n <= 99, `m` is an odd integer such that 3 <= m <= 99, `grid` is a list of n lists of strings, `elements` is a dictionary with key-value pairs for each element in the grid that is not '..', `allPlayers` is a dictionary with key-value pairs for each player in the grid, `goal` is a list of two lists containing the positions of 'B.G' and 'W.G' respectively, `points` is a list with two elements, `stdin` is empty, `i` is n-1, `t` is an integer greater than or equal to 0, `time` is t-1, `comand` is a list of strings read from the last line of stdin. If `comand` has exactly 3 elements, then `obj` is the first string of the last line of stdin, `com` is the second string of the last line of stdin, and `el` is the third string of the last line of stdin. If `el` is '.Q', then the value of `obj` is set to True. If `el` is '.S', then the first element of `points` is 0 and the second element is 10, and '[time] [GoalName[team]] CATCH GOLDEN SNITCH' is printed where time is t-1 and GoalName[team] is the name of the team that caught the golden snitch. Otherwise, the state of the variables remains unchanged. If `comand` does not have exactly 3 elements, then `obj` is either '.B' or a player, `com` is the second element of `comand`, `pos` is the value of `elements[obj]`, and `nxt` is a tuple containing the new position of `obj` after moving in the direction specified by `com`. If `obj` is '.B' and the cell at the new position `nxt` is occupied by a player, or `obj` is a player and the cell at the new position `nxt` is occupied by '.B', then the player is eliminated and "time is t-1 and player is eliminated" is printed. Otherwise, if `com` is 'T', the value of `obj` in `allPlayers` is set to False and if the goal is scored, '[time] [GoalName[team]] GOAL' is printed where time is t-1 and GoalName[team] is the name of the goal of the team that scored, which is either 'B' or 'W', and the element at index team in points is incremented by 1. If `com` is not 'T', if `obj` is a player, then the value of `elements[obj]` is updated to `nxt`. Otherwise, the state of the program remains unchanged.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where points[0] and points[1] are the final scores of the two teams, which are integers)

#Overall this is what the function does:This function simulates a game where two teams, 'B' and 'W', compete to score points by moving players and the ball ('.B') around a grid. The game consists of a series of commands read from standard input, each representing a move or action. The function processes these commands, updating the game state accordingly. It eliminates players who collide with the ball or each other, scores goals when the ball reaches a goal position, and awards points for catching the golden snitch. The game ends after all commands have been processed, and the final score is printed to the console.

#State of the program right berfore the function call: pos is a pair of integers representing a position on the field, and goal is a list of two lists of pairs of integers, where each pair represents a goal position on the field.
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns the value of 'res', which indicates whether the position 'pos' is in 'goal[0]' (returns 0), in 'goal[1]' (returns 1), or not in either (returns -1).

#Overall this is what the function does:Determines the status of a given position on a field relative to two goal positions, returning 0 if the position is in the first goal, 1 if it's in the second goal, or -1 if it's in neither.

#State of the program right berfore the function call: el is a string of length 2, where the first character is either 'B', 'R', or '.', and the second character is either a digit from 0 to 9 or 'G' or 'Q'.
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns a boolean value indicating whether the first character of the string 'el' is 'B' or 'R' and the second character is not 'G'.

#Overall this is what the function does:This function evaluates a given 2-character string 'el' and returns True if the first character is either 'B' or 'R' and the second character is not 'G', otherwise it returns False.

