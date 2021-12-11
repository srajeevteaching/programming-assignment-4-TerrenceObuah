import random
dealer_cards[]
player_cards[]
while len(dealer_cards)!=2:
    dealer_cards.append(random.randint(1,11))
    if len(dealer_cards)==2:
        print("dealer has X and, dealer_cards[1]) ")

while len(player_cards)!=2:
    player_cards.append(random.randint(1,11))
    if len(player_cards)==2:
        print("You have , player_cards ")
    if sum(dealer_cards) == 21:
        print("dealer has 21 and won")
    elif sum(dealer_cards)>21:
        print("dealer has busted")

while sum(player_cards)<21:
    action_taken = str(input( "Do you want to hit or stay?" ))
    if action_taken == "hit":
        player_cards.append(random.randint(1,11))
        print("You now have a total of", + str(sum(player_cards)) + "with", dealer_cards)
else:
print("The dealer has a total of,"+ str(sum(dealer_cards))+ "with" ,dealer_cards)
print("You have a total of" +str(sum(player_cards)) + "with", dealer_cards)
if sum(dealer_cards)> sum(player_cards):
        print("dealer wins")
    else:
            print("You win")

    if sum(player_cards)>21:
 print("You've busted. You lost")
elif:
    sum(player_cards) == 21:
    print("You have Blackjack! You won!")


















