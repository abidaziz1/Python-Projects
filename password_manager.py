import sqlite3
from cryptography.fernet import Fernet
import os,random,string,getpass

# Generate a random secret key
def generate_key():
    return Fernet.generate_key()

def load_key():
    return open("secret.key","rb").read()

def save_key(key):
    with open("secret.key","wb") as key_file:
        key_file.write(key)

# Check if secret.key exists
if not os.path.exists("secret.key"):
    key = generate_key()
    save_key(key)
else:
    key = load_key()

cipher = Fernet(key)

# Database Setup
conn = sqlite3.connect('passwords.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS passwords
             (id INTEGER PRIMARY KEY, service TEXT, username TEXT, password TEXT)''')
conn.commit()

# Generate Password
def generate_password(length=12):
    letters = string.ascii_letters + string.digits + string.punctuation
    password =  ''.join(random.choice(letters) for i in range(length))
    return password

# Add Password
def add_password(service, username, password):
    encrypted_password = cipher.encrypt(password.encode()).decode()
    c.execute("INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)", (service, username, encrypted_password))
    conn.commit()

# Retrieve Password
def get_password(service):
    c.execute("SELECT username, password FROM passwords WHERE service=?", (service,))
    result = c.fetchone()
    if result:
        username, encrypted_password = result
        decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
        return username, decrypted_password
    return None

def delete_password(service):
    c.execute("DELETE FROM passwords WHERE service=?", (service,))
    conn.commit()

def list_services():
    c.execute("SELECT service FROM passwords")
    return [row[0] for row in c.fetchall()]

def main():
    while True:
        print("\nPassword Manager")
        print("1. Add new password")
        print("2. Retrieve password")
        print("3. Delete password")
        print("4. List services")
        print("5. Generate password")
        print("6. Exit")        
        choice = input("Choose an option: ")
        
        if choice == '1':
            service = input("Enter the service: ")
            username = input("Enter the username: ")
            password = getpass.getpass("Enter the password (leave empty to generate a new one): ")
            if not password:
                password = generate_password()
                print(f"Generated password: {password}")
            add_password(service, username, password)
            print(f"Password for {service} added.")

        elif choice == '2':
            service = input("Enter the service: ")
            result = get_password(service)
            if result:
                username, password = result
                print(f"Username: {username}")
                print(f"Password: {password}")
            else:
                print("Service not found.")
        
        elif choice == '3':
            service = input("Enter the service: ")
            delete_password(service)
            print(f"Password for {service} deleted.")
        
        elif choice == '4':
            services = list_services()
            if services:
                print("Services:")
                for service in services:
                    print(service)
            else:
                print("No services found.")
        
        elif choice == '5':
            length = int(input("Enter the password length (default is 12): "))
            password = generate_password(length)
            print(f"Generated password: {password}")
        
        elif choice == '6':
            print("Exiting")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()