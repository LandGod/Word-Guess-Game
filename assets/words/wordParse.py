import re

old_list = open('wordlist.txt', 'r')
new_list = open('parsedWordList.txt', 'w')


pattern = re.compile(r"[a-z]{4,}\s")
new_list.write('[')
timer = 15
for line in old_list:
    theWord = pattern.search(line)
    if (not theWord):
        print('Nope')
        print("Continuing")
        continue
    new_list.write("\"" + theWord.group(0).strip() + "\", ")
    timer = timer - 1
    if timer < 1:
        new_list.write("\n")
        timer = 15


new_list.write(']')
old_list.close()
new_list.close()
