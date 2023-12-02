import re
from util import open_as_list

def main():
  color_max = {
    "red": "12",
    "green": "13",
    "blue": "14"
  }

  running_total = 0
  
  games = {}

  for idx, line in enumerate(open_as_list("./src/day2_input.txt")):
    games[idx] = line.split(":")[1].split(";")
    running_total += idx+1
  
  # part 1
  for key in games.keys():
    to_parse = re.sub(",", "", ''.join(games[key])).split(" ")
    for i in range(1, len(to_parse), 2):
      num_cubes = to_parse[i]
      cube_color = to_parse[i+1]

      if int(color_max[cube_color]) < int(num_cubes):
        running_total -= key+1
        break

  print("Part 1")
  print(running_total)
  print("\n")
  # part 2
  running_total = 0
  for key in games.keys():
    high_dict = {
      "red": "0",
      "green": "0",
      "blue": "0"
    }
    to_parse = re.sub(",", "", ''.join(games[key])).split(" ")

    for i in range(1, len(to_parse), 2):
      num_cubes = to_parse[i]
      cube_color = to_parse[i+1]
      if int(high_dict[cube_color]) < int(num_cubes):
        high_dict[cube_color] = num_cubes

    running_total += (int(high_dict["red"]) * int(high_dict["green"]) * int(high_dict["blue"]))

  print("Part 2")
  print(running_total)


if __name__ == "__main__":
  main()