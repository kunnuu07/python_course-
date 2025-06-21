class product:
    def product_info(self):
        n = int(input("How many Product Is there: "))
        info ={}
        for i in range(n):
            name = input("Enter Product Name: ")
            place = input("Enter Producer Name: ")
            Price = float(input("Enter Price Of Product: "))
            info[name , place] = Price
            
            print("_____Product_Info______")
            for (name,Price),place in info.items():
                print(f"Product:{name} , Producer:{place} : Price{Price}")

            return str(info)

class total(product):
    def collection(self):
        self.totall = sum(self.info , key= self.info.get)
        self.collection = f"Total Collection: {self.totall}"

def file(data,text):
    with open("Product_info.txt" , "w") as f:
        f.write("Product Info Is Following \n\n")
        f.write(text + "\n\n")
        f.write("Total Collection Is " + data)

a = total()
collection = a.collection
info = product()
pro_info = info.product_info

file(collection , pro_info)