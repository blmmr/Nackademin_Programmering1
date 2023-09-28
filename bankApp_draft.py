# Kontoinformation

class Account_Info:
    def __init__(self, owner, account_id, pin_code, balance):    # jag ändrade ordningen på parametrarna och försökte följa ungefär samma sekvens i koden
        self.owner = owner
        self.account_id = account_id
        self.pin_code = pin_code
        self.balance = balance

        # debit/Kredit används inte i programmet alls, men ni kan utveckla funktioner så att egenskapen är relevant

        # jag började organisera om koden och kanske jag kommer att skapa en klass till

        # jag tog bort get_access eftersom ändå den frågar redan efter account id och pin code

    def get_owner(self):
        return self.owner

    def get_account_id(self):
        return self.account_id

    def get_pin_code(self):
        return self.pin_code

    def get_balance(self):
        print(f"{self.owner}, your account balance is: {self.balance} SEK")

    def withdraw(self):
        amount = input("Enter the amount to withdraw: ")
        try:
            amount = int(amount)
            if amount < 0:
                print("Cannot withdraw a negative amount.")
            elif amount > self.balance:
                print(f"Cannot withdraw more than your account balance which is: {self.balance} SEK")
            else:
                self.balance -= amount
                print(f"{amount} SEK withdrawn.")
                self.get_balance()
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def deposit(self):
        amount = input("Enter the amount to deposit: ")
        print("Please place the money in the machine.")
        try:
            amount = int(amount)
            if amount < 0:
                print("Cannot deposit a negative amount on .")
            else:
                self.balance += amount
                print(f"{amount} SEK was successfully deposited in your account.")
                self.get_balance()
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def quit(self):  # funktionen för att avsluta programmet
        print("=================================")
        print("Thank you for using our services!")
        print("=================================")


def login_UI(accounts):
    print("*" * 20)
    print("* STOCKHOLM BANK *")
    print("*" * 20)
    user_id = input("To log in, enter your account id: ")
    pin_code_tries = 3

    for account in accounts:
        if user_id == str(account.get_account_id()):
            while pin_code_tries > 0:
                user_pincode = input("Enter your pin code: ")
                for account in accounts:
                    if user_pincode == str(account.get_pin_code()):
                        return account
                else:  # fel pin code, avslutar programmet nu men kan utvecklas mer så att kontot låses t.ex.
                    pin_code_tries -= 1
                    if pin_code_tries == 0:
                        return print(
                            "You have entered the wrong pin code too many times. Your account has been locked.")
                    print(f"Pin code incorrect. You have {pin_code_tries} tries left.")
                    continue
    else:
        print("*" * 20)
        print("Account not found.")  # Konto-ID hittades inte
        print("*" * 20)
        print("Try again.")
        return login_UI(accounts)  # fortsätt med begäran och ange ID


def main_UI(account):
    if account:
        print(f"Welcome, {account.get_owner()}")
        while True:
            print("*" * 20)
            print("ACTIONS:")
            print("[c]heck balance")
            print("[w]ithdraw")
            print("[d]eposit")
            print("[q]uit")
            action = input("Select an action: ").strip().lower()   # metod för att undvika logiska fel vid inmatning av mellanrum och stora bokstäver
            if action == 'c':
                account.get_balance()
            elif action == 'w':
                account.withdraw()
            elif action == 'd':
                account.deposit()
            elif action == 'q':
                account.quit()  # anropar funktionen för att avsluta programmet
                break
            else:
                print("Invalid action. Please select a valid option.")


# databas med information för varje konto omorganiserades och flyttades till slutet av koden
# de kan vi ha i en separat json fil och spara
accounts = [
    Account_Info("Åsa Åström", 121212, 1213, 10000),
    Account_Info("Elsa Eriksson", 234567, 3457, 5500),
    Account_Info("Olle Olsson", 987654, 7891, 32000),
    Account_Info("Maja Malmström", 567890, 1235, 7500),
    Account_Info("Gustav Gustafsson", 345678, 5679, 15000),
    Account_Info("Sara Svensson", 456789, 2346, 2800),
    Account_Info("Karl Karlsson", 789012, 6790, 9000),
    Account_Info("Emma Engström", 345678, 1236, 42000),
    Account_Info("Nils Nilsson", 123456, 3457, 6200),
    Account_Info("Anna Andersson", 567890, 7892, 10500),
    Account_Info("Per Persson", 987654, 2347, 2000),
    Account_Info("Linnéa Lindberg", 234567, 5680, 17500),
    Account_Info("Anders Åberg", 345678, 1237, 8800),
    Account_Info("Ida Isaksson", 121213, 3458, 44000),
    Account_Info("Erik Eriksson", 789013, 6791, 6000),
    Account_Info("Maria Månsson", 345679, 1238, 3100),
    Account_Info("Johan Johansson", 567891, 7893, 8700),
    Account_Info("Linda Larsson", 987655, 2348, 12300),
    Account_Info("Andreas Andersson", 567891, 5681, 9300),
    Account_Info("Karin Karlsson", 345679, 1239, 42000),
    Account_Info("David Dahlström", 123457, 3459, 7000),
    Account_Info("Anna Andersson", 567892, 5682, 12500),
    Account_Info("Peter Persson", 345680, 1240, 8800),
    Account_Info("Sofia Svensson", 234568, 5683, 4800),
    Account_Info("Jonas Johansson", 345681, 1241, 11000),
    Account_Info("Emma Eriksson", 987656, 6792, 19000),
    Account_Info("Lars Larsson", 567893, 5684, 7700),
    Account_Info("Hanna Holm", 234569, 1242, 8600),
    Account_Info("Mikael Mårtensson", 345682, 1243, 42000),
    Account_Info("Linnea Lindström", 123458, 3460, 6200)
]

logged_in_account = login_UI(accounts)
if logged_in_account:
    main_UI(logged_in_account)
