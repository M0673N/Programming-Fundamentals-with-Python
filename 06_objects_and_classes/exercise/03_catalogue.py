class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        list_to_be_sorted = [i for i in self.products if i[0] == first_letter]
        return list_to_be_sorted

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        self.products.sort()
        result += "\n".join(self.products)
        return result
