
from Ant import ant_colony_optimization

num_ants = 10
num_iterations = 100
num_cities = 50
alpha = 1
beta = 2
rho = 0.1
initial_pheromone = 0.1

best_distance, best_path = ant_colony_optimization(num_ants, num_iterations, num_cities, alpha, beta, rho, initial_pheromone)

if best_distance is not None:
    print(f"Best distance found: {best_distance}")
    print(f"Best path found: {best_path}")