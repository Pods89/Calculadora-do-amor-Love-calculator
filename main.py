# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

nome_minusculo1 = (name1.lower() + name2.lower())
t = nome_minusculo1.count("t")
r = nome_minusculo1.count("r")
u = nome_minusculo1.count("u")
e = nome_minusculo1.count("e")
true_contagem = (t + r + u + e)
l = nome_minusculo1.count("l")
o = nome_minusculo1.count("o")
v = nome_minusculo1.count("v")
e = nome_minusculo1.count("e")
love_contagem = (l + o + v + e)
score = (str(true_contagem) + str(love_contagem))
score1 = int(score)

if score1 <= 10 or score1 >= 90:
  print(f"Your score is {score1}, you go together like coke and mentos.")
elif score1 >= 40 and score1 <= 50:
  print(f"Your score is {score1}, you are alright together.")
else: 
  print(f"Your score is {score1}.")
