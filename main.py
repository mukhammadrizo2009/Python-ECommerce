from models.user import User
from utils.printers import Print
import sys


while True:
    Print.print_menu(Print)
    choose = input("Amalni tanlang: ")
    
    if choose == "1":
        Print.welcome(Print)
        User.create_user()
    
    if choose == "2":
        Print.welcome2(Print)
        User.login_user()
    
    if choose == "3":
        Print.bye(Print)
        sys.exit()