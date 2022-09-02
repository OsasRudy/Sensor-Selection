class Product():
    def __init__(self, name: str, space, price: float):
        self.name = name
        self.space = space
        self.price = price


products_list = []

products_list.append(Product('Refrigerator A', 0.751, 999.9))
products_list.append(Product('Cell phone', 0.00000899, 2199.12))
products_list.append(Product('TV 55', 0.400, 4346.99))
products_list.append(Product('TV 50', 0.290, 3999.90))
products_list.append(Product('TV 42', 0.200, 2999.00))
products_list.append(Product('Notebook A', 0.00350, 2499.90))
products_list.append(Product('Ventilator', 0.496, 199.90))
products_list.append(Product('Microwave A', 0.0424, 308.66))
products_list.append(Product('Microwave B', 0.0544, 429.90))
products_list.append(Product('Microwave C', 0.0319, 299.29))
products_list.append(Product('Refrigerator B', 0.635, 849.00))
products_list.append(Product('Refrigerator C', 0.870, 1199.89))
products_list.append(Product('Notebook B', 0.498, 1999.90))
products_list.append(Product('Notebook C', 0.527, 3999.00))

for product in products_list:
    print(product.name, '-', product.space, '-', product.price)
