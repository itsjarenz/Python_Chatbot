def slice_name(input_name):
  name = input_name.split()[0]
  surname = input_name.split()[1]
  return name, surname
  
if __name__ == "__main__":
  print(slice_name("Joao Diogo")) 