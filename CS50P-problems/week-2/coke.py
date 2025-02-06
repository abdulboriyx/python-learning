def  main():
      price = 50 
      while(price>0):
            print(f'Amount due: {price}')
            given_coint = int(input('Insert coint: '))
            if (given_coint == 5 or given_coint == 10 or given_coint == 25):
                  price -= given_coint

            if (price<=0):
                  print(f'Change owed: {price}')
main()