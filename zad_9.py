class BankAccount:

    def __init__(self, owner, password, value):
        self.owner = owner
        self.value = value
        self.password = password

    def deposit(self, added):
        self.value += added
        print(f"{added}$ zostalo dodane, teraz masz: {self.value}$")

    def withdraw(self, taken):
        if self.value < taken:
            print(f"nie mozesz wyplacic tyle: {taken}$, masz tylko: {self.value}$")
        else:
            self.value -= taken
            print(f"wyplaciles: {taken}$, teraz masz: {self.value}$")

    def password_check(self, psw):
        correct_password = 0
        while not correct_password:
            if psw == self.password:
                correct_password = 1
                print("weryfikacja zakonczona sukcesem.")
            else:
                psw = input("niepoprawne haslo, podaj haslo ponownie: ")

    def balance_check(self):
        print(f"teraz masz: {self.value}$")


name = input("podaj swoje imie: ")
passwrd = input("podaj haslo do konta: ")
amount = int(input("podaj jaka ilosc chcesz wplacic na początek: "))

new_acc = BankAccount(name, passwrd, amount)
while True:
    password_input = input("podaj haslo: ")
    new_acc.password_check(password_input)
    next_step = int(input(f"Czesc {new_acc.owner}. Co chcesz zrobić w kolejnym kroku? \n 1 - wplacic \n 2 - wyplacic \n 3 - sprawdzic stan konta \n 4 - zakonczyc korzystanie z banku \n"))
    if next_step == 1:
        new_acc.deposit(int(input("podaj ilosc: ")))
    if next_step == 2:
        new_acc.withdraw(int(input("podaj ilosc: ")))
    if next_step == 3:
        new_acc.balance_check()
    if next_step == 4:
        break
