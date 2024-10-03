from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("USER_NAME")
COMMASEPARATED = "tech lead"
PASSWORD = os.getenv("PASS")
CONNECTION_MESS = ""
UPTO_PAGE = 1


# Just to add some colors in text
class BCOLORS:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
