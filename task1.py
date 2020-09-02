import data
import random


class Product(data.ParentProduct):
    def __init__(self, name, amount, price):
        super().__init__(name)
        self.amount = amount
        self.price = price

    def show_price(self, currency):
        print(f"{self.name} price is {self.price}" + currency)

    def show_amount(self):
        print(f"{self.name} amount is {self.amount}")

    def calculate_total_value(self):
        return self.amount * self.price


def generate(products):
    for i in range(len(products)):
        products[i]["amount"] = random.randint(data.products[i]["amount"]["min"], data.products[i]["amount"]["max"])
        products[i]["price"] = random.randint(data.products[i]["price"]["min"], data.products[i]["price"]["max"])


def create_instances(products, obj_values):
    for product in products:
        p = Product(product["name"], product["amount"], product["price"])
        data.obj_list.append(p)
        obj_values.append(p.calculate_total_value())


def write_to_file(products, values):
    f = open("results_01.txt", "w+")
    f.write("Name\tAmount\tPrice\tValue\n")
    for i in range(len(products)):
        f.write(products[i].name+"\t"+str(products[i].amount)+"\t"+str(products[i].price)+"\t"+str(values[i])+"\n")
    f.close()


def main():
    print(data.products)
    my_products = data.products
    generate(my_products)
    print(my_products)
    obj_values = []
    create_instances(my_products, obj_values)
    for obj in data.obj_list:
        print(obj.name, obj.amount, obj.price, sep=' ')
    print(obj_values)
    write_to_file(data.obj_list, obj_values)


if __name__ == '__main__':
    main()
