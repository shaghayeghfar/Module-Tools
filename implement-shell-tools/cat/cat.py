import argparse

def print_file(filename, mode):
    with open(filename, "r") as file:
        line_number = 1

        for line in file:
            if mode == "number_all":
                print(f"{line_number} {line}", end="")
                line_number += 1

            elif mode == "number_nonempty":
                if line.strip() == "":
                    print(line, end="")
                else:
                    print(f"{line_number} {line}", end="")
                    line_number += 1

            else:
                print(line, end="")


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-n", action="store_true", help="Number all lines")
group.add_argument("-b", action="store_true", help="Number non-empty lines")
parser.add_argument("filenames", nargs="+")

args = parser.parse_args()

if args.n:
    mode = "number_all"
elif args.b:
    mode = "number_nonempty"
else:
    mode = "none"

for filename in args.filenames:
    print_file(filename, mode)
