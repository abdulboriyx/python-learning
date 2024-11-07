def main(): 
      difficulty = input("Difficult or Casual? ")

      if not (difficulty == "Difficult" or difficulty == "Casual"):
            print("Enter a valid difficulty")
            return


      players = input("Multiplayer or Single-player? ")
      if not (players == "Multiplayer" or players == "Single-Player"):
            print("Enter a valid number of players")
            return

      # Conditionals
      # if difficulty == "Difficult":
      #       if players == "Multiplayer":
      #             recommend("Poker")
      #       elif players == "Single-player":
      #             recommend("Klondike")
      #       else:
      #             print("Enter a valid number of players")
      # elif difficulty == "Casual":
      #       if players == "Multiplayer":
      #             recommend("Hearts")
      #       elif players == "Single-Player": 
      #             recommend("Clock")
      #       else:
      #             print("Enter a valid number of players")
      # else: 
      #       print("Enter a valid difficulty")



      # Boolean

     
      if difficulty == "Difficult" and players == "Multiplayer":
            recommend("Poker")
      elif difficulty == "Difficult" and players == "Single-Player":
            recommend("Klondike")
      elif difficulty == "Casual" and players == "Multiplayer":
            recommend("Hearts")
      elif difficulty == "Casual" and players == "Single-Player":
            recommend("Clock")

def recommend(game):
      print("You might like", game)

main()