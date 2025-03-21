#State of the program right berfore the function call: expression is a string consisting of characters "+" and "-", and length is an integer representing the length of the string expression such that 1 <= length <= 5000.
def func_1(expression, length):
    count = 0
    balance = 0
    for char in expression:
        if char == '+':
            balance += 1
        elif char == '-':
            balance -= 1
        
        if balance < 0:
            count += 1
            balance = 0
        
    #State: Output State: `count` is the number of times `balance` became negative, `balance` is 0, `expression` is a string consisting of characters "+" and "-", and length is the integer representing the length of the string expression such that 1 <= length <= 5000.
    return count + (balance > 0)
    #The program returns the number of times `balance` became negative plus 1 if `balance` is greater than 0
#Overall this is what the function does:The function accepts a string `expression` consisting of characters "+" and "-" and an integer `length` representing the length of `expression`. It counts the number of times the balance (initially set to 0) goes negative while iterating through each character in `expression`. If the final balance is greater than 0, it adds 1 to the count. The function returns this final count.

