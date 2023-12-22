f = open("my.ideas","a+")
import random

def add():
  
  idea = input("Idea > ")
  f = open("my.ideas", "a+")
  f.write(f"{idea}\n")
  f.close()
  

def show():
  
  f = open("my.ideas", "r")
  ideas = f.read().split("\n")
  f.close()
  ideas.remove("")
  idea = random.choice(ideas)
  print(idea)
  
  

while True:
  menu = input("1: Add idea\n2: Show random idea\n> ")
  if menu == "1":
    add()
  else:
    show()
