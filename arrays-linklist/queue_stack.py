from collections import deque

# heroes_list = deque(['Sergei', 'Larry', 'Sam'])
# heroes_list.append('Demis')

# heroes_list.pop()
# print(heroes_list)

# first_million_queue
firsthunlion_queue = deque()

firsthunlion_queue.append('Steve Jobs')
firsthunlion_queue.append('Bill Gates')
firsthunlion_queue.append('Larry Ellison')
firsthunlion_queue.append('Jeff Bezos')
print(firsthunlion_queue)

# todo tasks

todo_list = deque()

todo_list.append('Read one chapter of Biology for Dummies')
todo_list.append('Learn 20 new Korean words')
todo_list.append('Write something new for MindMatters')
todo_list.append('Code')

print(todo_list)


todo_list.popleft()
todo_list.popleft()
print(todo_list)


# instagram_post
instagram_search = deque()
instagram_search.appendleft('instagram.com')
instagram_search.appendleft('https://www.instagram.com/gigihadid/')
instagram_search.appendleft('https://www.instagram.com/p/DELWFHTytfc/?img_index=2')
print(instagram_search)

instagram_search.popleft()
print(instagram_search)

instagram_search.popleft()
print(instagram_search)

instagram_search.popleft()
print(instagram_search)


