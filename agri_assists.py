class AgriculturalAccount:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation


class User:
    def __init__(self, username, password, account):
        self.username = username
        self.password = password
        self.account = account


class UserManager:
    def __init__(self):
        self.users = []

    #Create a new account
    def create_account(self):
        username = input("Enter username: ")
        if any(user.username == username for user in self.users):
            print("Username already exists. Please choose a different username.")
            return
        password = input("Enter password: ")
        name = input("Enter your full name: ")
        age = int(input("Enter age: "))
        occupation = input("Enter occupation: ")
        account = AgriculturalAccount(name, age, occupation)
        new_user = User(username, password, account)
        self.users.append(new_user)
        print("Account created successfully!")

    #log in function
    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in self.users:
            if user.username == username and user.password == password:
                print(f"Welcome, {user.account.name}!")
                return user
        print("Invalid username or password.")
        return None

    #Display information
    def display_profile(self, user):
        print("\n=== User Profile ===")
        print(f"Name: {user.account.name}")
        print(f"Age: {user.account.age}")
        print(f"Occupation: {user.account.occupation}")
        print("======================")


class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class ProductManager:
    def __init__(self):
        self.products = []

    #add new product (farmer)
    def add_product(self):
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
        self.products.append(Product(name, quantity, price))
        print("Product added successfully!")

    #Display products
    def display_products(self):
        if not self.products:
            print("No products available.")
            return
        print("\n=== Available Products ===")
        for idx, product in enumerate(self.products, start=1):
            if product.quantity > 0:
                print(f"{idx}. {product.name} - {product.quantity} units at ${product.price:.2f} each")
        print("============================")

    def buy_product(self):
        self.display_products()
        if not self.products:
            return
        choice = int(input("Enter the product number to buy: ")) - 1
        if choice < 0 or choice >= len(self.products):
            print("Invalid choice.")
            return
        product = self.products[choice]
        quantity = int(input(f"Enter quantity to buy (Available: {product.quantity}): "))
        if quantity <= 0 or quantity > product.quantity:
            print("Invalid quantity.")
            return
        total_price = quantity * product.price
        confirm = input(f"The total price is ${total_price:.2f}. Confirm purchase? (yes/no): ").strip().lower()
        if confirm == 'yes':
            product.quantity -= quantity
            print("Purchase successful!")
            if product.quantity == 0:
                self.products.remove(product)
        else:
            print("Purchase canceled.")


class MainMenu:
    def __init__(self):
        self.user_manager = UserManager()
        self.product_manager = ProductManager()
        self.logged_in_user = None
        self.predefined_data()

    def predefined_data(self):
        # Predefined accounts for students and farmer
        self.user_manager.users.append(User("afiq", "password123", AgriculturalAccount("Afiq Shahriar", 22, "Student")))
        self.user_manager.users.append(User("ismail", "password123", AgriculturalAccount("Ismail Rabbi", 23, "Student")))
        self.user_manager.users.append(User("kazi", "password123", AgriculturalAccount("Kazi Tawhid", 35, "Farmer")))

        # Predefined products
        self.product_manager.products.append(Product("Rice", 100, 56))
        self.product_manager.products.append(Product("Potato", 150, 35.00))
        self.product_manager.products.append(Product("Cucumber", 80, 75))
        self.product_manager.products.append(Product("Tomato", 110, 70))

    def display_menu(self):
        while True:
            print("\n=== Agri Assist ===")
            if self.logged_in_user is None:
                print("1. Create Account")
                print("2. Login")
                print("3. Exit")
            elif self.logged_in_user.account.occupation.lower() == "farmer":
                print("1. Add Product")
                print("2. Display Products")
                print("3. Buy Product")
                print("4. View Profile")
                print("5. Logout")
            else:  # Non-farmer accounts
                print("1. Display Products")
                print("2. Buy Product")
                print("3. View Profile")
                print("4. Logout")

            choice = int(input("Enter your choice: "))

            if self.logged_in_user is None:
                if choice == 1:
                    self.user_manager.create_account()
                elif choice == 2:
                    self.logged_in_user = self.user_manager.login()
                elif choice == 3:
                    print("Thank you for using Agri Assist!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            elif self.logged_in_user.account.occupation.lower() == "farmer":
                if choice == 1:
                    self.product_manager.add_product()
                elif choice == 2:
                    self.product_manager.display_products()
                elif choice == 3:
                    self.product_manager.buy_product()
                elif choice == 4:
                    self.user_manager.display_profile(self.logged_in_user)
                elif choice == 5:
                    self.logged_in_user = None
                    print("Logged out successfully!")
                else:
                    print("Invalid choice. Please try again.")
            else:  # Non-farmer accounts
                if choice == 1:
                    self.product_manager.display_products()
                elif choice == 2:
                    self.product_manager.buy_product()
                elif choice == 3:
                    self.user_manager.display_profile(self.logged_in_user)
                elif choice == 4:
                    self.logged_in_user = None
                    print("Logged out successfully!")
                else:
                    print("Invalid choice. Please try again.")



menu = MainMenu()
menu.display_menu()

