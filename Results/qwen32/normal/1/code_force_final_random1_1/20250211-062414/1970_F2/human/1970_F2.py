"""
https://codeforces.com/problemset/problem/1970/F2
F2. Playing Quidditch (Medium)
"""
 
n, m = [int(x) for x in input().split()]
players = dict()
goals = {"B": [], "R": []}
mouvements = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}
middle = ((m + 1) // 2, (n + 1) // 2)
quidditch = [middle, ""]
pointsb, pointsr = 0, 0
 
for y in range(n):
    s = input().split()
    for x in range(m):
        if s[x] == "..":
            continue
        elif s[x] == ".Q":
            quidditch[0] = (x, y)
        elif s[x] == "RG":
            goals["R"].append((x, y))
        elif s[x] == "BG":
            goals["B"].append((x, y))
        else:
            players[s[x]] = (x, y)
 
 
def add(a, b):
    x, y = a
    dx, dy = b
    return x + dx, y + dy
 
 
moves = int(input())
for i in range(moves):
    mo = input().split()
    if mo[0] == ".Q":
        quidditch[0] = add(quidditch[0], mouvements[mo[1]])
    elif mo[1] in "ULDR":
        players[mo[0]] = add(players[mo[0]], mouvements[mo[1]])
        if ".B" in players:
            elimines = []
            for k, v in players.items():
                if k != ".B" and v == players[".B"]:
                    elimines.append(k)
            elimines.sort()
            for c in elimines:
                print(i, c, "ELIMINATED")
                if quidditch[1] == c:
                    quidditch = [players[c], ""]
                del players[c]
    elif mo[1] == "C":
        quidditch[1] == mo[0]
    elif mo[1] == "T":
        quidditch[1] = ""
        if players[mo[0]] in goals["R"]:
            pointsb += 1
            print(i, "BLUE GOAL")
            if mo[0][0] == "R":
                quidditch[0] = middle
            else:
                quidditch[0] = players[mo[0]]
        if players[mo[0]] in goals["B"]:
            pointsr += 1
            print(i, "RED GOAL")
            if mo[0][0] == "B":
                quidditch[0] = middle
            else:
                quidditch[0] = players[mo[0]]
print("FINAL SCORE:", pointsr, pointsb)