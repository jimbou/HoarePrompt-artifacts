#State of the program right berfore the function call: stdin contains two inputs: first an integer (between 1 and 10^4 inclusive) and then a list of integers (between 1 and 2 * 10^5 inclusive).
    t = int(input())
    numbers = []
    for _ in range(t):
        n = int(input())
        
        numbers.append(n)
        
    #State: t is an integer between 0 and 10^4 inclusive, numbers is a list containing t integers, _ is t-1, stdin is empty
    values = [(0) for _ in range(max(numbers) + 1)]
    sum_values = [(0) for _ in range(max(numbers) + 1)]
    total = 0
    for i in range(10):
        values[i] = i
        
        total += i
        
        sum_values[i] = total
        
    #State: t is an integer between 0 and 10^4 inclusive, numbers is a list containing t integers, values is a list containing max(numbers) + 1 elements where the first element is 0, the second element is 1, the third element is 2, the fourth element is 3, the fifth element is 4, the sixth element is 5, the seventh element is 6, the eighth element is 7, the ninth element is 8, and the tenth element is 9, sum_values is a list containing max(numbers) + 1 elements where the first element is 0, the second element is 1, the third element is 3, the fourth element is 6, the fifth element is 10, the sixth element is 15, the seventh element is 21, the eighth element is 28, the ninth element is 36, and the tenth element is 45, total is 45, _ is t-1, stdin is empty, i is 9
    for i in range(10, n + 1):
        word = str(i)
        
        last = int(word[len(word) - 1])
        
        remainder = int(word[:-1])
        
        values[i] = values[last] + values[remainder]
        
        sum_total = values[i] + sum_values[i - 1]
        
        sum_values[i] = sum_total
        
    #State: t is an integer between 0 and 10^4 inclusive, numbers is a list containing t integers, values is a list containing max(numbers) + 1 elements where the first element is 0, the second element is 1, the third element is 2, the fourth element is 3, the fifth element is 4, the sixth element is 5, the seventh element is 6, the eighth element is 7, the ninth element is 8, the tenth element is 9, the eleventh element is 45, the twelfth element is 54, the thirteenth element is 99, the fourteenth element is 207, the fifteenth element is 471, the sixteenth element is 1062, the seventeenth element is 2367, the eighteenth element is 5274, the nineteenth element is 11826, the twentieth element is 26572, the twenty-first element is 59319, the twenty-second element is 132860, the twenty-third element is 298299, the twenty-fourth element is 669696, the twenty-fifth element is 1509645, the twenty-sixth element is 3407406, the twenty-seventh element is 7698787, the twenty-eighth element is 17383860, the twenty-ninth element is 39295551, the thirtieth element is 88527810, the thirty-first element is 200623220, the thirty-second element is 453816816, the thirty-third element is 1028452595, the thirty-fourth element is 2333516414, the thirty-fifth element is 5277629115, the thirty-sixth element is 11947117710, the thirty-seventh element is 27089596815, the thirty-eighth element is 61552973430, the thirty-ninth element is 139483836345, the fortieth element is 315679405070, the forty-first element is 715825586815, the forty-second element is 1624593470170, the forty-third element is 3686614454475, the forty-fourth element is 8358912294470, the forty-fifth element is 18975696148175, sum_values is a list containing max(numbers) + 1 elements where the first element is 0, the second element is 1, the third element is 3, the fourth element is 6, the fifth element is 10, the sixth element is 15, the seventh element is 21, the eighth element is 28, the ninth element is 36, the tenth element is 45, the eleventh element is 90, the twelfth element is 135, the thirteenth element is 234, the fourteenth element is 441, the fifteenth element is 912, the sixteenth element is 1974, the seventeenth element is 4239, the eighteenth element is 9133, the nineteenth element is 19659, the twentieth element is 42491, the twenty-first element is 91852, the twenty-second element is 199213, the twenty-third element is 431512, the twenty-fourth element is 934625, the twenty-fifth element is 2028510, the twenty-sixth element is 4423026, the twenty-seventh element is 9656047, the twenty-eighth element is 21112194, the twenty-ninth element is 46312441, the thirtieth element is 101594851, the thirty-first element is 223692372, the thirty-second element is 494838223, the thirty-third element is 1095514468, the thirty-fourth element is 2417758949, the thirty-fifth element is 5331517908, the thirty-sixth element is 11817378167, the thirty-seventh element is 26214756334, the thirty-eighth element is 58224512701, the thirty-ninth element is 129469627816, the fortieth element is 287639255627, the forty-first element is 639827511444, the forty-second element is 1423671020871, the forty-third element is 3172372051742, the forty-fourth element is 7050744103487, the forty-fifth element is 15730481956924, total is 45, _ is t-1, stdin is empty, i is 45, n is greater than 44, word is "45", last is 5, remainder is 4, sum_total is 15730481956924.
    for n in numbers:
        print(sum_values[n])
        
    #State: `t` is an integer between 0 and 10^4 inclusive, `numbers` is a list containing `t` integers that must have at least `t` elements, `total` is 45, `_` is `t-1`, `stdin` is empty, `i` is 45, `n` is the last element in the list, `word` is "45", `last` is 5, `remainder` is 4, `sum_total` is 15730481956924, and the value of `sum_values` at index `n` which is the last element in the list is being printed

#Overall this is what the function does:This function reads an integer t and a list of t integers from standard input, calculates the sum of the digits of each integer in the list, and prints the sum of the digits of each integer. The function uses dynamic programming to calculate the sum of the digits of each integer, where the sum of the digits of an integer is calculated as the sum of the digits of its last digit and the sum of the digits of the remaining digits. The function prints the sum of the digits of each integer in the list.

