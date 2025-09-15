class Product():
    serial_num = 0
    def __init__(self):
        Product_num += 1
        self.serial_num = Product.serial_num
        self.name = None
       
if __name__ == 'main':
    tv1 = Product()
    tv2 = Product()
    tv3 = Product()
