great_question = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').lower()

if (great_question == '42'):
      print('Yes')
elif (great_question == 'forty two'):
      print('Yes')
elif (great_question == 'forty-two'):
      print('Yes')
else:
      print('Nope')