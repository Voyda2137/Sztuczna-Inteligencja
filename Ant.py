import numpy as np

class Ant:
    def __init__(self, num_cities):
        self.num_cities = num_cities
        self.visited = np.zeros(num_cities, dtype=bool)
        self.path = []
        self.total_distance = 0

    def visit_city(self, city):
        self.visited[city] = True
        self.path.append(city)

    def is_visited(self, city):
        return self.visited[city]

def generate_distance_matrix(num_cities):
    distance_matrix = np.random.randint(1, 10, size=(num_cities, num_cities))
    np.fill_diagonal(distance_matrix, 0)
    return distance_matrix

def initialize_pheromone_matrix(num_cities, initial_pheromone):
    return np.ones((num_cities, num_cities)) * initial_pheromone

def ant_colony_optimization(num_ants, num_iterations, num_cities, alpha, beta, rho, initial_pheromone):
    distance_matrix = generate_distance_matrix(num_cities)
    pheromone_matrix = initialize_pheromone_matrix(num_cities, initial_pheromone)
    best_distance = float('inf')
    best_path = []

    for iteration in range(num_iterations):
        ants = [Ant(num_cities) for _ in range(num_ants)]
        for ant in ants:
            ant.visit_city(np.random.randint(0, num_cities))
            while len(ant.path) < num_cities:
                next_city = select_next_city(ant, pheromone_matrix, distance_matrix, alpha, beta)
                ant.visit_city(next_city)
                ant.total_distance += distance_matrix[ant.path[-2]][ant.path[-1]]
            ant.total_distance += distance_matrix[ant.path[-1]][ant.path[0]]

            if ant.total_distance < best_distance:
                best_distance = ant.total_distance
                best_path = ant.path

        update_pheromone_matrix(pheromone_matrix, ants, rho)

        print(f"Iteration {iteration + 1}: Best distance = {best_distance}")

    return best_distance, best_path

def select_next_city(ant, pheromone_matrix, distance_matrix, alpha, beta):
    current_city = ant.path[-1]
    unvisited_cities = np.where(np.logical_not(ant.visited))[0]
    pheromone = pheromone_matrix[current_city, unvisited_cities]
    visibility = 1 / distance_matrix[current_city, unvisited_cities]
    probabilities = np.power(pheromone, alpha) * np.power(visibility, beta)
    probabilities /= np.sum(probabilities)
    next_city = np.random.choice(unvisited_cities, p=probabilities)
    return next_city

def update_pheromone_matrix(pheromone_matrix, ants, rho):
    pheromone_matrix *= (1 - rho)
    for ant in ants:
        delta_pheromone = 1 / ant.total_distance
        for i in range(ant.num_cities):
            city1 = ant.path[i]
            city2 = ant.path[(i + 1) % ant.num_cities]
            pheromone_matrix[city1, city2] += delta_pheromone


