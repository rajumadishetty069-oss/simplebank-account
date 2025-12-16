import tkinter as tk
from tkinter import messagebox
import random  # Because generating account numbers via voodoo math is peak financial innovation

class BankAccount:
    def __init__(self, initial_balance=0):
        # Starting balance: As reliable as a chocolate teapot
        self.balance = initial_balance
        # Account number: A random string of digits to make you feel like you're in a spy novel, not a bank
        self.account_number = random.randint(1000000000, 9999999999)
        print(f"New account created: {self.account_number}")  # The bank's way of saying "Welcome to the money pit"
    
    def deposit(self, amount):
        # Depositing? Bold move. Hope it's not your last paycheck
        if amount > 0:
            self.balance += amount
            return f"Deposited ₹{amount}. New balance: ₹{self.balance} – Congrats, you're temporarily not broke"
        else:
            return "Invalid deposit amount. Amount must be positive. (Negative money? That's just debt with extra steps.)"
    
    def withdraw(self, amount):
        # Withdrawal: Because nothing says 'adulting' like pretending you have money
        if amount > self.balance:
            return "Insufficient Balance! Transaction cancelled. (Reality check: You're poorer than you thought.)"
        elif amount <= 0:
            return "Invalid withdrawal amount. Amount must be positive. (Can't withdraw from your dignity – yet.)"
        else:
            self.balance -= amount  # Money gone. Poof. Like your New Year's resolutions
            message = f"Withdrew ₹{amount}. New balance: ₹{self.balance}"
            # Low balance siren: Because ₹99 won't even buy you a participation trophy
            if self.balance < 100:
                message += "\nLow Balance! Please maintain minimum ₹100. (Or embrace ramen life forever.)"
            return message
    
    def get_balance(self):
        return f"Current balance: ₹{self.balance} – Enough for just 1min?"

# GUI: Where bad decisions get a pretty interface
class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Bank Account App")  # "Simple" – said no one who's ever balanced a checkbook
        self.root.geometry("400x350")  # Sized for your delusions of financial grandeur
        
        # Conjure an account. Abracadabra, debt!
        self.account = BankAccount(0)
        
        # Account number: Because every broke millennial needs a secret code
        self.account_label = tk.Label(root, text=f"Account Number: {self.account.account_number}", 
                                      font=("Arial", 10, "bold"))
        self.account_label.pack(pady=5)
        
        # Balance: The cruel truth serum of your life choices
        self.balance_label = tk.Label(root, text=self.account.get_balance(), font=("Arial", 12, "bold"))
        self.balance_label.pack(pady=10)
        
        # Message area: For the bank's passive-aggressive pep talks
        self.message_label = tk.Label(root, text="", fg="blue", wraplength=350)
        self.message_label.pack(pady=5)
        
        # Amount entry: Where dreams (and typos) go to die
        tk.Label(root, text="Enter Amount (₹):", font=("Arial", 10)).pack(pady=5)
        self.amount_entry = tk.Entry(root, font=("Arial", 10))
        self.amount_entry.pack(pady=5)
        self.amount_entry.focus()  # Lazy loading for the terminally impatient
        
        # Buttons: Color-coded for your impending regret
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)
        
        # Deposit: Green like envy – or money you don't deserve
        tk.Button(button_frame, text="Deposit", command=self.deposit, 
                  bg="green", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        # Withdraw: Red for danger – mostly to your wallet
        tk.Button(button_frame, text="Withdraw", command=self.withdraw, 
                  bg="red", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        # Check: Blue like the sadness of seeing your balance
        tk.Button(button_frame, text="Check Balance", command=self.check_balance, 
                  bg="blue", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        # Exit: Gray mercy kill for your financial curiosity
        tk.Button(button_frame, text="Exit", command=root.quit, 
                  bg="gray", fg="white", width=10).pack(side=tk.LEFT, padx=5)
    
    def update_balance(self):
        # Update: Because lies don't refresh themselves
        self.balance_label.config(text=self.account.get_balance())
    
    def show_message(self, msg):
        self.message_label.config(text=msg)
        # Auto-delete: Like your self-control after payday
        self.root.after(5000, lambda: self.message_label.config(text=""))
    
    def deposit(self):
        try:
            amt = float(self.amount_entry.get())  # Alchemy: Words to wealth (usually fails)
            msg = self.account.deposit(amt)
            self.update_balance()
            self.show_message(msg)
            self.amount_entry.delete(0, tk.END)  # Erase evidence of your fleeting riches
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number. (Emojis don't buy groceries.)")
    
    def withdraw(self):
        try:
            amt = float(self.amount_entry.get())
            msg = self.account.withdraw(amt)
            if "cancelled" not in msg.lower():  # Victory lap? Nah, just borrowed time
                self.update_balance()
            self.show_message(msg)
            self.amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number. (Wishing won't make it so.)")
    
    def check_balance(self):
        self.update_balance()
        self.show_message("Balance checked. (Brace yourself – it's rarely good news.)")

# Launch: Into the abyss of amateur banking
if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()