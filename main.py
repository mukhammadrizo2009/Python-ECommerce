from models.user import User
from models.order import Order
from utils.printers import Print
import sys


while True:
    Print.print_menu(Print)
    choose = input("Amalni tanlang: ")
    
    if choose == "1":
        Print.welcome(Print)
        User.create_user()
    
    if choose == "2":
        while True:
            Print.welcome2(Print)
            if User.login_user():
                break
            
        while True:       
            Print.order_print(Print)
            chooses = input("Amalni tanlang: ")
            if chooses == "1":
                Print.mahsulotlar(Print)
                break
        
        while True:                
            if chooses == "2":
                Print.buyurtma(Print)
                break
        
        while True:        
            if chooses == "3":
                Print.buyurtmani_korish(Print)
                break
            
        while True:   
            if chooses == "4":
                Print.bye(Print)
                sys.exit()
                break
                
    if choose == "3":
        Print.bye(Print)
        sys.exit()