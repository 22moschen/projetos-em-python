#criando a estrutura basica do programa
class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Supplier:
    def __init__(self, name):
        self.name = name

class Client:
    def __init__(self, name):
        self.name = name

class Inventory:
    def __init__(self):
        self.products = []
        self.suppliers = []
        self.clients = []

    def add_product(self, product):
        self.products.append(product)

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def add_client(self, client):
        self.clients.append(client)

    def check_stock(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product.quantity
        return None

    def restock_product(self, product_name, quantity):
        for product in self.products:
            if product.name == product_name:
                product.quantity += quantity

    def low_stock_warning(self, threshold=10):
        for product in self.products:
            if product.quantity < threshold:
                print(f"WARNING: Product {product.name} has low stock! Current quantity: {product.quantity}")

#utilizando a Inventoryclasse para criar um sistema de gerenciamento de estoque:

inventory = Inventory()

# Add suppliers
inventory.add_supplier(Supplier("Supplier A"))
inventory.add_supplier(Supplier("Supplier B"))

# Add clients
inventory.add_client(Client("Client A"))
inventory.add_client(Client("Client B"))

# Add products
product_apple = Product("Apples", 50)
inventory.add_product(product_apple)

product_banana = Product("Bananas", 30)
inventory.add_product(product_banana)

# Check stock
print(f"Current stock of apples: {inventory.check_stock('Apples')}")
print(f"Current stock of bananas: {inventory.check_stock('Bananas')}")

# Restock products
inventory.restock_product('Apples', 20)
inventory.restock_product('Bananas', 15)

# Check stock after restocking
print(f"Current stock of apples: {inventory.check_stock('Apples')}")
print(f"Current stock of bananas: {inventory.check_stock('Bananas')}")

# Generate low stock warning
inventory.low_stock_warning()

# A Inventoryclasse contém métodos para adicionar fornecedores,
# clientes, produtos e verificar estoque.
# O low_stock_warningmétodo gera um alerta
# quando o produto está em baixa quantidade.