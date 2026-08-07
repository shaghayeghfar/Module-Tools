import sys


# Get everything the user typed after wc.py
arguments = sys.argv[1:]


# These are our options
count_lines = False
count_words = False
count_characters = False


# Store file names here
filenames = []


# Check every argument
for argument in arguments:

    if argument == "-l":
        count_lines = True

    elif argument == "-w":
        count_words = True

    elif argument == "-c":
        count_characters = True

    else:
        filenames.append(argument)



# If the user did not give any flag,
# show all counts like normal wc
if (not count_lines 
        and not count_words 
        and not count_characters):

    count_lines = True
    count_words = True
    count_characters = True



# Go through every file
for filename in filenames:

    # Open the file
    with open(filename, "r") as file:

        # Read the whole file
        content = file.read()


        # Count lines
        lines = len(content.splitlines())


        # Count words
        words = len(content.split())


        # Count characters
        characters = len(content)



        # Prepare the answer
        answer = ""


        if count_lines:
            answer += str(lines) + " "


        if count_words:
            answer += str(words) + " "


        if count_characters:
            answer += str(characters) + " "



        # Print the result
        print(answer + filename)