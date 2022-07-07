song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
song = song.replace(' m', ' M');
print(song+ '\n')

quesntions = ["Are you?", "What day?", "Sound?"]
answer = ["sheep", "No", "Pop!"]
print(f"""{quesntions[0]}: {answer[1]}
{quesntions[1]}: {answer[2]}
{quesntions[2]}: {answer[0]}\n""")

print("""My cat likes %s,
My cat likes %s,
My cat fell on his %s
And now thinks he's a %s.\n""" % ("roast beef", "ham", "head", "clam"))

letter = """Dear {} {},

Thank you for your letter. We are sorry that our {}
{} in your {}. Please don't use it in a {}, especially
near any {}."""

salutation = "my"
name = "son"
product = "phone"
verbed = "boomed"
room = "house"
animals = "dog"

print(letter.format(salutation, name, product, verbed, room, room, animals))

winner_name = ["duck", "gourd", "spitz"]
for a in winner_name:
    print("%sy Mc%sface." % (a.capitalize(), a.capitalize()))
print()
for a in winner_name:
    print("{}y Mc{}face.".format(a.capitalize(), a.capitalize()))
print()
for a in winner_name:
    print(f"{a.capitalize()}y Mc{a.capitalize()}face.")