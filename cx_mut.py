import copy
import random

def varOr(population, toolbox, cxpb, mutpb):
    assert (cxpb + mutpb) <= 1.0, ("The sum of the crossover and mutation "
        "probabilities must be smaller or equal to 1.0.")

    new_pop = [toolbox.clone(ind) for ind in population]
    offspring = []
    for i in range(1, len(new_pop), 2):
        new_pop[i-1].off_cx_set(0), new_pop[i].off_cx_set(0)
        if random.random() < cxpb and len(ind)>1:
            new_pop[i-1].off_cx_set(1)
            new_pop[i].off_cx_set(1)
            offspring1, offspring2 = toolbox.mate(new_pop[i-1], new_pop[i])
            del offspring1.fitness.values
            del offspring2.fitness.values
            offspring1.off_cx_set(1), offspring2.off_cx_set(1)
            offspring.append(offspring1)
            offspring.append(offspring2)
    for i in range(len(new_pop)):
        if new_pop[i].off_cx_get() != 1:
            if random.random() < (cxpb+mutpb):  # Apply mutation
                offspring1, = toolbox.mutate(new_pop[i])
                del offspring1.fitness.values
                offspring1.off_mut_set(1)
                offspring.append(offspring1)

    if len(offspring) < len(population):
        for i in range(len(new_pop)):
            if new_pop[i].off_mut_get() != 1 and new_pop[i].off_cx_get() != 1:
                offspring1 = copy.deepcopy(new_pop[i])
                offspring.append(offspring1)

    return offspring
