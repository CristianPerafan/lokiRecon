import os
from dotenv import load_dotenv

load_dotenv()

def getVisionModel():
  return os.getenv("VISION_MODEL")

def getInstagramUsername():
    try:
        return os.getenv("INSTAGRAM_USERNAME")
    except Exception as e:
        print("Error getting Instagram Username")
        return None
    
def getInstagramPassword():
    try:
        return os.getenv("INSTAGRAM_PASSWORD")
    except Exception as e:
        print("Error getting Instagram Password")
        return None