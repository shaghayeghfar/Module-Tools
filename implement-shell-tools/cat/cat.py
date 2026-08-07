import sys

# Check if the user used a flag
if len(sys.argv) > 1 and sys.argv[1] == "-n":

    # Start from the second argument because the first is "-n"
    for filename in sys.argv[2:]:

        with open(filename, "r") as file:

            line_number = 1

            for line in file:
                print(f"{line_number} {line}", end="")
                line_number += 1


elif len(sys.argv) > 1 and sys.argv[1] == "-b":

    # Start from the second argument because the first is "-b"
    for filename in sys.argv[2:]:

        with open(filename, "r") as file:

            line_number = 1

            for line in file:

                # Only number non-empty lines
                if line.strip() == "":
                    print(line, end="")
                else:
                    print(f"{line_number} {line}", end="")
                    line_number += 1


else:

    # No flag, just print every file
    for filename in sys.argv[1:]:

        with open(filename, "r") as file:
            print(file.read(), end="")