# sort_package.py

import argparse

def sort(width, height, length, mass):
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20

    return "REJECTED" if is_bulky and is_heavy else (
           "SPECIAL"  if is_bulky or is_heavy  else "STANDARD")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Classify a package based on size and weight.")
    parser.add_argument("width", type=int)
    parser.add_argument("height", type=int)
    parser.add_argument("length", type=int)
    parser.add_argument("mass", type=int)
    args = parser.parse_args()

    result = sort(args.width, args.height, args.length, args.mass)
    print(result)

