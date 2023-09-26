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
    Account("Åsa Åström", 10000, True, 157838, 9885),
    Account("Elsa Eriksson", 5500, True, 197606, 6214),
    Account("Olle Olsson", 32000, True, 346709, 2507),
    Account("Maja Malmström", 7500, True, 231046, 6302),
    Account("Gustav Gustafsson", 15000, True, 564293, 9149),
    Account("Sara Svensson", 2800, True, 157507, 9123),
    Account("Karl Karlsson", 9000, True, 328400, 7465),
    Account("Emma Engström", 42000, True, 963078, 7619),
    Account("Nils Nilsson", 6200, True, 404388, 2008),
    Account("Anna Andersson", 10500, True, 331646, 7345),
    Account("Per Persson", 2000, True, 221171, 1255),
    Account("Linnéa Lindberg", 17500, True, 272883, 7328),
    Account("Anders Åberg", 8800, True, 494224, 5203),
    Account("Ida Isaksson", 44000, True, 681794, 1164),
    Account("Erik Eriksson", 6000, True, 994270, 1856),
    Account("Maria Månsson", 3100, True, 244977, 5595),
    Account("Johan Johansson", 8700, True, 914766, 4396),
    Account("Linda Larsson", 12300, True, 684010, 2586),
    Account("Andreas Andersson", 9300, True, 653698, 2316),
    Account("Karin Karlsson", 42000, True, 378913, 1989),
    Account("David Dahlström", 7000, True, 326565, 4576),
    Account("Anna Andersson", 12500, True, 719667, 8096),
    Account("Peter Persson", 8800, True, 488449, 3564),
    Account("Sofia Svensson", 4800, True, 175489, 9081),
    Account("Jonas Johansson", 11000, True, 739594, 2754),
    Account("Emma Eriksson", 19000, True, 349790, 6433),
    Account("Lars Larsson", 7700, True, 227997, 6902),
    Account("Hanna Holm", 8600, True, 611915, 2978),
    Account("Mikael Mårtensson", 42000, True, 704174, 6287),
    Account("Linnea Lindström", 6200, True, 702902, 7469)
]


def login_UI():
    print("*" * 20)
    print("* STOCKHOLM BANK *")
    print("*" * 20)
    user_id = int(input("To log in, enter your id: "))
    pin_code_tries = 3

    for account in accounts:
        if user_id == int(account.account_id):
            while pin_code_tries > 0:
                user_pincode = input("Enter your pin code: ")
                for account in accounts:
                    if user_pincode == str(account.pin_code):
                        return account
                else:   # fel pin code
                        pin_code_tries -= 1
                        if pin_code_tries == 0:
                            return print("You have entered the wrong pin code too many times. Your account has been locked.")
                        print(f"Pin code incorrect. You have {pin_code_tries} tries left.")
                        continue
    else:
        return print("Account not found.")  # Konto-ID hittades inte



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
            action = input(
                "Select an action: ").lower()  # Metod för att undvika logiska fel vid inmatning av stora bokstäver
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
