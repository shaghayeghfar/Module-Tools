import sys
import os


# Get arguments from the command line
arguments = sys.argv[1:]


# Check if -1 flag exists
show_one_per_line = False

if "-1" in arguments:
    show_one_per_line = True
    arguments.remove("-1")


# Check if -a flag exists
show_all_files = False

if "-a" in arguments:
    show_all_files = True
    arguments.remove("-a")


# If no path is given, use current directory
if len(arguments) == 0:
    path = "."
else:
    path = arguments[0]


# Check if the path exists
if not os.path.exists(path):
    print(f"ls: cannot access '{path}': No such file or directory")
    sys.exit()


# If the path is a file, just print the file name
if os.path.isfile(path):
    print(path)


# If the path is a folder, list its contents
else:

    files = os.listdir(path)


    # Remove hidden files unless -a was used
    if not show_all_files:
        files = [
            file for file in files
            if not file.startswith(".")
        ]


    # Print one file per line
    if show_one_per_line:
        for file in files:
            print(file)


    # Normal ls behaviour
    else:
        print("  ".join(files))