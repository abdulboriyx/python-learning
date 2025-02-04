# faces 
def main():
      face = convert()
      print(face)

def convert():
      x = input('Enter emoji: ').replace(":)", "🙂")
      x = x.replace(":(", "🙁")
      return x
main()