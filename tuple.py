import copy
words = ('A', 'B', 'C')
for num in words:
    print(num)
    print(type(words))

a = [1,2,[8,9]]
b = a.copy()
c = list(a)
d = a[:]

print(a,b,c,d)

a[2][1] = 10
print(a,b,c,d)

e = copy.deepcopy(a)
a[2][1] = 100
print(a,e)

Day = ["mon", "tuesday", "wednesday"]
Month = ["Jan", "Feb", "Mar"]

ans = list(zip(Day, Month))
print(ans[0], type(ans[0]))
print(type(zip(Month, Day)))

a = range(1, 11)
b = range(1, 11)

anss = [(row, col) for row in a if row % 2 == 0 for col in b if col % 2 == 1]
for ans in anss:
    print(ans)

# homwwork
years_list = [1999,2000,2001,2002,2003,2004]
print(years_list[3])
print(years_list[-1])

things = ["mozzarella", "cinderella", "salmonella"]
things[1].capitalize()
print(things)
things[0] = things[0].upper()
print(things)
del things[-1]
print(things)

surprise = ["Groucho", "Chico", "Harpo"]
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1] = surprise[-1].capitalize()
print(surprise[-1])

even = [num for num in range(10) if num % 2 == 0]
print(even)

start1 = ["fee", "fie", "foe"]
rhymes = [("flop", "get a mop"),
        ("fope", "turn the rope"),
        ("fa", "get your ma"),
        ("fudge", "call the judge"),
        ("fat", "pet the cat"),
        ("fog", "walk the dog"),
        ("fun", "say we're done"),
        ]
start2 = "Someone better"
start1_caps = " ".join([word.capitalize() + "!" for word in start1])
for first, second in rhymes:
    print(f"{start1_caps} {first.capitalize()}!")
    print(f"{start2} {second}.")