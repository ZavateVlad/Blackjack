
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
another_card = True

user = random.sample(cards, 2)
dealer = random.sample(cards, 1)

def add_card(player):
  player.append(random.choice(cards))
  return player

def show_cards(show):
  print(f"  Your cards: {user}, current score: {sum(user)}")
  if show == False:
    print(f"  Dealer's first card: {dealer[0]}")
  if show == True:
    print(f"Dealer's final hand: {dealer}, final score: {sum(dealer)}")


def compare(player1, player2):
  if 1 in player1 or 1 in player2:
    if sum(player1) < 21:
      player1.remove(11)
      player1.append(1)
    if sum(player2) < 21:
      player2.remove(1)
      player2.append(11)
    
  if sum(player1) <= 21 and sum(player2) <= 21:
    if sum(player1) < sum(player2):
      print('You lose')
    elif sum(player1) == sum(player2):
      print('Tie')
    elif sum(player1) > sum(player2):
      print('You win')

  if sum(player1) > 21 or sum(player2) > 21:
    if sum(player1) < sum(player2):
      print('You win')
    elif sum(player1) == sum(player2):
      print('Tie')
    elif sum(player1) > sum(player2):
      print('You lose')


def game():
  another_card = True
  while another_card:
    show = False
    show_cards(show)
    user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_choice == 'y':
      add_card(user)
      if sum(user) > 21:
        while sum(dealer) < 17:
          add_card(dealer)
        show = True
        show_cards(show)
        compare(user, dealer)
        another_card = False
    elif user_choice == 'n':
      while sum(dealer) < 17:
        add_card(dealer)
        show = True
      show_cards(show)
      compare(user, dealer)
      another_card = False

game()

  


  


  
  

       
   

  

  
   

