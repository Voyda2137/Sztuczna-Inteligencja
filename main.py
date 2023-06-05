import csv

import numpy as np
import time
from Ant import ant_colony_optimization, generate_distance_matrix

num_ants1 = 40
num_iterations1 = 50
num_ants2 = 80
num_iterations2 = 100
num_ants3 = 120
num_iterations3 = 150
num_cities = 50
alpha = 1
beta = 2
rho = 0.1
initial_pheromone = 0.1
# distance = generate_distance_matrix(num_cities)
# np.savetxt('macierz.txt', distance, fmt='%.8f')
distance = np.loadtxt('macierz.txt')
start = time.perf_counter()
best_distance1, best_path1, results1 = ant_colony_optimization(num_ants1, num_iterations1, num_cities, alpha, beta, rho, initial_pheromone, distance)
end = time.perf_counter()
final1 = end - start
final1 = f"{final1:.4f}"
np.savetxt('results1.csv', results1, delimiter=',', fmt='%.0f')

start = time.perf_counter()
best_distance2, best_path2, results2 = ant_colony_optimization(num_ants1, num_iterations2, num_cities, alpha, beta, rho, initial_pheromone, distance)
end = time.perf_counter()
final2 = end - start
final2 = f"{final2:.4f}"
np.savetxt('results2.csv', results2, delimiter=',', fmt='%.0f')

start = time.perf_counter()
best_distance3, best_path3, results3 = ant_colony_optimization(num_ants1, num_iterations3, num_cities, alpha, beta, rho, initial_pheromone, distance)
end = time.perf_counter()
final3 = end - start
final3 = f"{final3:.4f}"
np.savetxt('results3.csv', results3, delimiter=',', fmt='%.0f')

start = time.perf_counter()
best_distance4, best_path4, results4 = ant_colony_optimization(num_ants2, num_iterations1, num_cities, alpha, beta, rho, initial_pheromone, distance)
end = time.perf_counter()
final4 = end - start
final4 = f"{final4:.4f}"
np.savetxt('results4.csv', results4, delimiter=',', fmt='%.0f')

start = time.perf_counter()
best_distance5, best_path5, results5 = ant_colony_optimization(num_ants2, num_iterations2, num_cities, alpha, beta, rho, initial_pheromone, distance)
end = time.perf_counter()
final5 = end - start
final5 = f"{final5:.4f}"
np.savetxt('results5.csv', results5, delimiter=',', fmt='%.0f')

start = time.perf_counter()
best_distance6, best_path6, results6 = ant_colony_optimization(num_ants2, num_iterations3, num_cities, alpha, beta, rho, initial_pheromone, distance)
end = time.perf_counter()
final6 = end - start
final6 = f"{final6:.4f}"
np.savetxt('results6.csv', results6, delimiter=',', fmt='%.0f')

start = time.perf_counter()
best_distance7, best_path7, results7 = ant_colony_optimization(num_ants3, num_iterations1, num_cities, alpha, beta, rho, initial_pheromone, distance)
end = time.perf_counter()
final7 = end - start
final7 = f"{final7:.4f}"
np.savetxt('results7.csv', results7, delimiter=',', fmt='%.0f')

start = time.perf_counter()
best_distance8, best_path8, results8 = ant_colony_optimization(num_ants3, num_iterations2, num_cities, alpha, beta, rho, initial_pheromone, distance)
end = time.perf_counter()
final8 = end - start
final8 = f"{final8:.4f}"
np.savetxt('results8.csv', results8, delimiter=',', fmt='%.0f')

start = time.perf_counter()
best_distance9, best_path9, results9 = ant_colony_optimization(num_ants3, num_iterations3, num_cities, alpha, beta, rho, initial_pheromone, distance)
end = time.perf_counter()
final9 = end - start
final9 = f"{final9:.4f}"
np.savetxt('results9.csv', results9, delimiter=',', fmt='%.0f')
arr = [['time1',final1], ['time2',final2], ['time3',final3], ['time4',final4], ['time5',final5], ['time6',final6], ['time7',final7], ['time8',final8], ['time9',final9]]
# np.savetxt('exectime.csv', arr, delimiter=',', fmt='%.04')
print(f"Best distance found for 40 ants 50 iterations: {best_distance1}")
print(f"Best path found for 40 ants 50 iterations: {best_path1}")

print(f"Best distance found for 40 ants 100 iterations: {best_distance2}")
print(f"Best path found for 40 ants 100 iterations: {best_path2}")

print(f"Best distance found for 40 ants 150 iterations: {best_distance3}")
print(f"Best path found for 40 ants 150 iterations: {best_path3}")

print(f"Best distance found for 80 ants 50 iterations: {best_distance4}")
print(f"Best path found for 80 ants 50 iterations: {best_path4}")

print(f"Best distance found for 80 ants 100 iterations: {best_distance5}")
print(f"Best path found for 80 ants 100 iterations: {best_path5}")

print(f"Best distance found for 80 ants 150 iterations: {best_distance6}")
print(f"Best path found for 80 ants 150 iterations: {best_path6}")

print(f"Best distance found for 120 ants 50 iterations: {best_distance7}")
print(f"Best path found for 120 ants 50 iterations: {best_path7}")

print(f"Best distance found for 120 ants 100 iterations: {best_distance8}")
print(f"Best path found for 120 ants 100 iterations: {best_path8}")

print(f"Best distance found for 120 ants 150 iterations: {best_distance9}")
print(f"Best path found for 120 ants 150 iterations: {best_path9}")

