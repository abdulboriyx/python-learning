import csv

# rappers = []

# for _ in range(3):
#       rapper = input('Enter your fav rapper: ')
#       rappers.append(rapper)

# for rapper in sorted(rappers):
#       print(f'hello, {rapper}')


# with

# name = input('What is your name, bish? ')
# with open('I/O/name-list.txt', 'a') as file:
#       file.write(f'{name}\n')


# read file

# with open('I/O/name-list.txt', 'r') as file:
#       lines = file.readlines()

# for line in lines:
#       print('hello,', line.rstrip())

# csv
# with open('I/O/name-list.csv', 'r') as file:
#       for line in file:
#             rapper, city = line.rstrip().split(',')
#             print(f'{rapper} is from {city}')

# movie
# movies = []

# with open('I/O/name-list.csv') as file:
#       for line in file:
#             movie_name, movie_director = line.rstrip().split(',')
#             movie = {}
#             movie["name"] = movie_name
#             movie['director'] = movie_director
#             movies.append(movie)


# for movie in movies:
#       print(f'{movie['name']} is directed by {movie['director']}')


# podcast
# podcasts = []

# with open('I/O/podcast-list.csv') as file:
#       for line in file:
#             podcast_name, podcast_holder = line.rstrip().split(',')

#             podcast = {}
#             podcast = {'name': podcast_name, 'holder': podcast_holder}
#             podcasts.append(podcast)

# for podcast in podcasts:
#       print(f'{podcast['name']} is held by {podcast['holder']}')


# company

# companies = []
# with open('I/O/companu-list.csv') as file:
#       for line in file:
#             company_name, company_ceo = line.rstrip().split(',')

#             company = {}
#             company = {'name': company_name, 'ceo': company_ceo}
#             companies.append(company)

# def get_company(company):
#       return company['name']

# for company in sorted(companies, key=get_company):
#       print(f'{company['ceo']} is CEO of {company['name']}')






# podcasts = []

# with open('I/O/podcast-list.csv') as file:
#       for line in file:
#             name, host = line.rstrip().split(',')
#             podcasts.append({'name': name, 'host': host})


# for podcast in sorted(podcasts, key=lambda podcast: podcast['name']):
#       print(f'{podcast['name']}\'s host is {podcast['host']}')






# founders
founders = []

with open('I/O/csv-list.csv') as file:
      reader = csv.DictReader(file)
      for row in reader:
            founders.append({'company': row['company'], 'founder': row['founder'], 'year': row['year']})
for founder in sorted(founders, key=lambda founder: founder['founder']):
      # print(f'{founder['company']} was founded by {founder['founder']} in {founder['year']}')
      print(founder)