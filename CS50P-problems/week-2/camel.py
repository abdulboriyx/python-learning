# # solution
def main():
      camelcase = input('Get your camel snaked: ')
      print((f'Snaked: {get_snaked(camelcase)}'))

def get_snaked(camel):
      snaked = ''
      for case in camel:
            if (case.isupper()):
                  snaked += '_'
                  snaked += case.lower()
            else:
                  snaked += case
      return snaked

main()


