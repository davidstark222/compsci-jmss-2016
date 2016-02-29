# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically

word_list = []
quit = False

while not quit:
    word = input("")
    if word == "quit":
        quit = True
    else:
        word_list.append(word)
word_list.sort()
for word in word_list:
    print(word+" ",end='')