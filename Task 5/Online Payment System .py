class Payment:
    def pay(self, amount):
        print("Processing payment of", amount)

class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card.")
        print("Verifying card details...")
        print("Payment Successful!\n")

class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI.")
        print("Checking UPI ID...")
        print("Payment Successful!\n")

class WalletPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Wallet.")
        print("Checking wallet balance...")
        print("Payment Successful!\n")

payment1 = CreditCardPayment()
payment2 = UPIPayment()
payment3 = WalletPayment()

payment_list = [payment1, payment2, payment3]

amount = 1000

for payment in payment_list:
    payment.pay(amount)