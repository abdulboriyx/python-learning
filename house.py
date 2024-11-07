# nameX = input("What is your name? ")

# if name == "Donald":
#       print("Republican")
# elif name == "Musk":
#       print("Republican")
# elif name == "JD":
#       print("Republican")
# elif name == "Kamala":
#       print("Democrat")
# elif name == "Tim":
#       print("Democrat") 
# else: 
#       print("Who are you?")     

# match nameX:
#       case "Kendrick" | "Snoop" | "Tupac" | "Tyler":
#             print("West Coast")
#       case "Nas" | "Jay" | "Rakim":
#             print("East Coast")
#       case _:
#             print("Who?")

library = input("What is the name of the book? ")

match library:
      case "Steve Jobs" | "Elon Musk" | "Benjamin Franklin" | "Phil Knight":
            print("Biography Section")
      case "Zero to One" | "The Lean Startup" | "The Hard Thing" | "Who":
            print("Startup Section")
      case "I, Robot" | "Foundations" | "Hitchhiker's Guide":
            print("Sci-Fi Section")
      case _:
            print("Hand it to the Librarians, please")