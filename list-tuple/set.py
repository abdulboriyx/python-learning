alex = set(['Hip-Hop', 'Football', 'NBA', 'Streamers'])
mehrinoz = set(['Pop', 'Movies', 'Books', 'Ping-pong'])
jahonbaxsh = set(['Rock', 'Football', 'UFC', 'Tech'])
ali = set(['R&B', 'Philosophy', 'AI', 'Sci-fi', 'Robotics', 'Maths'])


# my_interests = set(['Soccer', 'Clothing', 'Reading', 'Music', 'Coding'])
my_interests = input('Enter your interests: ')
interest_set = set(my_interests.split(', '))


common_alex = interest_set & alex
common_mehrinoz = interest_set & mehrinoz
common_jahonbaxsh = interest_set & jahonbaxsh
common_ali = interest_set & ali

alex_list = list(common_alex)
mehrinoz_list = list(common_mehrinoz)
jahonbaxsh_list = list(common_jahonbaxsh)
ali_list = list(common_ali)


print('You have these common interests with Alex:', *alex_list if alex_list else ['None'])
print('You have these common interests with Mehrinoz:', *mehrinoz_list if mehrinoz_list else ['None'])
print('You have these common interests with Jahonbaxsh:', *jahonbaxsh_list if jahonbaxsh_list else ['None'])
print('You have these common interests with Ali:', *ali_list if ali_list else ['None'])