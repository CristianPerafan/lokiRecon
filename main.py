from src import consolePrint as cp
from src.ascii import banner


VERSION = "0.1.0"
DESCRIPTION = "A personal project focused on integrating Large Language Models (LLMs) with open-source intelligence (OSINT) techniques for reconnaissance."

def main():
    cp.printConsole(banner,cp.GREEN)
    cp.printConsole("Version: "+VERSION+" developed by Cristian Perafan 🔥",cp.YELLOW)

if __name__ == "__main__":
    main()