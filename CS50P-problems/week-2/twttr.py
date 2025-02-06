# twttr

def main():
      twttr = input('Input: ').lower()
      print(f'{get_twttr(twttr)}')
def get_twttr(twt):
      new_twt = ''
      vowel_list = ['a', 'o', 'u', 'e', 'i']

      for vowel in twt:
            if (vowel not in vowel_list):
                  new_twt += vowel
            
                  
      return new_twt
      
main()