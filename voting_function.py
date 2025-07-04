def voting():
  for i in range(1,6):
    name=input("Enter name: ")
    age=int(input("Enter age: "))
    if age>=18:
      print("you can vote ")
    else:
      print("you can not vote") 

voting()

print("program end ")

