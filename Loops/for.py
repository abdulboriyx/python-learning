# def main():
#       names = ["Stephen", "Alan", "Robert", "Isaac", "Albert"]
      # for i in range(len(names)):
      #       print(names[i])

      # for i in range(len(names)):
      #       print(send_message(names[i], "Avicenna"))

#       for name in names:
#             print(send_message(name, "Avicenna"))

# def send_message(receiver, sender):
#       return f"""
#      +~~~~~~~~~~~~~~~~~~~~~~~~~+
#       Hey {receiver},

#       We are going to play soccer against Stalin team. They want to playa again even if they have lost to us recently. Are you gonna join? Let me know

#       Love, 
#       {sender}

#       +~~~~~~~~~~~~~~~~~~~~~~~~~+
#       """
      

# main()



# students
artist_rec = input("Recommend artist for your friends ")
def main():
      
      students = ["Alan", "John", "Denzel", "Jack", "Leon"]

      # for student in students:
      print(send_message(students[0], "Avicenna"))

def send_message(receiver, sender):
      if artist_rec == "Kendrick Lamar":
            return f""" 
            -----------------------

            Hey {receiver}

            I highly recommend you check out these 10 amazing songs by Kendrick Lamar! His music is incredible and has such powerful messages. Here are some of my favorites:

            "HUMBLE", "Alright", "DNA", "King Kunta", "M.A.A.D City", "Bitch, Don't Kill My Vibe", "Swimming Pools (Drank)", "The Blacker the Berry", "Poetic Justice", "Money Trees"
            
            Let me know which one you like the most!

            Love,
            {sender}
             """
      elif artist_rec == "J Cole":
            return f""" 
            -----------------------

            Hey {receiver}

            I highly recommend you check out these 10 amazing songs by J Cole! His music is incredible and has such powerful messages. Here are some of my favorites:
            
            "Middle Child", "No Role Modelz", "G.O.M.D.", "Love Yourz", "Wet Dreamz", "MIDDLE CHILD", "4 Your Eyez Only", "Lights Please", "Dollar and a Dream", "The Climb Back"
            
            Let me know which one you like the most!

            Love,
            {sender}
             """
      elif artist_rec == "Drake":

            return f""" 
            -----------------------

            Hey {receiver}

            I highly recommend you check out these 10 amazing songs by Drake! His music is incredible and has such powerful messages. Here are some of my favorites:
            
            "God's Plan", "Hotline Bling", "Started From the Bottom", "In My Feelings", "One Dance", "Take Care", "Nonstop", "Marvins Room", "The Ride", "Controlla"
            
            Let me know which one you like the most!

            Love,
            {sender}
             """

main()