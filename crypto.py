class DollarValue:
    def __get__(self, instance, owner):
        quotation = instance.quotation.get(instance.crypto_name, 0) * instance.amount
        return quotation * instance.amount

    def __set__(self, instance, value):
        raise AttributeError("Неможливо змінити доларову вартість напряму")

class Portfel:
    def __init__(self, investor):
        self.investor = investor
        self.crypto = {}
        self.quotation = {}

    def add_crypto(self, crypto_name, amount):
        try:
            if crypto_name in self.crypto:
                self.crypto[crypto_name] += amount
            else:
                self.crypto[crypto_name] = amount
        except Exception as e:
            print(f"Помилка при додаванні криптовалюти: {str(e)}")

    def del_crypto(self, crypto_name):
        try:
            if crypto_name in self.crypto:
                del self.crypto[crypto_name]
            else:
                raise KeyError(f"Криптовалюти '{crypto_name}' немає в портфелі")
        except KeyError as e:
            print(f"Помилка при видаленні криптовалюти: {str(e)}")

    def crypto_to_dollar(self):
        for crypto_name, amount in self.crypto.items():
            pass

    def show_portfel(self):
        self.crypto_to_dollar()
        print(f"Investor: {self.investor}")
        for crypto_name, amount in self.crypto.items():
            dollar_amount = self.quotation.get(crypto_name, 0) * amount
            print(f"Crypto: {crypto_name}, amount: {amount}, USD: {dollar_amount:.2f}")

    def sort_portfel(self):
        self.crypto = {crypto_name: amount for crypto_name, amount in sorted(self.crypto.items(), key=lambda x: -self.quotation.get(x[0], 0)* x[1])}

p = Portfel("Інвестор1")

p.quotation = {
    "btc": 4500,
    "etg": 3200
}

p.add_crypto("btc", 2)
p.add_crypto("etg", 10)

p.show_portfel()


p.sort_portfel()

print("\nВідсортований портфель:")
p.show_portfel()
