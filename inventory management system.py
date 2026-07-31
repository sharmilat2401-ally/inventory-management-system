import tkinter as tk
from tkinter import messagebox

products = []

# Add Product
def add_product():
    pid = entry_id.get()
    name = entry_name.get()
    qty = entry_qty.get()
    price = entry_price.get()

    if pid == "" or name == "" or qty == "" or price == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    products.append([pid, name, qty, price])
    display_products()
    clear_fields()

# Display Products
def display_products():
    listbox.delete(0, tk.END)
    for product in products:
        listbox.insert(
            tk.END,
            f"ID: {product[0]} | Name: {product[1]} | Qty: {product[2]} | Price: ₹{product[3]}"
        )

# Clear Fields
def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_qty.delete(0, tk.END)
    entry_price.delete(0, tk.END)

# Select Product
def select_product(event):
    try:
        index = listbox.curselection()[0]
        product = products[index]

        clear_fields()
        entry_id.insert(0, product[0])
        entry_name.insert(0, product[1])
        entry_qty.insert(0, product[2])
        entry_price.insert(0, product[3])
    except IndexError:
        pass

# Update Product
def update_product():
    try:
        index = listbox.curselection()[0]
        products[index] = [
            entry_id.get(),
            entry_name.get(),
            entry_qty.get(),
            entry_price.get()
        ]
        display_products()
        clear_fields()
    except IndexError:
        messagebox.showerror("Error", "Select a product to update")

# Delete Product
def delete_product():
    try:
        index = listbox.curselection()[0]
        products.pop(index)
        display_products()
        clear_fields()
    except IndexError:
        messagebox.showerror("Error", "Select a product to delete")

# GUI Window
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("600x500")
root.configure(bg="lightcyan")

# Labels & Entries
tk.Label(root, text="Product ID", bg="lightcyan").pack()
entry_id = tk.Entry(root, width=40)
entry_id.pack()

tk.Label(root, text="Product Name", bg="lightcyan").pack()
entry_name = tk.Entry(root, width=40)
entry_name.pack()

tk.Label(root, text="Quantity", bg="lightcyan").pack()
entry_qty = tk.Entry(root, width=40)
entry_qty.pack()

tk.Label(root, text="Price", bg="lightcyan").pack()
entry_price = tk.Entry(root, width=40)
entry_price.pack()

# Buttons
tk.Button(root, text="Add Product", bg="lightgreen",
          command=add_product, width=20).pack(pady=5)

tk.Button(root, text="Update Product", bg="lightblue",
          command=update_product, width=20).pack(pady=5)

tk.Button(root, text="Delete Product", bg="tomato",
          command=delete_product, width=20).pack(pady=5)

# Product List
listbox = tk.Listbox(root, width=80, height=12)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", select_product)

root.mainloop()