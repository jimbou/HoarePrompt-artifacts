#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input is a list of n strings, each of length n, where each string represents a row in the transition video plan. The characters in the strings are either 'F' (funny), 'S' (scary), '?' (undecided), or '.' (same scenario, no transition). The matrix is symmetric, and at most \lfloor \frac{n}{2} \rfloor transition videos are already decided.
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
        
    #State: After the loop executes all iterations, `a` and `b` will contain the counts of 'F' and 'S' transitions for each row and column, respectively, and `xx` will be a list containing the empty string followed by the n input strings. The values of `n` and the input matrix remain unchanged.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: `sa` contains the row indices where there is at least one 'F' transition and no 'S' transitions, and `sb` contains the column indices where there is at least one 'S' transition and no 'F' transitions. The values of `n` and `xx` remain unchanged.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: `sa` contains the row indices where there is at least one 'F' transition and no 'S' transitions, plus any additional indices `i` from 1 to `n` where both `a[i]` and `b[i]` are 0. `sb` remains unchanged, and the values of `n` and `xx` remain unchanged.
        for i in range(1, n + 1):
            nx = ''
            
            for j in range(1, n + 1):
                if xx[i][j - 1] != '?':
                    nx += xx[i][j - 1]
                elif i in sa[:n // 4] or j in sa[:n // 4]:
                    nx += 'F'
                else:
                    nx += 'S'
            
            print(nx)
            
        #State: The loop does not modify the values of `sa`, `sb`, `n`, or `xx`. The loop only prints the modified strings `nx` for each iteration of `i` from 1 to `n`. Therefore, the output state is the same as the initial state: `sa` contains the row indices where there is at least one 'F' transition and no 'S' transitions, plus any additional indices `i` from 1 to `n` where both `a[i]` and `b[i]` are 0. `sb` remains unchanged, and the values of `n` and `xx` remain unchanged.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `sa` remains unchanged, `sb` may have additional elements appended, which are the row indices where both `a[i]` and `b[i]` are 0, and the length of `sa` is still less than the length of `sb`. The values of `n` and `xx` remain unchanged.
        for i in range(1, n + 1):
            nx = ''
            
            for j in range(1, n + 1):
                if xx[i][j - 1] != '?':
                    nx += xx[i][j - 1]
                elif i in sb[:n // 4] or j in sb[:n // 4]:
                    nx += 'S'
                else:
                    nx += 'F'
            
            print(nx)
            
        #State: `sa` remains unchanged, `sb` may have additional elements appended, which are the row indices where both `a[i]` and `b[i]` are 0, and the length of `sa` is still less than the length of `sb`. The values of `n` and `xx` remain unchanged. The loop prints a string `nx` for each row `i` from 1 to `n`, where `nx` is constructed by replacing '?' characters in `xx[i]` with 'S' if `i` or `j` is in the first quarter of `sb`, otherwise replacing '?' with 'F'.
    #State: *`sa` contains the row indices where there is at least one 'F' transition and no 'S' transitions, and `sb` contains the column indices where there is at least one 'S' transition and no 'F' transitions. The values of `n` and `xx` remain unchanged. If the length of `sa` is greater than or equal to the length of `sb`, the loop prints modified strings `nx` for each iteration of `i` from 1 to `n`, where `nx` is the same as the initial state, and `sa` may have additional indices `i` from 1 to `n` where both `a[i]` and `b[i]` are 0. If the length of `sa` is less than the length of `sb`, `sa` remains unchanged, `sb` may have additional elements appended, which are the row indices where both `a[i]` and `b[i]` are 0, and the loop prints a string `nx` for each row `i` from 1 to `n`, where `nx` is constructed by replacing '?' characters in `xx[i]` with 'S' if `i` or `j` is in the first quarter of `sb`, otherwise replacing '?' with 'F'.
#Overall this is what the function does:The function reads an integer `n` and a list of `n` strings, each of length `n`, representing a symmetric transition video plan. It then processes this plan to determine the counts of 'F' (funny) and 'S' (scary) transitions for each row and column. Based on these counts, it identifies rows that have only 'F' transitions and columns that have only 'S' transitions. If the number of rows with only 'F' transitions is greater than or equal to the number of columns with only 'S' transitions, it adds any undecided rows (rows with no transitions) to the list of rows with only 'F' transitions and prints a modified transition plan where '?' characters are replaced with 'F' for the first quarter of these rows and 'S' for the rest. If the number of rows with only 'F' transitions is less than the number of columns with only 'S' transitions, it adds any undecided rows to the list of columns with only 'S' transitions and prints a modified transition plan where '?' characters are replaced with 'S' for the first quarter of these columns and 'F' for the rest. The original input values `n` and the list of strings `xx` remain unchanged.

