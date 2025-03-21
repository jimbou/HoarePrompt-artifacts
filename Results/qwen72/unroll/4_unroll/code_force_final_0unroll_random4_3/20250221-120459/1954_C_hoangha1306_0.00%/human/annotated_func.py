#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, x and y are integers for each test case such that 1 <= x, y < 10^100, and x and y consist only of digits from 1 to 9.
def func():
    t = int(input())
    for q in range(t):
        a = input()
        
        b = input()
        
        kq1 = ''
        
        kq2 = ''
        
        vt = 0
        
        for i in range(len(a)):
            if a[i] == b[i]:
                kq1 = kq1 + a[i]
                kq2 = kq2 + a[i]
                continue
            else:
                x, y = min(int(a[i]), int(b[i])), max(int(a[i]), int(b[i]))
                if vt == 0:
                    vt = 1
                    if a[i] > b[i]:
                        kq1 = kq1 + str(x)
                        kq2 = kq2 + str(y)
                    else:
                        kq1 = kq1 + str(y)
                        kq2 = kq2 + str(x)
                else:
                    kq1 = kq1 + str(y)
                    kq2 = kq2 + str(x)
        
        print(kq1)
        
        print(kq2)
        
    #State: For each iteration of the loop, the variables `kq1` and `kq2` are updated based on the comparison of the digits of the input strings `a` and `b`. After all iterations, `kq1` and `kq2` will contain the strings formed by the rules specified in the loop, and these strings will be printed. The variables `t`, `x`, and `y` remain unchanged.
#Overall this is what the function does:The function `func` processes `t` test cases, where `t` is an integer between 1 and 1000. For each test case, it reads two strings `a` and `b` from input, each containing digits from 1 to 9. It then constructs two new strings `kq1` and `kq2` by comparing the corresponding digits of `a` and `b`. If the digits are the same, they are added to both `kq1` and `kq2`. If the digits are different, the smaller digit is added to `kq1` and the larger digit is added to `kq2` for the first difference encountered, and then the larger digit is added to `kq1` and the smaller digit is added to `kq2` for all subsequent differences. The function prints `kq1` and `kq2` for each test case. The function does not return any value.

