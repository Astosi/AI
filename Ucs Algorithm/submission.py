import csv
from queue import PriorityQueue
from io import open
import os

FILE_PATH = os.getcwd() + "\cities.csv"

cities = {}


class CityNotFoundError(Exception):
    def __init__(self, city):
        print("%s does not exist" % city)

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}        

def build_graph(path):
    
    with open(FILE_PATH,"r", encoding="UTF-8") as file:
        
        reader = csv.reader(file)
        next(reader)

        for line in reader:
        
            city1 = line[0].lower()
            city2 = line[1].lower()
            
            weight = line[2]

            if city1 not in cities:
                cities[city1] = Node(city1)
            
            if city2 not in cities:
                cities[city2] = Node(city2)
            
            cities[city1].neighbors[city2] = int(weight)
            cities[city2].neighbors[city1] = int(weight)


def uniform_cost_search(graph, start, end):
  
    if start not in cities:
        raise CityNotFoundError(start)
    if end not in cities:
        raise CityNotFoundError(end)

    visited = set()
    queue = PriorityQueue()
    
    queue.put((0, start, [start]))

    while queue:

        cost, current, route = queue.get()

        if current not in visited:
            visited.add(current)

            if current == end:
                print("From city "+start+" to "+end+",the shortest route is: ")
                print(" -> ".join(route))
                print("With cost of", cost, "unit distance.\n")
                return

            neighbors = cities[current].neighbors

            for city in neighbors: 

                if city not in visited:

                    total_cost = cost + neighbors[city]
                    queue.put((total_cost, cities[city].name, route + [cities[city].name]))


if __name__ == "__main__":
    
    build_graph(FILE_PATH)

    while True:
        try:
            print("Please write exit to terminate the program.\n") 
            
            departure = input("Please enter the city of departure:").lower()
            
            if departure == 'exit':
                print("Program is terminated!")
                break
            
            arrival = input("Please enter the city of arrival:").lower()

            if arrival == 'exit':
                print("Program is terminated!")
                break

            uniform_cost_search(cities, departure, arrival)
      
        except CityNotFoundError:
            print("City could not be found.")