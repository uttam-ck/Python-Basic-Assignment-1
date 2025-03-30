# Q8. File Restructuring and JSON Formating
# You are given a large dataset in JSON format representing an e-commerce platform's order history, which includes orders from multiple customers. Each order has multiple items, with detailed attributes such as price, quantity, and shipping cost. Additionally, you need to extract specific information, perform calculations like the total cost, apply discounts, and sort the data based on various criteria like the total amount spent by each customer.
# The goal is to:
# Extract and restructure the data into a tabular format.
# Perform calculations such as:
# Total order value (price * quantity).
# Apply a discount based on the total value of an order (e.g., 10% discount if the order exceeds $100).
# Calculate shipping cost based on the number of items ordered (e.g., $5 per item).
# Sort the data by the total amount spent by each customer.
# Format the output so that it can be easily saved into a CSV file.

# So Write a Python program that:
# Extract and restructure the data to create a flat list of each product purchased by each customer, containing:
# Order ID
# Customer Name
# Product Name
# Product Price
# Quantity Purchased
# Total Value (price * quantity)
# Discount (10% if the total order value > $100)
# Shipping Cost (based on the number of items ordered)
# Final Total (after discount + shipping)
# Shipping Address
# Country Code
# Calculate:
# For each order, apply a 10% discount to the total value if the total order value is over $100.
# Calculate the total shipping cost (e.g., $5 per item).
# Compute the final total by adding the shipping cost and applying the discount (if any).
# Sort the list of orders by the final total amount spent by each customer.
# Output the data in CSV format with the following columns:
# Order ID, Customer Name, Product Name, Product Price, Quantity Purchased, Total Value, Discount, Shipping Cost, Final Total, Shipping Address, Country Code
# Constraints:
# The JSON file can contain a variable number of orders.
# Each order contains a variable number of items.
# Handle missing fields or unexpected values gracefully.
# Copy this given JSON and save it as a sales.json file and take it as an input (read file)
# {'orders': [{'order_id': 'O001', 'customer': {'id': 'C001', 'name': 'John Doe', 'email': 'john@example.com'}, 'items': [{'product_id': 'P001', 'name': 'Laptop', 'price': 999.99, 'quantity': 1}, {'product_id': 'P002', 'name': 'Mouse', 'price': 25.99, 'quantity': 2}], 'shipping_address': '123 Main St, Springfield, IL'}, {'order_id': 'O002', 'customer': {'id': 'C002', 'name': 'Jane Smith', 'email': 'jane@example.com'}, 'items': [{'product_id': 'P003', 'name': 'Phone', 'price': 599.99, 'quantity': 1}], 'shipping_address': '456 Oak St, Seattle, WA'}, {'order_id': 'O003', 'customer': {'id': 'C001', 'name': 'John Doe', 'email': 'john@example.com'}, 'items': [{'product_id': 'P004', 'name': 'Headphones', 'price': 149.99, 'quantity': 1}, {'product_id': 'P005', 'name': 'Keyboard', 'price': 99.99, 'quantity': 1}], 'shipping_address': '123 Main St, Springfield, IL'}]}


import json
import csv

def process_sales_data(json_file, output_csv):
    """Processes sales data from JSON and saves it as a CSV file."""
    with open(json_file, "r") as file:
        data = json.load(file)
    
    orders = []
    for order in data.get("orders", []):
        order_id = order.get("order_id", "N/A")
        customer_name = order.get("customer", {}).get("name", "Unknown")
        shipping_address = order.get("shipping_address", "Unknown")
        
        for item in order.get("items", []):
            product_name = item.get("name", "Unknown")
            product_price = item.get("price", 0.0)
            quantity = item.get("quantity", 1)
            total_value = product_price * quantity
            
            discount = total_value * 0.10 if total_value > 100 else 0
            shipping_cost = 5 * quantity
            final_total = total_value - discount + shipping_cost
            
            orders.append([
                order_id, customer_name, product_name, product_price,
                quantity, total_value, discount, shipping_cost,
                final_total, shipping_address, "N/A"
            ])
    
    orders.sort(key=lambda x: x[8], reverse=True)
    
    headers = ["Order ID", "Customer Name", "Product Name", "Product Price", "Quantity Purchased",
               "Total Value", "Discount", "Shipping Cost", "Final Total", "Shipping Address", "Country Code"]
    
    with open(output_csv, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(orders)
    
    print(f"Processed data saved to {output_csv}")

if __name__ == "__main__":
    process_sales_data("sales.json", "sales_output.csv")