import random

# minor = random.choice(["neuroscience", "philosophy"])

# rannumb = random.randint(1, 100)

rappers = ["Kendrick Lamar", "Eminem", "J Cole", "Andre 3000", "21 Savage", "Playboi Carti", "Nas"]
random.shuffle(rappers)
for rapper in rappers:
      print(rapper)