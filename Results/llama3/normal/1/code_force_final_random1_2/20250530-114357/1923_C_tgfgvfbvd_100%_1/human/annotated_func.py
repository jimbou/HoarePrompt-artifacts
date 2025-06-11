#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then two space-separated integers, then a space-separated list of integers, and then multiple space-separated pairs of integers.
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = [0]
        
        c = [0]
        
        i, j = 0, 0
        
        for x in l:
            if x == 1:
                j += 1
            i += x
            p.append(i)
            c.append(j)
        
        for _ in range(m):
            a, b = map(int, input().split())
            i = c[b] - c[a - 1]
            s = p[b] - p[a - 1]
            if b - a + 1 > 1 and s - (b - a + 1) >= i:
                print('YES')
            else:
                print('NO')
        
    #State: n is an integer, m is 0, l is a list of integers, p is a list containing len(l) + len(l) elements: 0 and the value of i plus the sum of all integers in the list l, c is a list containing len(l) + len(l) elements: 0 and the value of j, i is equal to c[b] - c[a - 1], a is an integer, b is an integer, s is equal to p[b] - p[a - 1], j is equal to its original value plus the number of 1's in the list l, x is the last integer in the list l, _ is 0, stdin contains no input. If b - a + 1 > 1 and s - (b - a + 1) >= i, then 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function processes multiple test cases from standard input. Each test case consists of an integer n, followed by two space-separated integers, a space-separated list of integers, and multiple space-separated pairs of integers. The function calculates the cumulative sum and count of 1's in the list of integers, then for each pair of integers, it checks if the sum of the corresponding subarray minus its length is greater than or equal to the count of 1's in that subarray. If the condition is met and the subarray has more than one element, it prints 'YES', otherwise it prints 'NO'.

