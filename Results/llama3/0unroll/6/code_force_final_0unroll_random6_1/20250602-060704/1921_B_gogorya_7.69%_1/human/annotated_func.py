#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains a single integer n (1 <= n <= 10^5). The second line contains a string s of n characters, where the i-th character is '1' if there is a cat in the i-th box and '0' otherwise. The third line contains a string f of n characters, where the i-th character is '1' if there should be a cat in the i-th box and '0' otherwise.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s1 = input()
        
        s2 = input()
        
        a1 = s1.count('1')
        
        a2 = s2.count('1')
        
        hd = a1 - a2
        
        res = abs(a1 - a2)
        
        for i in range(n):
            if hd > 0:
                hd -= 1
                continue
            if s1[i] == '1' and s2[i] == '0':
                res += 1
        
        print(res)
        
    #State: The number of cats in each box is equal to the desired number of cats in each box, and the total number of cats is equal to the desired total number of cats. The output is the minimum number of operations required to achieve this state.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: the number of boxes, the current state of cats in the boxes, and the desired state of cats in the boxes. It calculates the minimum number of operations required to make the current state match the desired state, considering two types of operations: moving a cat from one box to another and adding/removing a cat from a box. The function prints the minimum number of operations required for each test case.

