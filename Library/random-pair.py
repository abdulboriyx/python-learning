import random

opponent_team = ["Prince", "Jay Z", "Kanye", "Taylor Swift", "Bruno Mars", "The Beatles", "Ed Sheeran", "the Weekend"]

user_team = []


for i in range(8):
      user_rapper = input(f'Enter your favorite artist {i + 1} ')
      user_team.append(user_rapper)



def main():

      battles = []
      all_winners = []
      user_winner = []
      opponent_winner = []
      
      for i in range(8):
            user_random = random.choice(user_team)
            user_team.remove(user_random)

            opponent_random = random.choice(opponent_team)
            opponent_team.remove(opponent_random)

            print(f"\n {user_random} vs {opponent_random}")
            
            battles.append([user_random, opponent_random])

      winner_choice = input("\n Do you want to get winners? (Yes/No) ")
      if (winner_choice == "Yes"):

            
                  # winner
            print("\n Pairs:")
            for battle in battles:
                  winner = random.choice(battle)
                  
                  all_winners.append(winner)
                  print(f"\n {battle[0]} vs {battle[1]} - Winner: {winner}")

            all_winners_str = ", ".join(all_winners)
            

            print(f"\n Winners are: {all_winners_str}") 

      else:
            return battles
      
      second_round_choice = input("\n Do you want to get winners? (Yes/No) ")
      if (second_round_choice == "Yes"):
                  next_round_winners = []

                  for i in range(4):
                        round_winner1 = random.choice(all_winners)
                        all_winners.remove(round_winner1)
                        

                        round_winner2 = random.choice(all_winners)
                        all_winners.remove(round_winner2)

                        
                        
                        next_winner = random.choice([round_winner1, round_winner2])
                        

                        print(f"\n {round_winner1} vs {round_winner2} - Winner: {next_winner}")
                        next_round_winners.append(next_winner)

                        next_winners_str = ", ".join(next_round_winners)
            

                  print(f"\n Winners are: {next_winners_str}") 

      third_round_choice = input("\n Do you want to continue? (Yes/No) ")
      if (third_round_choice) == 'Yes':
                  third_round_winners = []
                  for i in range(2):
                        round_winner3 = random.choice(next_round_winners)
                        next_round_winners.remove(round_winner3)
                        

                        round_winner4 = random.choice(next_round_winners)
                        next_round_winners.remove(round_winner4)

                        
                        
                        third_round_winner = random.choice([round_winner3, round_winner4])
                        

                        print(f"\n {round_winner3} vs {round_winner4} - Winner: {next_winner}")
                        third_round_winners.append(third_round_winner)

                        third_round_winners_str = ", ".join(third_round_winners)
            

                  print(f"\n Winners are: {third_round_winners_str}") 
      final_round_choice = input("\n Do you want to continue? (Yes/No) ")
      if (final_round_choice == 'Yes'):
                  final_winner = []
                  for i in range(1):
                        round_winner5 = random.choice(third_round_winners)
                        third_round_winners.remove(round_winner5)
                        

                        round_winner6 = random.choice(third_round_winners)
                        third_round_winners.remove(round_winner6)

                        
                        
                        final_round_winner = random.choice([round_winner5, round_winner6])
                        

                        print(f"\n {round_winner5} vs {round_winner6} - Winner: {final_round_winner}")
                        final_winner.append(final_round_winner)

                        final_round_winner_str = ", ".join(final_winner)
            

                  print(f"\n GOAT is: {final_round_winner_str}") 
                          
                        
#       second_round = input("Do you want to continue? (Yes/No) ")
#       if (second_round == 'Yes'):
#             for i in range(4):
#                   if user_winner:
#                         user_second_round = random.choice(user_winner)
#                         user_winner.remove(user_second_round)
#                   else:
#                         user_second_round = None
#                   if opponent_winner:      
#                         opponent_second_round = random.choice(opponent_winner)
#                         opponent_winner.remove(opponent_second_round)
#                   else: 
#                         opponent_second_round = None
#                   if user_second_round is None:
#                         print(f"{opponent_second_round} wins by default!")
#                   elif opponent_second_round is None:
#                         print(f"{user_second_round} wins by default!")
#                   else:
#                         print(f"{user_second_round} vs {opponent_second_round}")
      
#       # third round
#       third_round = input("Do you want to continue? (Yes/No)")
#       if (third_round == 'Yes'):
#             for i in range(2):
#                   if user_winner:
#                         user_third_round = random.choice(user_winner)
#                         user_winner.remove(user_third_round)
#                   else:
#                         user_third_round = None
#                   if opponent_winner:      
#                         opponent_third_round = random.choice(opponent_winner)
#                         opponent_winner.remove(opponent_third_round)
#                   else: 
#                         opponent_third_round = None
#                   if user_third_round is None:
#                         print(f"{opponent_third_round} wins by default!")
#                   elif opponent_third_round is None:
#                         print(f"{user_third_round} wins by default!")
#                   else:
#                         print(f"{user_third_round} vs {opponent_third_round}")
      
main()