import os
from dotenv import load_dotenv

from src import consolePrint as cp
from src.constants import banner,options
from src.vision import Vision

from src.socialNetworks.instagramAnalyzer import InstagramAnalyzer

load_dotenv()

"""
  App Configuration
"""
VERSION = "0.1.0"
VISION_MODEL = os.getenv("VISION_MODEL")

instagramAnalyzer = InstagramAnalyzer()
print(instagramAnalyzer)

def evaluateCommand(command:str):
  command = command.lower()

  if command == "0":
    cp.printConsole("Goodbye....",cp.RED)
    exit()
  elif command == "1":
    cp.printConsole("Instagram profile Analyzer powered by Large Language Models\n",cp.GREEN)
    instagramAnalyzer.analyze()
  else:
    cp.printConsole("Command not found!",cp.RED)

def printBanner():
  cp.printConsole(banner,cp.GREEN)
  cp.printConsole("Version: "+VERSION+" developed by Cristian Perafan 🔥",cp.YELLOW)

def main():
  while True:
    cp.printConsole(options,cp.YELLOW)
    userInput = input(">:")
    cp.printConsole("\n",cp.GREEN)
    evaluateCommand(userInput)


    

if __name__ == "__main__":
  printBanner()
  main()
    