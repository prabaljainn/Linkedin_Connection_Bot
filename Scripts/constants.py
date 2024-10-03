from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("USER_NAME")
commaseparated = "accenture"
password = os.getenv("PASS")

connection_mess = ''
# upto pages is just to let the script know for how many pages you want it to execute
upto_page = 1


# Just to add some colors in text
class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
