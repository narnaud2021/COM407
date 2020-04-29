
from random import *

def init_population(number_of_individuals, genes):
    population = []
    for i in range(number_of_individuals):
        individual = []
        for j in range(genes):
            geneb = randint(0,1)
            individual.append(geneb)
        population.append([individual, -1])
    return population

def calc_fitness(target, population):
    
    '''Calculates the fitness of a population by checking the amount of true
    statements in each individual by comparing if they match to the target
    individual, and adding all of them and then returning
    the fitness'''
    similarity = population == target
    fitness_scores = []
    for chrom in population:
        fitness = 0
        for i in chrom[0]:
            if i == 1:
                fitness = fitness + 1
            else:
                fitness = fitness + 0
        chrom[1] = fitness
        fitness_scores.append(fitness)

    return fitness_scores

def calc_fitness2(target, population):
    
    '''Calculates the fitness of an individual by checking the amount of true
    statements matching the target and adding them act, and then returning
    the fitness'''
    fitness = 0
    for i in range(len(population)):
        if population[i] == target[i]:
            fitness = fitness + 1
        else:
            fitness = fitness + 0
    return fitness

def roulette_wheel_selection(population, fitness):
    
    '''Adds the sum of all the individual's fitness in the population. Next it creates 
    a random number from zero to the sum. If the current number is not higher than 
    the random number, it checks the next row while increasing the fitness. Thus, higher fitness 
    indiviudals have a higher chance of being picked.'''
    fitness_sum = sum(fitness)
    pick = randrange(0, int(fitness_sum))
    current = 0
    for row in population:
        current += row[1] 
        if current > pick:  
            return row

def breed_by_crossover(parent_1, parent_2):
    
    '''Creates a random crossover point. The offspring is produced by taking the chromsomes from
    the beginning to the crossover point of the first parent and the rest from the second 
    parent. Then it returns the child.'''
    
    chromosome_length = len(parent_1)
    crossover_point = randint(1,chromosome_length-1)
    child = parent_1[0:crossover_point] + parent_2[crossover_point::]
    
    return child

def mutation(population, mutation_rate):

    '''Goes through all the chromosomes from all the individuals in the population. It creates a
    random probability. Mutation occurs if the probability is less than the set mutation rate and
    flips the chromosome'''
    for i in range(len(population)):
        for j in range(len(population[0])):
            random_mutate_possibility = uniform(0,1)
            if random_mutate_possibility <= mutation_rate:
                if population[i][0][j] == 1:
                    population[i][0][j] = 0
                else:
                    population[i][0][j] = 1


    return population
