#State of the program right berfore the function call: password is a string consisting of lowercase Latin letters and digits, with a length of 1 to 20 characters.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: Output State: `digits` is a list containing all the digit characters from the `password` string, and `letters` is a list containing all the lowercase Latin letter characters from the `password` string. The order of characters in both lists is the same as their order in the `password` string.
    digits.sort()
    letters.sort()
    for i in range(len(digits)):
        if i < len(digits) - 1 and digits[i] > digits[i + 1]:
            return False
        
        if i < len(letters) and digits[-1] > letters[i]:
            return False
        
    #State: The loop completes without returning `False`, and the `digits` and `letters` lists remain unchanged.
    sortedPassword = ''.join(digits + letters)
    if (sortedPassword == password) :
        return True
        #The program returns True.
    else :
        return False
        #The program returns False.
#Overall this is what the function does:The function `func_1` accepts a parameter `password`, which is a string consisting of lowercase Latin letters and digits with a length between 1 and 20 characters. It returns `True` if the `password` is already sorted in non-decreasing order (i.e., digits come first and are sorted, followed by letters which are also sorted). Otherwise, it returns `False`. The function does not modify the `password` string or any external state.

