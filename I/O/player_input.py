import csv

player_name = input("What is player's name? ")
club = input("What is player's club? ")

with open("players.csv", "a") as file:
      write = csv.DictWriter(file, fieldnames="player_name, club")
      write.writerow({"player_name": player_name, "club": club})