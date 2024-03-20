import tkinter as tk
from inventory_system import Inventory, Product, Supplier, Client

class InventoryApp:
    def __init__(self, master):
        self.master = master
        self.inventory = Inventory()

        # Create widgets
        self.supplier_label = tk.Label(master, text="Supplier")
        self.supplier_entry = tk.Entry(master)
        self.add_supplier_button = tk.Button(master, text="Add Supplier", command=self.add_supplier)

        self.client_label = tk.Label(master, text="Client")
        self.client_entry = tk.Entry(master)
        self.add_client_button = tk.Button(master, text="Add Client", command=self.add_client)

        self.product_name_label = tk.Label(master, text="Product Name")
        self.product_name_entry = tk.Entry(master)
        self.product_quantity_label = tk.Label(master, text="Product Quantity")
        self.product_quantity_entry = tk.Entry(master)
        self.add_product_button = tk.Button(master, text="Add Product", command=self.add_product)

        self.product_name_to_check_label = tk.Label(master, text="Product Name to Check")
        self.product_name_to_check_entry = tk.Entry(master)
        self.check_stock_button = tk.Button(master, text="Check Stock", command=self.check_stock)

        self.product_name_to_restock_label = tk.Label(master, text="Product Name to Restock")
        self.product_name_to_restock_entry = tk.Entry(master)
        self.product_quantity_to_restock_label = tk.Label(master, text="Product Quantity to Restock")
        self.product_quantity_to_restock_entry = tk.Entry(master)
        self.restock_product_button = tk.Button(master, text="Restock Product", command=self.restock_product)

        self.low_stock_threshold_label = tk.Label(master, text="Low Stock Threshold")
        self.low_stock_threshold_entry = tk.Entry(master)
        self.generate_low_stock_warning_button = tk.Button(master, text="Generate Low Stock Warning", command=self.generate_low_stock_warning)

        # Grid widgets
        self.supplier_label.grid(row=0, column=0)
        self.supplier_entry.grid(row=0, column=1)
        self.add_supplier_button.grid(row=0, column=2)

        self.client_label.grid(row=1, column=0)
        self.client_entry.grid(row=1, column=1)
        self.add_client_button.grid(row=1, column=2)

        self.product_name_label.grid(row=2, column=0)
        self.product_name_entry.grid(row=2, column=1)
        self.product_quantity_label.grid(row=2, column=2)
        self.product_quantity_entry.grid(row=2, column=3)
        self.add_product_button.grid(row=2, column=4)

        self.product_name_to_check_label.grid(row=3, column=0)
        self.product_name_to_check_entry.grid(row=3, column=1)
        self.check_stock_button.grid(row=3, column=2)

        self.product_name_to_restock_label.grid(row=4, column=0)
        self.product_quantity_to_restock