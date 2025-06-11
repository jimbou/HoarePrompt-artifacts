#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 100), followed by t test cases. Each test case consists of an integer n (1 ≤ n ≤ 16), a character representing the trump suit, and 2n distinct cards, each represented as a two-character string.
    input()
    trump = input()
    trumps = []
    answers = []
    suits = {'C': None, 'D': None, 'H': None, 'S': None}
    for card in input().split():
        rank, suit = card
        
        if suit == trump:
            trumps.append(rank)
        elif suits[suit] is not None:
            answers.append(' '.join([(x + suit) for x in sorted([suits[suit], rank])]))
            suits[suit] = None
        else:
            suits[suit] = rank
        
    #State: `stdin` is empty, `trump` is a character, `trumps` is a list containing the first character of each word in the original stdin that has a suit equal to `trump`, `answers` is a list containing strings which are the concatenation of the sorted values of `suits[suit]` and the first character of each word in the original stdin that has a suit not equal to `trump`, followed by the suit, `suits` is a dictionary with keys C, D, H, S and values None.
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: `stdin` is empty, `trump` is a character, `trumps` is an empty list, `answers` is a list containing strings which are the concatenation of the sorted values of `suits[suit]` and the first character of each word in the original stdin that has a suit not equal to `trump`, followed by the suit, and a new string that is the concatenation of `rank`, `suit`, a space, the last character that was in `trumps`, and `trump` for each suit in `suits` that has a non-None value, `suits` is a dictionary with keys C, D, H, S and all key-value pairs have non-None values.
    trumps = sorted(trumps, reverse=True)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: Output State: `stdin` is empty, `trump` is a character, `trumps` is an empty list, `answers` is a list containing strings which are the concatenation of the sorted values of `suits[suit]` and the first character of each word in the original stdin that has a suit not equal to `trump`, followed by the suit, and a new string that is the concatenation of `rank`, `suit`, a space, the last character that was in `trumps`, and `trump` for each suit in `suits` that has a non-None value, `suits` is a dictionary with keys C, D, H, S and all key-value pairs have non-None values, and all elements of the `trumps` list followed by the `trump` character are printed.
    #
    #In natural language, the output state after the loop executes all the iterations is that the `trumps` list is empty, and all elements of the original `trumps` list followed by the `trump` character have been printed. The other variables remain unchanged.
    for answer in answers:
        print(answer)
        
    #State: `stdin` is empty, `trump` is a character, `trumps` is an empty list, `answers` is an empty list, `suits` is a dictionary with keys C, D, H, S and all key-value pairs have non-None values, and all elements of the original `answers` list have been printed.

#Overall this is what the function does:This function reads input from stdin, processes the input to determine the trump suit and cards, and then prints out the sorted cards in a specific format. It first reads the number of test cases, then for each test case, it reads the number of cards, the trump suit, and the cards themselves. It then processes the cards to determine the sorted order and prints out the result. If there are any remaining trump cards, it prints them out in pairs. Finally, it prints out the sorted non-trump cards. The function does not return any value, but instead prints out the results directly.

