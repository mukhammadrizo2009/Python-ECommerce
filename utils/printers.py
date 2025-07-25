from termcolor import colored


def print_status(text, status):
    status_map = {
        'error': 'red',
        'succes': 'green'
    }
    text = colored(text, status_map.get(status, 'red'))
    print(text)
    
class Print:   
    def print_menu(self):
        print(colored("===== Menu =====","blue"))
        print(colored("1.Register" , "yellow"))
        print(colored("2.Login" , "yellow"))
        print(colored("3.Exit" , "yellow"))
    
    def welcome(self):
        print(colored("Dasturga hush kelibsiz!" , "blue"))
        
    def bye(self):
        print(colored("Dasturimizdan foydalanganingiz uchun tashakkur!" , "cyan"))
        
    def welcome2(self):
        print(colored("Sizni ko'rganimizdan hursandmiz!" , "blue"))
        
    def order_print(self):
        print(colored("===== Order Menu =====","blue"))
        print(colored("1.Mahsulotlar ro'yhati." , "yellow"))
        print(colored("2.Buyurtma berish." , "yellow"))
        print(colored("3.Buyurtmalarni ko'rish." , "yellow"))
        print(colored("4.Exit" , "yellow"))
        
    def mahsulotlar(self):
        print(colored("Mahsulotlar ro'yhati!" , "light_green"))
        
        
    def buyurtma(self):
        print(colored("Buyurtma berishga xush kelibsiz!" , "light_green"))
        
    def buyurtmani_korish(self):
        print(colored("Buyurtmalaringiz ro'yhati!" , "light_green"))