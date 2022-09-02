from random import random
import Product
# A set individual make up a population.
class Individual():
    def __init__(self, spaces: float, prices: float, space_limit: float = 3.0, generation: int = 0):
        self.spaces: float = spaces
        self.prices: float = prices
        self.space_limit: float = space_limit
        self.score_evaluation = 0
        self.used_space = 0
        self.generation = generation
        #  A set of chromosome represents a solution.
        self.chromosome = []

        for i in range(len(spaces)):
            #  Fifty percent probability to select a random number greater than 0.5 o
            if random() < 0.5:
                self.chromosome.append('0')
            else:
                self.chromosome.append('1')

    def fitness(self):
        """
        Fitness function --> quality measurement to find out how the chromosome solve the problem
        check if its an acceptable solution that could be used for evaluation
        solution based on a maximisation problem --> maximise the profit based on the price of the products

        """
        score: int = 0
        sum_spaces: float = 0
        #  loop through the selected chromosomes = products
        for i in range(len(self.chromosome)):
            if self.chromosome[i] == '1':   #means the product has been selected
                score += self.prices[i]  #sum all the prices of the selected products
                sum_spaces += self.spaces[i]
                print(sum_spaces)
                print(self.space_limit)
        # if the total space surpirses the limit  and not use the individual in the next generation
        if sum_spaces > self.space_limit:
            score = 1
        self.score_evaluation = score
        self.used_space = sum_spaces
