import sys

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

def printConsole(message, color=WHITE):
    sys.stdout.write(message)

def set_color(color):
    return f"\033[1;3{color}m"

RESET_COLOR = "\033[0m"

def printConsole(message, color=WHITE):
    sys.stdout.write(set_color(color) + message + RESET_COLOR + "\n")
    sys.stdout.flush()