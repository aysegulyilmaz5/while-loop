i = 1

studentnumber = int(input("Please enter student number:"))
print(studentnumber)

while i <studentnumber:

  midterm1 = float(input("Please enter midterm1 grade:"))
  print(midterm1)

  midterm2 = float(input("Please enter midterm2 grade:"))
  print(midterm2)

  final = float(input("Please enter final grade:"))
  print(final)

  avg = midterm1*0.3+midterm2*0.3+final*0.4
  print("Average:")
  print(avg)

  if avg>85 and avg <100 :
    print("Very good")

  elif avg > 60 and avg < 85 :
    print("Good")
  
  elif avg > 40 and avg < 60 :
    print("Middle")
  
  else:
    print("Very Bad") 


  i = i + 1


