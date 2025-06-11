#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100), followed by t test cases. Each test case consists of an integer n (1 <= n <= 16), a character representing the trump suit (one of "CDHS"), and a space-separated list of 2n cards, where each card is a two-character string (the first character is the rank of the card, one of "23456789", and the second character is the suit of the card, one of "CDHS"). All cards are different.
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
        
    #State: trumps is a list containing the ranks of all cards with the trump suit, answers is a list containing strings, each string is the concatenation of the suit of a card and the rank of the card, or the value of suits[suit] and the rank of the card, whichever is smaller, followed by the suit of the card and the rank of the card, or the value of suits[suit] and the rank of the card, whichever is larger, suits is a dictionary with keys 'C', 'D', 'H', 'S' and values None.
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: trumps is an empty list, answers is a list containing strings, each string is the concatenation of the suit of a card and the rank of the card, or the value of suits[suit] and the rank of the card, whichever is smaller, followed by the suit of the card and the rank of the card, or the value of suits[suit] and the rank of the card, whichever is larger, with four additional strings that are the concatenation of the current rank and suit, followed by the last rank that was in trumps and the first key in the suits dictionary, suits is a dictionary with keys 'C', 'D', 'H', 'S' and values that must have at least 4 key-value pairs.
    trumps = sorted(trumps, reverse=True)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: trumps is an empty list, answers is a list containing strings, each string is the concatenation of the suit of a card and the rank of the card, or the value of suits[suit] and the rank of the card, whichever is smaller, followed by the suit of the card and the rank of the card, or the value of suits[suit] and the rank of the card, whichever is larger, with four additional strings that are the concatenation of the current rank and suit, followed by the last rank that was in trumps and the first key in the suits dictionary, suits is a dictionary with keys 'C', 'D', 'H', 'S' and values that must have at least 4 key-value pairs.
    for answer in answers:
        print(answer)
        
    #State: trumps is an empty list, answers is an empty list, answer is the last answer in the list, suits is a dictionary with keys 'C', 'D', 'H', 'S' and values that must have at least 4 key-value pairs, and the last answer in the list answers is being printed

#Overall this is what the function does:This function processes a series of card game test cases from standard input, where each test case consists of a trump suit and a list of cards. It then prints out the cards in a specific order, with the trump suit cards being printed first in descending order, followed by the non-trump suit cards in a specific pairing order. If there are not enough trump suit cards to pair with the non-trump suit cards, it prints 'IMPOSSIBLE' and exits. The function does not return any value, but instead prints the results directly to the console.

