import re

from util import open_as_list

def main():
  running_total = 0

  # Part 1
  list = open_as_list("./src/day1_input.txt")
  for line in list:
    digits_only = re.sub("[^\d]", "", line)
    running_total += int(digits_only[0] + digits_only[-1])
  
  print(running_total)

  #Part 2
  num_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
  }
  running_total = 0
  for line in list:
    pattern = re.compile(r'(\d|one|two|three|four|five|six|seven|eight|nine)')
    digits_only = pattern.findall(line)

    for key in num_dict.keys():
      if digits_only[0] == key:
        digits_only[0] = num_dict[key]
      if digits_only[-1] == key:
        digits_only[-1] = num_dict[key]
    running_total += int(f"{digits_only[0]}{digits_only[-1]}")
    
  print(running_total)


if __name__ == "__main__":
  main()