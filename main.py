class Product:
    def __init__(self, name: str, price: float, discountPercent: float):
        
        self.name = name
        self.price = price
        self.discountPercent = discountPercent

    def getDiscountAmount(self):
        return self.price - self.getDiscountPrice()

    def getDiscountPrice(self):
        return (self.price * self.discountPercent) / 100
