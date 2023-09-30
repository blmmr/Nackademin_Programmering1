# Kontoinformation
import json
import datetime


class AccountInfo:
    def __init__(self, owner, account_id, pin_code, balance):
        self.owner = owner
        self.account_id = account_id
        self.pin_code = pin_code
        self.balance = balance

    # get används för att kapsla in klassparametrarna och säkerställa att dessa data inte ändras. Det är en del av objektorientering.
    # vi skulle kunna använda också set i fall av parametrar som behöver ändras

    def get_owner(self):
        return self.owner

    def get_account_id(self):
        return self.account_id

    def get_pin_code(self):
        return self.pin_code

    def get_balance(self):
        print(f"{self.owner}, your account balance is: {self.balance} SEK")

    def withdraw(self):
        amount = input(
            "Enter the amount to withdraw: ").strip()  # metod för att undvika logiska fel vid inmatning av mellanrum
        try:
            amount = int(amount)
            if amount < 0:
                print("Cannot withdraw a negative amount.")
            elif amount > self.balance:
                print(f"Cannot withdraw more than your account balance which is: {self.balance} SEK")
            else:
                self.balance -= amount
                print(f"{amount} SEK was successfully withdrawn from your account.")
                self.get_balance()
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def deposit(self):
        amount = input(
            "Enter the amount to deposit: ").strip()  # metod för att undvika logiska fel vid inmatning av mellanrum
        print("Please place the money in the machine.")
        try:
            amount = int(amount)
            if amount < 0:
                print("Cannot deposit a negative amount on.")
            else:
                self.balance += amount
                print(f"{amount} SEK was successfully deposited in your account.")
                self.get_balance()
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def quit(self):  # funktionen för att avsluta programmet
        return self.quit


# json filen
def load_accounts():
    try:
        with open("accountlist2.json", "r", encoding="utf-8") as file:  # encoding="utf-8" undviker bokstavsförvrängning vid utskrift av listan
            data = json.load(file)

        return [AccountInfo(account_data["owner"], account_data["account_id"], account_data["pin_code"],
                            account_data["balance"]) for account_data in data]
    except FileNotFoundError:
        return []


def save_accounts(accounts):
    data = [{"owner": account.owner, "account_id": account.account_id, "pin_code": account.pin_code,
             "balance": account.balance}
            for account in accounts]
    with open("accountlist2.json", "w") as file:
        json.dump(data, file, indent=5)


accounts = load_accounts()


def login_UI(accounts):
    print("*" * 60)
    print("*" + "STOCKHOLM BANK MENU".center(58) + "*")
    print("*" * 60)
    user_id = input("To log in, enter your account id: ").strip()
    pin_code_tries = 3

    for account in accounts:
        if user_id == str(account.get_account_id()):
            while pin_code_tries > 0:
                user_pincode = input("Enter your pin code: ").strip()
                for account in accounts:
                    if user_pincode == str(account.get_pin_code()):
                        return account
                else:  # fel pin code, avslutar programmet nu men kan utvecklas mer så att kontot låses t.ex.
                    pin_code_tries -= 1
                    if pin_code_tries == 0:
                        return print(
                            "You have entered the wrong pin code too many times. \nYour account has been locked.")
                    print(f"Pin code incorrect. You have {pin_code_tries} tries left.")
                    continue
    else:
        print("=" * 60)
        print("Account not found. Try again.")  # Konto-ID hittades inte
        return login_UI(accounts)  # fortsätt med begäran och ange ID


def main_UI(account):
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
            action = input(
                "Select an action: ").strip().upper()  # metod för att undvika logiska fel vid inmatning av mellanrum och stora bokstäver
            if action == 'C':
                account.get_balance()
            elif action == 'W':
                account.withdraw()
            elif action == 'D':
                account.deposit()
            elif action == 'Q':
                account.quit()  # anropar funktionen för att avsluta programmet
                print("=" * 60)
                print("Thank you for using our services!")
                print("=" * 60)
                break
            else:
                print("=" * 60)
                print("Invalid action. Please select a valid option.")


logged_in_account = login_UI(accounts)
if logged_in_account:
    main_UI(logged_in_account)
