from termcolor import colored
import json
from datetime import datetime
from uuid import uuid4
from utils import (
    make_password, is_valid_username, print_status,
    is_valid_password,
)
from getpass import getpass

class User:
    
    def __init__(self, id, username, password, phone, first_name, last_name, age, gender):
        self.id = id
        self.username = username
        self.password = password
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.joined_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'phone': self.phone,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'gender': self.gender,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['id'],
            data['username'],
            data['password'],
            data['phone'],
            data['first_name'],
            data['last_name'],
            data['age'],
            data['gender'],
        )
    
    @classmethod
    def load_users(cls):
        with open('database/users.json') as jsonfile:
            try:
                data = json.load(jsonfile)
            except:
                data = []

        users = [User.from_dict(item) for item in data]

        return users
    
    @classmethod
    def save_users(cls, users):
        with open('database/users.json', 'w') as jsonfile:
            data = [user.to_dict() for user in users]
            json.dump(data, jsonfile, indent=2)

    @classmethod
    def create_user(cls):
        while True:
            username = input("Username: ")
            
            if not username:
                print(colored("Username bo'sh bo'lishi mumkin emas!" , "red"))
                
            elif len(username) < 4 or len(username) > 20:
                print(colored("Username 4 dan 20 gacha belgidan iborat bo'lishi kerak!" , "red"))
                
            elif not username.isalnum():
                print(colored("Usernameda harf va raqam bo'lish kerak!" , "red"))
                
            else:
                print(colored("Username qabul qilindi!" , "green"))
                break
            
        while True:
            password = getpass("Password: ")
            
            if len(password) < 8 or len(password) > 12:
                print(colored("Parol 8 dan 12 gacha belgidan iborat bo'lish kerak!" , "red"))
                
            else:
                print(colored("Parol qabul qilindi!" , "green"))
                break
            
        while True:
            confirm_password = getpass("Confirm Password: ")
            
            if confirm_password != password:
                print(colored("Parollar tasdiqlanmad!" , "red"))
                
            else:
                print(colored("Parollar tasdiqlandi!" , "green"))
                break
            
        while True:
            phone = input("Phone: ")
            
            if not phone.isdigit():
                print(colored("Raqamdan iborat bo'lish kerak!" , "red"))
                
            elif len(phone) != 9:
                print(colored("Telefon nomer 9 raqamdan iborat bo'lsin!" , "red"))
                
            else:
                print(colored("Telefon nomer tasdiqlandi!" , "green"))
                break
            
        while True:
            first_name = input("First Name: ").capitalize()
            
            if not first_name.isalpha():
                print(colored("Ism faqat harfdan iborat bo'lish kerak!" , "red"))
                
            else:
                print(colored("Ism tasdiqlandi!" , "green"))
                break
            
        while True:
            last_name = input("Last Name: ").capitalize()
            
            if not last_name.isalpha():
                print(colored("Familiya faqat harfdan iborat bo'lish kerak!" , "red"))
                
            else:
                print(colored("Familiya tasdiqlandi!" , "green"))
                break
        
        while True:
                age = input("Age: ")
                
                if not age.isdigit():
                   print(colored("Yosh raqamdan iborat bo'lish kerak!" , "red"))
                   
                elif int(age) <= 0:
                    print(colored("Yosh hato kiritildi!" , "red"))
                    
                elif int(age) > 99:
                    print(colored("Yosh hato kiritildi!" , "red"))
                    
                else:
                    print(colored("Yosh tasdiqlandi!" , "green"))  
                    break 
        
        while True:
            gender = input("Gender: ").lower()
            
            if gender not in ["female" , "male"] :
                print(colored("Jins noto'g'ri kiritildi!" , "red"))
                
            else:
                print(colored("Jins tasdiqlandi!" , "green"))
                break


        user = cls(
                str(uuid4()),
                username,
                make_password(password), 
                phone,
                first_name,
                last_name,
                int(age),
                gender
                )


        users = cls.load_users()


        users.append(user)


        cls.save_users(users)

        print(colored("Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi!", "cyan"))

    def login_user():
        try:
            with open('database/users.json', 'r') as file:
                users = json.load(file)
        except:
            print(colored("Foydalanuvchilar ro'yxati topilmadi!", "red"))
            return

        username = input("Username: ")
        password = getpass("Password: ")

        for user in users:
            if user['username'] == username and user['password'] == make_password(password):
                print(colored("Xush kelibsiz!", "green"))
                return True
        
        print(colored("Foydalanuvchi topilmadi!", "red"))
        return False
