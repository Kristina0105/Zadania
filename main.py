class User:
    def __init__(self, name, pin_code, balance):
        self.name = name
        self.pin_code = pin_code
        self.balance = balance

    def check_pin_code(self, pin_entered):
        return pin_entered == self.pin_code

    def check_balance(self):
        return self.balance

    def pay_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return 0


class Bankomat:
    def __init__(self, bankomat_balance):
        self.bankomat_balance = bankomat_balance
        self.users = {}
        self.load_users()

    def registration(self, name, pin_code, balance):
        new_user = User(name,pin_code, balance)
        self.users[name] = new_user
        self.save_users()

    def login(self, name, pin_code):
        if name in self.users:
            user = self.users[name]
            if user.check_pin_code(pin_code):
                return user
        return None

    def operations(self, user):
        while True:
            print("\nОберіть операцію:")
            print("1. Перевірити баланс")
            print("2. Зняти гроші")
            print("3. Вийти")

            choice = input("Введіть номер операції: ")

            if choice == "1":
                print(f"Поточний баланс: {user.check_balance():.2f} гривень")
            elif choice == "2":
                amount = float(input("Введіть сумму яку хочете зняти: "))
                paid = user.pay_money(amount)
                if paid > 0:
                    print(f"Ви зняли ${paid:.2f}. Поточний баланс: ${user.check_balance():.2f}")
                else:
                    print("Недостатньо коштів на рахунку")
            elif choice == "3":
                break

    def load_users(self):
        try:
            with open(file, "r") as f:
                for line in f:
                    name, pin_code, balance = line.strip().split(",")
                    self.users[name] = User(name, pin_code, float(balance))
        except FileNotFoundError:
            pass

    def save_users(self):
        with open(file, "w") as f:
            for name, user in self.users.items():
                f.write(f"{user.name},{user.pin_code},{user.balance}\n")

file = "users.txt"
bankomat = Bankomat(1000)

while True:
    print("\nОберіть дію:")
    print("1. Реєстрація")
    print("2. Вхід")
    print("3. Вийти")

    option = input("Оберіть номер операції: ")

    if option == "1":
        name = input("Впишіть ім'я: ")
        pin_code = input("Введіть пін-код: ")
        balance = float(input("Введіть початковий баланс: "))
        bankomat.registration(name, pin_code, balance)
        print("Користувача зареєстровано")
    elif option == "2":
        name = input("Впишіть ім'я: ")
        pin_code = input("Введіть пін-код: ")
        user = bankomat.login(name, pin_code)
        if user:
            bankomat.operations(user)
        else:
            print("Неправильне ім'я користувача або пін-код")
    elif option == "3":
        break