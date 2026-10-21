
import sys

arguments = sys.argv[1:]
count_lines = False
count_words = False
count_characters = False
filenames = []

for argument in arguments:
    if argument == "-l":
        count_lines = True
    elif argument == "-w":
        count_words = True
    elif argument == "-c":
        count_characters = True
    else:
        filenames.append(argument)

if not count_lines and not count_words and not count_characters:
    count_lines = True
    count_words = True
    count_characters = True

total_lines = 0
total_words = 0
total_characters = 0

for filename in filenames:
    with open(filename, "r") as file:
        content = file.read()

    lines = len(content.splitlines())
    words = len(content.split())
    characters = len(content)

    total_lines += lines
    total_words += words
    total_characters += characters

    answer = ""
    if count_lines:
        answer += str(lines) + " "
    if count_words:
        answer += str(words) + " "
    if count_characters:
        answer += str(characters) + " "

    print(answer + filename)

if len(filenames) > 1:
    total = ""
    if count_lines:
        total += str(total_lines) + " "
    if count_words:
        total += str(total_words) + " "
    if count_characters:
        total += str(total_characters) + " "

    print(total + "total")
