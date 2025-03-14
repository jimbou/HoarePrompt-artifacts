#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input consists of n lines, each containing n characters. The j-th character of the i-th line is either 'F', 'S', '?', or '.', where 'F' indicates a funny transition video, 'S' indicates a scary transition video, '?' indicates an undecided transition video, and '.' indicates i=j. It is guaranteed that the i-th character of the j-th line and the j-th character of the i-th line are the same for all i and j. At most floor(n/2) characters in the input are 'F' or 'S'.
def func():
    n = int(input())
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    xx = ['']
    for i in range(1, n + 1):
        x = input()
        
        for j in range(1, n + 1):
            if x[j - 1] == 'F':
                a[i] += 1
                a[j] += 1
            elif x[j - 1] == 'S':
                b[i] += 1
                b[j] += 1
        
        xx.append(x)
        
    #State: `n` is an integer such that 2 <= `n` <= 24, `a` is a list of `n + 1` integers reflecting 'F' relationships, `b` is a list of `n + 1` integers reflecting 'S' relationships, `xx` is a list of `n + 1` strings, where the first string is an empty string and the remaining `n` strings are the input strings.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: `n` is an integer such that 2 <= `n` <= 24, `a` is a list of `n + 1` integers reflecting 'F' relationships, `b` is a list of `n + 1` integers reflecting 'S' relationships, `xx` is a list of `n + 1` strings, where the first string is an empty string and the remaining `n` strings are the input strings, `sa` is a list of indices where there is a 'F' relationship but no 'S' relationship, `sb` is a list of indices where there is an 'S' relationship but no 'F' relationship.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: `n` is an integer such that 2 <= `n` <= 24, `a` is a list of `n + 1` integers reflecting 'F' relationships, `b` is a list of `n + 1` integers reflecting 'S' relationships, `xx` is a list of `n + 1` strings, where the first string is an empty string and the remaining `n` strings are the input strings, `sa` is a list of indices where there is a 'F' relationship but no 'S' relationship, plus any additional indices where both `a[i]` and `b[i]` are 0, `sb` is a list of indices where there is an 'S' relationship but no 'F' relationship, and the length of `sa` is greater than or equal to the length of `sb`; `t` is the length of `sa` before the loop started.
        for i in range(1, n + 1):
            nx = ''
            
            for j in range(1, n + 1):
                if xx[i][j - 1] != '?':
                    nx += xx[i][j - 1]
                elif i in sa[:n // 4 - 1] or j in sa[:n // 4 - 1]:
                    nx += 'F'
                else:
                    nx += 'S'
            
            print(nx)
            
        #State: `n` is an integer such that 2 <= `n` <= 24, `a` is a list of `n + 1` integers reflecting 'F' relationships, `b` is a list of `n + 1` integers reflecting 'S' relationships, `xx` is a list of `n + 1` strings where each '?' in the strings from index 1 to `n` is replaced by 'F' or 'S' based on the conditions in the loop, `sa` is a list of indices where there is a 'F' relationship but no 'S' relationship, plus any additional indices where both `a[i]` and `b[i]` are 0, `sb` is a list of indices where there is an 'S' relationship but no 'F' relationship, and the length of `sa` is greater than or equal to the length of `sb`; `t` is the length of `sa` before the loop started.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `n` is an integer such that 2 <= `n` <= 24, `a` is a list of `n + 1` integers reflecting 'F' relationships, `b` is a list of `n + 1` integers reflecting 'S' relationships, `xx` is a list of `n + 1` strings, where the first string is an empty string and the remaining `n` strings are the input strings, `sa` is a list of indices where there is a 'F' relationship but no 'S' relationship, `sb` is a list of indices where there is an 'S' relationship but no 'F' relationship, and the length of `sa` is less than or equal to the length of `sb` (since `sb` might have grown by including additional indices where both `a[i]` and `b[i]` are `0`).
        for i in range(1, n + 1):
            nx = ''
            
            for j in range(1, n + 1):
                if xx[i][j - 1] != '?':
                    nx += xx[i][j - 1]
                elif i in sb[:n // 4 - 1] or j in sb[:n // 4 - 1]:
                    nx += 'S'
                else:
                    nx += 'F'
            
            print(nx)
            
        #State: `xx` is a list of `n + 1` strings where the first string is an empty string and the remaining `n` strings have each '?' replaced by 'S' if the corresponding index conditions are met, otherwise by 'F'. The `a`, `b`, `sa`, and `sb` lists remain unchanged.
    #State: `n` is an integer such that 2 <= `n` <= 24, `a` is a list of `n + 1` integers reflecting 'F' relationships, `b` is a list of `n + 1` integers reflecting 'S' relationships, `xx` is a list of `n + 1` strings where each '?' in the strings from index 1 to `n` is replaced by 'F' or 'S' based on the conditions in the loop, `sa` is a list of indices where there is a 'F' relationship but no 'S' relationship, plus any additional indices where both `a[i]` and `b[i]` are 0, `sb` is a list of indices where there is an 'S' relationship but no 'F' relationship. If the length of `sa` is greater than or equal to the length of `sb`, `t` is the length of `sa` before the loop started. Otherwise, `xx` is a list of `n + 1` strings where the first string is an empty string and the remaining `n` strings have each '?' replaced by 'S' if the corresponding index conditions are met, otherwise by 'F', and the `a`, `b`, `sa`, and `sb` lists remain unchanged.
#Overall this is what the function does:The function accepts an integer `n` and an `n x n` matrix where each element is either 'F', 'S', '?', or '.'. It processes this matrix to replace each '?' with either 'F' or 'S' based on specific conditions, ensuring that no more than floor(n/2) characters in the entire matrix are 'F' or 'S'. The function then prints the modified matrix.

