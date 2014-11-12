#from glob import glob

#print glob("edd-pop-50.o20347177-*")

import sys

best_fit = 0
best_pop = 0
progress = 0

best = dict()

for x in sys.argv[1:]:
    data = open(x, 'r')
    for line in data:
        progress = line.split()[1][:-1]
        #print(line.split())
        if line.split()[0] == "population":
            population = line.split()[4]
            if population not in best:
                best[population] = (0,0)
            #print(population)
        if line.split()[0] == "gen":
            fitness = line.split()[3][1:]
            generation = line.split()[1][:-1]
            #print(fitness)
            if fitness > best[population][0]:
                best[population] = (fitness, generation)

print(progress)


for j , k in best.iteritems():
    print(j , k)
