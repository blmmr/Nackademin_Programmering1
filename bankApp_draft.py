import json
import datetime
import time


class AccountInfo:  # Skapar en class "AccountInfo"
    def __init__(self, owner, account_id, pin_code, balance):   # Parametrarna kommer från en JSON-fil
        self.owner = owner
        self.account_id = account_id
        self.pin_code = pin_code
        self.balance = balance

    # Metoder för att hämta värden på info om användaren
    def get_owner(self):
        return self.owner

    def get_account_id(self):
        return self.account_id

    def get_pin_code(self):
        return self.pin_code

    def get_balance(self):  # Metod som printar användarens balance när dem väljer
        print(f"Your current balance is: {self.balance} SEK")  # borttagning av användarnamnet

    def withdraw(self): # Metod som låter användaren att withdraw från sitt konto
        amount = input("Enter the amount to withdraw: ").strip()
        try:
            amount = int(amount)
            if amount < 0:  # If-sats så att man inte kan withdrawa negativt (återgår till frågan)
                print("Cannot withdraw a negative amount.")
                print("Please enter a whole number.")  # Endast heltal
                self.withdraw()
            elif amount > self.balance: # Logik för att inte kunna withdrawa mer än man har på kontot
                print(f"Cannot withdraw more than your account balance which is: {self.balance} SEK")
            else:
                self.balance -= amount
                print(f"{amount} SEK was successfully withdrawn from your account!")
                self.get_balance()
        except ValueError:
            print("Invalid input. Please enter a whole number.")  # Endast heltal
            self.withdraw()  # Återgå till samma fråga efter felaktig inmatning

    def deposit(self):  # Metod som låter användaren att deposit till sitt konto
        amount = input("Enter the amount to deposit: ").strip()
        try:
            amount = int(amount)
            if amount < 0:
                print("Cannot deposit a negative amount on.")
            else:
                print("Please place the money in the machine and wait a few\nseconds...⌛")
                time.sleep(3)  # Metod för att fördröja (effekt)
                self.balance += amount
                print(f"{amount} SEK was successfully deposited in your account!")
                self.get_balance()
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            self.deposit()  # Återgå till samma fråga efter felaktig inmatning

    def quit(self):   # Metod för att avsluta körning av programmet
        return self.quit


# json filen
def load_accounts():    # Funktion för att hämta listan med konton från json-filen
    try:
        with open("accountlist2.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        return [AccountInfo(account_data["owner"], account_data["account_id"], account_data["pin_code"],
                            account_data["balance"]) for account_data in data]  # Skapar instanser till klassen
    except FileNotFoundError:
        return []


def login_ui(client):   # Funktion för login UI och login till konto
    print("*" * 60)
    print("*" + "STOCKHOLM BANK MENU".center(58) + "*")
    print("*" * 60)
    user_id = input("To log in, enter your account id: ").strip()
    pin_code_tries = 3

    for account in client:
        if user_id == str(account.get_account_id()):
            while pin_code_tries > 0:
                user_pincode = input("Enter your pin code: ").strip()
                if user_pincode == str(account.get_pin_code()):
                    return account
                else:  # Fel pin code, avslutar programmet
                    pin_code_tries -= 1
                    if pin_code_tries == 0:
                        return print(
                            "You have entered the wrong pin code too many times. \nYour account has been locked.")
                    print(f"Pin code incorrect. You have {pin_code_tries} tries left.")
                    continue
    else:
        print("=" * 60)
        print("Account not found. Try again.")  # Konto-ID hittades inte
        return login_ui(client)  # Fortsätt med begäran och ange ID


def main_ui(account):   # Funktion för main UI och actions
    if account:
        print(f"Welcome, {account.get_owner()}")
        while True:
            print("=" * 60)
            print("ACTIONS:")
            print("=" * 60)
            print("[C]heck balance")
            print("=" * 60)
            print("[W]ithdraw")
            print("=" * 60)
            print("[D]eposit")
            print("=" * 60)
            print("[Q]uit")
            print("=" * 60)
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # datum och tid (realtid)
            print(f"Current Date & Time: {current_time}")
            action = input("Select an action: ").strip().upper()
            if action == 'C':
                account.get_balance()
            elif action == 'W':
                account.withdraw()
            elif action == 'D':
                account.deposit()
            elif action == 'Q':
                account.quit()
                print("=" * 60)
                print("Thank you for using our services!")
                print("=" * 60)
                break
            else:
                print("=" * 60)
                print("Invalid action. Please select a valid option.")

# Kör programmet
accounts = load_accounts()
logged_in_account = login_ui(accounts)
if logged_in_account:
    main_ui(logged_in_account)
