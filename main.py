#Write your code below this row 👇

for fizz in range (1,101):
  if fizz % 3 == 0:
    print("Fizz")
  if fizz % 5 == 0:
    print ("Buzz")
  if fizz % 3 == 0 and fizz % 5 == 0:
    print ("FizzBuzz")
  print(fizz)
