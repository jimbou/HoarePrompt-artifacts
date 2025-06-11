#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case consists of three lines: the first line contains an integer n (1 <= n <= 16), the second line contains a single character (one of "CDHS"), and the third line contains a space-separated list of 2n two-character strings, where each string represents a card with a rank (one of "23456789") and a suit (one of "CDHS"). All cards are different.
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
        
    #State: Output State: The loop has processed all the cards in the input, and the state of the variables has been updated accordingly. The 'trumps' list contains all the ranks of the cards that have the same suit as the 'trump' character. The 'answers' list contains strings representing the sorted ranks of the cards for each suit, excluding the trump suit. The 'suits' dictionary has been updated to reflect the highest rank of each suit that has been seen so far, or None if no cards of that suit have been seen.
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: Output State: The loop has processed all the cards in the input, and the state of the variables has been updated accordingly. The 'trumps' list is empty. The 'answers' list contains strings representing the sorted ranks of the cards for each suit, excluding the trump suit. The 'suits' dictionary has been updated to reflect the highest rank of each suit that has been seen so far, or None if no cards of that suit have been seen.
    trumps = sorted(trumps)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: The 'trumps' list is empty, and the 'answers' list and 'suits' dictionary remain unchanged.
    for answer in answers:
        print(answer)
        
    #State: Output State: The 'trumps' list is empty, the 'answers' list remains unchanged, and the 'suits' dictionary remains unchanged.

#Overall this is what the function does:The function processes a series of card game test cases from standard input, where each test case consists of a set of cards with ranks and suits. It identifies the trump suit and separates the cards into trump cards and non-trump cards. For each non-trump suit, it finds the highest rank and pairs it with a trump card, if available. If no trump cards are available, it prints 'IMPOSSIBLE' and exits. Otherwise, it prints the paired cards in a sorted order, followed by any remaining trump cards in pairs. The function returns no value but prints the results of the card game processing to the standard output.

