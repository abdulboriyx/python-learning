import csv

players = []

with open("players.csv") as file:
      reader = csv.DictReader(file)
      # for line in file:
      for row in reader:
            # row = line.rstrip().split(",")
            # more efficient one:
            # player_name, club = line.rstrip().split(",")
            # player = {"player_name": player_name, "club": club}
            # players.append(player)
            players.append({"player_name": row['player_name'], "club": row["club"]})
            



for player in sorted(players, key=lambda player: player["player_name"]):
      print(f"{player['player_name']} played at {player['club']}")