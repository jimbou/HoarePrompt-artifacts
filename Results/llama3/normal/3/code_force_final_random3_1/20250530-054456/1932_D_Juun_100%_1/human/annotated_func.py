#State of the program right berfore the function call: stdin contains one or more test cases. Each test case contains three inputs: first an integer n (1 <= n <= 16), then a character (one of "CDHS"), and then a space-separated list of 2n two-character strings, each string consisting of a character (one of "23456789") and a character (one of "CDHS"). All 2n strings are different.
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
        
    #State: trumps is a list containing all the ranks of the cards in the input that have the suit equal to trump, answers is a list containing all the pairs of cards in the input that have the same suit and are not trumps, suits is a dictionary with keys 'C', 'D', 'H', 'S' and all values are None.
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: trumps is an empty list, answers is a list containing all the pairs of cards in the input that have the same suit and are not trumps, suits is a dictionary with keys 'C', 'D', 'H', 'S' and all values are None.
    trumps = sorted(trumps, reverse=True)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: `trumps` is an empty list, `answers` is a list containing all the pairs of cards in the input that have the same suit and are not trumps, `suits` is a dictionary with keys 'C', 'D', 'H', 'S' and all values are None, and all pairs of cards in the input that have the same suit and are trumps are printed, each pair followed by the suit of the pair.
    for answer in answers:
        print(answer)
        
    #State: `trumps` is an empty list, `answers` is an empty list, `answer` is the last pair of cards in the list, `suits` is a dictionary with keys 'C', 'D', 'H', 'S' and all values are None, and all pairs of cards in the input that have the same suit and are not trumps have been printed.

#Overall this is what the function does:This function processes a set of card inputs, pairing cards of the same suit and printing them out. It first separates the input cards into trumps and non-trumps based on a given trump suit. Then, it pairs the non-trump cards of the same suit and prints them out. If there are any trumps, it pairs them up and prints them out as well. If there are not enough trumps to pair with the non-trump cards, it prints 'IMPOSSIBLE' and exits. The function does not return any value, but instead prints out the paired cards directly.

