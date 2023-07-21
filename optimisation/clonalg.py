import math
import numpy as np
from numpy.random import uniform

def affinity(p_i, fonk, hist):    
    return fonk(p_i,hist)

def create_random_cells(population_size, problem_size, Xmin, Xmax):
    population = [np.sort(uniform(low=Xmin, high=Xmax, size=problem_size).astype(int)) for x in range(population_size)]
    # population = [[uniform(low=-3, high=12), uniform(low=4, high=6)]for x in range(population_size)]

    return population

def clone(p_i, clone_rate):
    clone_num = int(clone_rate / p_i[1])
    clones = [(p_i[0], p_i[1]) for x in range(clone_num)]
    
    return clones

def hypermutate(p_i, mutation_rate, Xmin, Xmax, fonk, hist):
    if uniform() <= p_i[1] / (mutation_rate * 100):
        ind_tmp = []
        for gen in p_i[0]:
            if uniform() <= p_i[1] / (mutation_rate * 100):
                ind_tmp.append(int(uniform(low=Xmin, high=Xmax)))
            else:
                ind_tmp.append(gen)
                
        return (np.array(ind_tmp), affinity(ind_tmp,fonk, hist))
    else:
        return p_i

def select(pop, pop_clones, pop_size, maxShort):
    population = pop + pop_clones    
    population = sorted(population, key=lambda x: x[1],reverse=maxShort)[:pop_size]    
    return population

def replace(population, population_rand, population_size, maxShort):
    population = population + population_rand
    population = sorted(population, key=lambda x: x[1],reverse=maxShort)[:population_size]
    
    return population

def init(hist, fitnessFonk, params = [100,100,90,70], esik = 3):

    population_size = int(params[1])
    selection_size = 10
    problem_size = int(esik)
    clone_rate = int(params[2])
    random_cells_num = int(params[3])
    
    mutation_rate = 0.2
    stop_codition = int(params[0])
    maxShort = True
    stop = 0
    Xmin = 2
    Xmax = 253
    population = create_random_cells(population_size, problem_size, Xmin, Xmax)
    best_affinity_it = []   


    while stop != stop_codition:
        # Affinity(p_i)
        population_affinity = [(p_i, affinity(p_i,fitnessFonk, hist)) for p_i in population]
        populatin_affinity = sorted(population_affinity, key=lambda x: x[1],reverse=maxShort)
        
        best_affinity_it.append(populatin_affinity[:5])
        
        # Populatin_select <- Select(Population, Selection_size)
        population_select = populatin_affinity[:selection_size]
        
        # Population_clones <- clone(p_i, Clone_rate)
        population_clones = []
        for p_i in population_select:
            p_i_clones = clone(p_i, clone_rate)
            population_clones += p_i_clones
            
        # Hypermutate and affinity
        pop_clones_tmp = []
        for p_i in population_clones:
            ind_tmp = hypermutate(p_i, mutation_rate, Xmin, Xmax, fitnessFonk, hist)
            pop_clones_tmp.append(ind_tmp)
        population_clones = pop_clones_tmp
        del pop_clones_tmp
        
        # Population <- Select(Population, Population_clones, Population_size)
        population = select(populatin_affinity, population_clones, population_size, maxShort)
        # Population_rand <- CreateRandomCells(RandomCells_num)
        population_rand = create_random_cells(random_cells_num, problem_size, Xmin, Xmax)
        population_rand_affinity = [(p_i, affinity(p_i,fitnessFonk, hist)) for p_i in population_rand]
        population_rand_affinity = sorted(population_rand_affinity, key=lambda x: x[1] ,reverse=maxShort)
        # Replace(Population, Population_rand)
        population = replace(population_affinity, population_rand_affinity, population_size, maxShort)
        population = [p_i[0] for p_i in population]
        
        stop += 1
       
    bests_mean = []
    
   
    liste = []
    for l1 in best_affinity_it:    
        for l2 in l1:
            liste.append([l2[0], l2[1]])    
    max_fit = [a[1] for a in liste]
    max_index = np.argmax(max_fit)    
    return [liste[max_index][1],liste[max_index][0]]
    