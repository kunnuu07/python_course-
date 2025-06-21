'''Create a program that:
Takes input for multiple product names and their prices
Stores them in a dictionary
Finds:
The most expensive product
The average price
The cheapest product '''

def product_info():
    n = int(input("How Many Product?\n\t Enter Here: "))
    product = {}
    for i in range(n):
        name = input("Enter Product Name: ")
        price = int(input("Enter Product Price: "))
        product[name]=price
    return product
    
def avg_product(product_data):
    total = sum(product_data.values())
    avg  = total / len(product_data)
    return avg

def product_price_info(product_data):
    highest = max(product_data,key=product_data.get)
    minimum= min(product_data,key=product_data.get)
    high = highest,product_data[highest]
    low = minimum,product_data[minimum]
    return high , low

product = product_info()
avg = avg_product(product)
high,low = product_price_info(product)

print(f"\nAverage Price: ₹{avg}")
print(f"Most Expensive Product: {high[0]} - ₹{high[1]}")
print(f"Cheapest Product: {low[0]} - ₹{low[1]}")