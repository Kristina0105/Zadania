class Client:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Client: {self.name} has balance {self.balance}"

class Bank:
    def __init__(self):
        self.clients = []

    def add_client(self, name):
        client = Client(name)
        self.clients.append(client)

    def find_client(self, name):
        for client in self.clients:
            if client.name == name:
                return client
        return None

    def save_into_file(self, file):
        try:
            with open (file, "w") as file:
                for client in self.clients:
                    file.write(f"{client.name}, {client.balance}")
            print("Data added")
        except IOError as e:
            print(f"Error with adding client's data to file: {e}")

    def download_from_file(self, file):
        try:
            with open(file, "r") as file:
                for line in file:
                    name, balance = line.strip().split(", ")
                    client = Client(name, float(balance))
                    self.clients.append(client)
            print("Data downloaded from file")
        except (IOError, FileNotFoundError) as e:
            print(f"Error with downloading client's data to file: {e}")


bank = Bank()
client1 = Client("w1", 333)
bank.add_client(client1)
print(client1)

client = bank.find_client(client1)
if client:
    print("client exist")
else:
    print("client not found")

bank.save_into_file("clients_data.txt")
bank.download_from_file("clients_data.txt")



