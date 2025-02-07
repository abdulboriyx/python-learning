# massachusetts plate

numbers = '012345678'
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    plate = ''
    for letter in s:
        if (s[0] not in numbers or s[1] not in numbers):
            if (2<=len(s)<=6):
                  plate += letter
            elif (s.isalpha()):
                  plate += letter
   
    for letter in range(len(s)):
        if s[letter].isnumeric():
            break
    for numb in range(letter, len(s)):
        if s[numb].isnumeric() == False:
            return False
        
    
    return plate
    




main()