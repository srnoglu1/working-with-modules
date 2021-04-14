import db

def addProduct(productName,price):
    db.products.append({
        "id": len(db.products) +1,
        "product": productName, 
        "price": price
    })

def updateTheProduct(id,productName,price):
    for pdt in db.products:
        if (pdt["id"] == id):
            pdt["product"] == productName
            pdt["price"] == price
            break

def showProducts():
    for pdt in db.products:
        print(f"id: {pdt['id']} product name: {pdt['product']} price: {pdt['price']} ")
