import re

def open_as_list():
  file = open("./day1/day1_input.txt", "r")
  content = file.read()
  list = content.split("\n")
  file.close()
  return list

def main():
  running_total = 0

  list = open_as_list()
  for line in list:
    digits_only = re.sub("[^\d]", "", line)
    running_total += int(digits_only[0] + digits_only[-1])
  
  print(running_total)

if __name__ == "__main__":
  main()