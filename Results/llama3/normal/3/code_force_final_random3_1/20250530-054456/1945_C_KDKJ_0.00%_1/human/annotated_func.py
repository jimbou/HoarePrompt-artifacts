#State of the program right berfore the function call: stdin contains two inputs: first an integer n (n >= 3) and then a string a of length n, consisting only of 0 and 1.
    n = int(input())
    a = input()
    S = [[0, 0]]
    for s in a:
        x, y = S[-1]
        
        if s == '0':
            x += 1
        else:
            y += 1
        
        S.append([x, y])
        
    #State: n is an integer greater than or equal to 3, a is an empty string, S is a list containing n+1 lists, the first list contains two elements, both 0, the second list contains two elements, x and y, where if the first character of a is 0, then x is 1 and y is 0, if the first character of a is 1, then x is 0 and y is 1, the third list contains two elements, x and y, where if the second character of a is 0, then x is incremented by 1, otherwise y is incremented by 1, the fourth list contains two elements, x and y, where if the third character of a is 0, then x is incremented by 1, otherwise y is incremented by 1, and so on, the last list contains two elements, x and y, where x is the total number of 0's in the original string a and y is the total number of 1's in the original string a, and stdin is empty.
    ans = 0
    satisfy = 0
    for i in range(n):
        left = S[i][0]
        
        lsum = S[i][0] + S[i][1]
        
        right = S[-1][1] - S[i][1]
        
        rsum = n - lsum
        
        if left * 2 < lsum or right * 2 < rsum:
            continue
        elif abs(n / 2 - i) <= abs(n / 2 - ans):
            ans = i
        
    #State: n is an integer greater than or equal to 3, a is an empty string, S is a list containing n+1 lists, the first list contains two elements, both 0, the second list contains two elements, x and y, where if the first character of a is 0, then x is 1 and y is 0, if the first character of a is 1, then x is 0 and y is 1, the third list contains two elements, x and y, where if the second character of a is 0, then x is incremented by 1, otherwise y is incremented by 1, the fourth list contains two elements, x and y, where if the third character of a is 0, then x is incremented by 1, otherwise y is incremented by 1, and so on, the last list contains two elements, x and y, where x is the total number of 0's in the original string a and y is the total number of 1's in the original string a, satisfy is 0, stdin is empty, ans is the index of the list in S that is closest to the middle of S, left is the first element of the last list in S, lsum is the sum of the elements in the last list in S, right is 0, rsum is 0, i is n-1.
    print(ans)
    #This is printed: (n+1)//2 (where n is an integer greater than or equal to 3)

#Overall this is what the function does:This function reads an integer n and a string a of length n from standard input, where n is greater than or equal to 3 and a consists only of 0 and 1. It then calculates the cumulative sums of 0 and 1 in the string a and finds the index of the cumulative sum that is closest to the middle of the string. Finally, it prints the index of the cumulative sum that is closest to the middle of the string.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than or equal to 1).
    for _ in range(int(input())):
        func_1()
        
    #State: Output State: `_` is equal to the input integer minus 1, stdin contains one input: an integer that must be greater than or equal to 1, and the function `func_1()` has been executed a number of times equal to the input integer.
    #
    #In natural language, this means that after the loop finishes executing, the variable `_` will hold the value of the input integer minus 1, the input integer will still be present in stdin, and the function `func_1()` will have been executed as many times as the value of the input integer.

#Overall this is what the function does:Executes the function `func_1()` a specified number of times, equal to the input integer provided, and does not modify the input integer in stdin.

