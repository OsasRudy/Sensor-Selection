import Individual
import Product
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    #  Lists to  store information regarding the products
    spaces = []
    prices = []
    names = []

    #  add the products to the respctive lists for easier access.
    for product in Product.products_list:
        spaces.append(product.space)
        prices.append(product.price)
        names.append(product.price)

    limit = 3
    individual1 = Individual.Individual(spaces, prices, names)
    print('Spaces:', individual1.spaces)
    print('Prices:', individual1.prices)
    print('Chromosome:', individual1.chromosome)

    """
    for loop to print the products that are going to be chosen
    """
    for i in range(len(Product.products_list)):
        if individual1.chromosome[i] == '1':
            print('Name:', Product.products_list[i].name)
    individual1.fitness()
    print("Score:", individual1.score_evaluation)
    print("Used space:", individual1.used_space)
    print("Chromosome:", individual1.chromosome)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
