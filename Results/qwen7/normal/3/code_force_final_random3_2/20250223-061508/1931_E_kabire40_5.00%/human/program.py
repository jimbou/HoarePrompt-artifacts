for y in range(int(input())):
    rev_val = []
    rev_res = ''
    list_len, max_power = input().split()
    operational_list = input().split()
    
    for x in operational_list:
        x_rev = int(x[::-1])
        if len(str(x_rev)) == len(x):
            rev_res = rev_res + x
        else:
            rev_val.append(x[::-1])
            
    rev_val.sort()
    
    
    # print(operational_list)
    # print(rev_res,'/',rev_val)
    
    for x in range(len(rev_val)):
        if (x % 2) == 0:
            # print('X:',rev_val[x])
            val_in = int(rev_val[x])
            # print('X:',val_in)
            rev_res += str(val_in)
        else:
            val_in = rev_val[x]
            rev_res += val_in[::-1]
        # print(rev_res)
    
    
    if 10**int(max_power) < int(rev_res):
        print('Sasha')
    else:
        print('Anna')