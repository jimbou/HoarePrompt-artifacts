#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 20) followed by three strings a, b, c, each consisting of n lowercase Latin letters.
    tests = int(input())
    for i in range(tests):
        slength = int(input())
        
        a = input()
        
        b = input()
        
        c = input()
        
        no = True
        
        if c == a or c == b:
            no = False
            print('NO')
        else:
            counter = 0
            for x in c:
                if x not in a[counter] and x not in b[counter]:
                    no = False
                    print('YES')
                    break
                counter += 1
        
        if no:
            print('NO')
        
    #State: tests is an integer between 1 and 1000, i is tests-1, stdin is empty, slength is an integer between 1 and 20, a is a string of lowercase Latin letters of length slength, b is a string of lowercase Latin letters of length slength, c is a string of lowercase Latin letters of length slength, x is the last character in the string c, counter is slength, and no is False.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and determines whether a given string c can be formed by taking characters from strings a and b without using any character more than once. It prints 'YES' if c can be formed, 'NO' otherwise. The function iterates through each test case, checking if c is equal to a or b, and if not, it checks if each character in c is present in the corresponding position in a or b. If any character in c cannot be formed, it prints 'YES' and moves on to the next test case. If all characters in c can be formed, it prints 'NO'.

