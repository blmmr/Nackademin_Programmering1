# bank app
import json

class Account:
    def __init__(self, owner, balance, debit, account_id, pin_code):
        self.owner = owner
        self.balance = balance
        self.debit = []
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
                self.record_debit(amount)
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
                self.record_debit(amount)
                print(f"{amount} SEK deposited.")
                self.get_balance()
        except ValueError:
            print("Invalid number.")

    def record_debit(self, amount):
        if amount > 0:
            self.debit.append(amount)

    def get_debit(self):
        if self.debit:
            print(f"Debit History for {self.owner}:")
            for i, amount in enumerate(self.debit, start=1):
                print(f"{i}. {amount} SEK")
        else:
            print("No debit history available.")

    def quit(self):  # Funktionen för att avsluta programmet
        print("=================================")
        print("Thank you for using our services!")
        print("=================================")

def load_accounts():
    try:
        with open("accounts.json", "r") as file:
            data = json.load(file)

        for account_data in data:
            if "debit" not in account_data:
                account_data["debit"] = []

        return [Account(account_data["owner"], account_data["balance"], account_data["debit"], account_data["account_id"], account_data["pin_code"]) for account_data in data]
    except FileNotFoundError:
        return []

def save_accounts(accounts):
    data = [{"owner": account.owner, "balance": account.balance, "debit": account.debit, "account_id": account.account_id, "pin_code": account.pin_code}
            for account in accounts]
    with open("accounts.json", "w") as file:
        json.dump(data, file, indent=5)



def login_UI():
    print("*" * 20)
    print("* STOCKHOLM BANK *")
    print("*" * 20)
    accounts = load_accounts()
    user_id = int(input("To log in, enter your id: "))
    pin_code_tries = 3

    for account in accounts:
        if user_id == int(account.account_id):
            while pin_code_tries > 0:
                user_pincode = input("Enter your pin code: ")
                for account in accounts:
                    if user_pincode == str(account.pin_code):
                        return account
                else:   # fel pin code, avslutar programmet nu men kan utvecklas mer så att kontot låses t.ex.
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
            print("[h]istory")
            print("[q]uit")
            action = input(
                "Select an action: ").lower()  # Metod för att undvika logiska fel vid inmatning av stora bokstäver
            if action == 'c':
                account.get_balance()
            elif action == 'w':
                account.withdraw()
            elif action == 'd':
                account.deposit()
            elif action == 'h':
                account.get_debit()
            elif action == 'q':
                account.quit()  # Anropar funktionen för att avsluta programmet
                break
            else:
                print("Invalid action. Please select a valid option.")


logged_in_account = login_UI()
if logged_in_account:
    main_UI(logged_in_account)
