def solve(s):
    ans = 0
    i = 0
    n = len(s)
    
    while i < n:
        if s[i:i+5] == 'mapie':  # Check for 'mapie'
            ans += 1
            i += 5  # Move pointer ahead by 5 characters
        elif s[i:i+3] == 'map':  # Check for 'map'
            ans += 1
            i += 3  # Move pointer ahead by 3 characters
        elif s[i:i+3] == 'pie':  # Check for 'pie'
            ans += 1
            i += 3  # Move pointer ahead by 3 characters
        else:
            i += 1  # Move pointer by 1 character if no match
    
    return ans
 
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(s))