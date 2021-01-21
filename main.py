"""
Chatbot
Author: Cara Tiller 
Period/Core: 5 

"""

import os
import importlib.util

import random

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)

def main():
  """This function contains all code for the chatbot."""
  print("Hello!")
  
  n=str(input("What is your first name? "))
  w=str(input("What is your last name? "))
  print("Nice to meet you "+ n +" "+ w + "!" )
  c = str(input("What country do you live in? "))
  if (c=="America" or c=="america"): 
      print("I live there too! ")
  else:
      print("I have never been there . ")

  x=str(input("Is it nice where you live ?"))
  if (x=="yes" or x=="Yes"):
      print("Thats good to hear!")
  elif(x=="no" or x=="No"):
      print("Awh I'm sorry.")


  m=str(input("If you could live anywhere else where would you live? "))
  u=random.randint(1,3)

  if u== 3: 
    print("Thats an intresting place! ")

  elif u== 2:
    print("Thats such a nice place!")

  elif u== 3:
    print("I hope that works out for you! ")




if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()


