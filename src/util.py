def open_as_list(fileName):
  file = open(fileName, "r")
  content = file.read()
  list = content.split("\n")
  file.close()
  return list