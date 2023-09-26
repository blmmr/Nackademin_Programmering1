# bank app
class Account:
    def __init__(self, owner, balance, debit, account_id, pin_code):
        self.owner = owner
        self.balance = balance
        # True om debit, False om kredit
        # Debit/Kredit används inte i programmet alls, men ni kan utveckla funktioner så att egenskapen är relevant
        self.debit = bool(debit)
        self.account_id = account_id
        self.pin_code = pin_code

    # lyckades inte implementera detta ännu, programmet kräver bara account_id att få tillgång till konto
    def get_access(self):
        password_input = input("Input your pin-code: (Must be 4 numbers)")
        try:
            password_input = int(password_input)
            if password_input == self.pin_code:
                print(f"Welcome, {self.owner}")
            else:
                print("Account not found.")
                exit()
        except ValueError:
            print("Please enter valid values.")

    def get_balance(self):
        print(f"{self.owner}, your account balance: {self.balance} SEK")

    def withdraw(self):
        amount = input("The sum to withdraw: ")
        try:
            amount = int(amount)
            if amount < 0:
                print("Cannot be negative")
            elif amount > self.balance:
                print(f"Cannot withdraw more than {self.balance}")
            else:
                self.balance -= amount
                print(f"{amount} SEK withdrawn.")
                self.get_balance()
        except ValueError:
            print("Invalid number.")

    def deposit(self):
        print("Please place the money in the machine.")
        amount = input("How much was put?")
        try:
            amount = int(amount)
            if amount < 0:
                print("To withdraw the money from the account, use the Withdraw function.")
            else:
                self.balance += amount
                print(f"{amount} SEK deposited.")
                self.get_balance()
        except ValueError:
            print("Invalid number.")

    def quit(self):  # Funktionen för att avsluta programmet
        print("=================================")
        print("Thank you for using our services!")
        print("=================================")

# de kan vi ha i en separat json fil och spara
accounts = [
    Account("Åsa Åström", 10000, True, 121212, 1212),
    Account("Elsa Eriksson", 5500, True, 234567, 3456),
    Account("Olle Olsson", 32000, True, 987654, 7890),
    Account("Maja Malmström", 7500, True, 567890, 1234),
    Account("Gustav Gustafsson", 15000, True, 345678, 5678),
    Account("Sara Svensson", 2800, True, 456789, 2345),
    Account("Karl Karlsson", 9000, True, 789012, 6789),
    Account("Emma Engström", 42000, True, 345678, 1234),
    Account("Nils Nilsson", 6200, True, 123456, 3456),
    Account("Anna Andersson", 10500, True, 567890, 7890),
    Account("Per Persson", 2000, True, 987654, 2345),
    Account("Linnéa Lindberg", 17500, True, 234567, 5678),
    Account("Anders Åberg", 8800, True, 345678, 1234),
    Account("Ida Isaksson", 44000, True, 121212, 3456),
    Account("Erik Eriksson", 6000, True, 789012, 5678),
    Account("Maria Månsson", 3100, True, 345678, 7890),
    Account("Johan Johansson", 8700, True, 567890, 2345),
    Account("Linda Larsson", 12300, True, 987654, 1234),
    Account("Andreas Andersson", 9300, True, 567890, 5678),
    Account("Karin Karlsson", 42000, True, 345678, 2345),
    Account("David Dahlström", 7000, True, 123456, 1234),
    Account("Anna Andersson", 12500, True, 567890, 3456),
    Account("Peter Persson", 8800, True, 345678, 2345),
    Account("Sofia Svensson", 4800, True, 234567, 5678),
    Account("Jonas Johansson", 11000, True, 345678, 1234),
    Account("Emma Eriksson", 19000, True, 987654, 7890),
    Account("Lars Larsson", 7700, True, 567890, 3456),
    Account("Hanna Holm", 8600, True, 234567, 1234),
    Account("Mikael Mårtensson", 42000, True, 345678, 5678),
    Account("Linnea Lindström", 6200, True, 123456, 2345)
]


def login_UI():
    print("*" * 20)
    print("* STOCKHOLM BANK *")
    print("*" * 20)
    user_id = input("To log in, enter your id: ")
    for account in accounts:
        if user_id == str(account.account_id):
            user_pincode = input("Enter your pin code: ")
            for account in accounts:
                if user_pincode == str(account.pin_code):
                    return account
        else:
            return None


def main_UI(account):
    if account:
        print(f"Welcome, {account.owner}")
        while True:
            print("*" * 20)
            print("ACTIONS:")
            print("[c]heck balance")
            print("[w]ithdraw")
            print("[d]eposit")
            print("[q]uit")
            action = input("Select an action: ").lower() # Metod för att undvika logiska fel vid inmatning av stora bokstäver
            if action == 'c':
                account.get_balance()
            elif action == 'w':
                account.withdraw()
            elif action == 'd':
                account.deposit()
            elif action == 'q':
                account.quit()  # Anropar funktionen för att avsluta programmet
                break
            else:
                print("Invalid action. Please select a valid option.")


logged_in_account = login_UI()
if logged_in_account:
    main_UI(logged_in_account)

