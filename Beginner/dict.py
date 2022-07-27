e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
print('e2f', e2f)
print('walrus =>', e2f['walrus'])
f2e = {fra: en for en, fra in e2f.items()}
print('chien =>', f2e['chien'])
print(set(e2f.keys()))

life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'],
 'octopi': {}, 'emus': {}}, 'plants': {}, 'other': {}}
print('life:', life.keys())
print('animals:', life['animals'].keys())
print('animals: cats:', life['animals']['cats'])

squares = {i: i**2 for i in range(10)}
print('squares:', squares)

odd = {i for i in range(10) if i % 2 == 1}
print('odd', odd)

for thing in ('Got %s' % number for number in range(10)):
    print(thing)

a = ('optimist', 'pessimist', 'troll')
b = ('The glass is half full', 'The glass is half empty', 'How did you get the glass?')
c = dict(zip(a,b))
print(c)

titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plant']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
movie = dict(zip(titles, plots))
print(movie)