import argparse
import cowsay


parser = argparse.ArgumentParser(description="Make animals say things")

# Get supported animals from cowsay library
animals = list(cowsay.char_funcs.keys())

parser.add_argument(
    "message",
    nargs="+",
    help="The message to say."
)

parser.add_argument(
    "--animal",
    choices=animals,
    default="cow",
    help="The animal to be saying things."
)

args = parser.parse_args()

message = " ".join(args.message)

# Call the selected animal function from cowsay
animal = getattr(cowsay, args.animal)

animal(message)