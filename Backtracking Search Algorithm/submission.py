import plotly.express as px
import pandas as pd
import plotly.io as pio
import numpy as np
pio.renderers.default='browser'

# Do not modify the line below.
countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]

# Do not modify the line below.
colors = ["blue", "green", "red", "yellow"]

graph = {"Argentina" : {'Bolivia','Chile','Paraguay','Uruguay','Brazil'},
         "Bolivia" : {'Argentina', 'Brazil', 'Chile', 'Paraguay', 'Peru'},
         "Brazil" : {'Argentina', 'Bolivia', 'Colombia', 'Guyana', 'Paraguay', 'Peru',
                     'Suriname', 'Uruguay', 'Venezuela'},
         "Chile" : {'Argentina', 'Bolivia', 'Peru'},
         "Colombia" : {'Brazil', 'Ecuador', 'Peru', 'Venezuela'},
         "Ecuador": {'Colombia', 'Peru'},
         "Falkland Islands" : {"Falkland Islands"},
         "Guyana" : {'Brazil', 'Suriname', 'Venezuela'},
         "Paraguay" : {'Argentina', 'Bolivia', 'Brazil'},
         "Peru" : {'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador'},
         "Suriname" : {'Brazil', 'Guyana'},
         "Uruguay" : {'Argentina', 'Brazil'},
         "Venezuela" : {'Brazil', 'Colombia', 'Guyana'}}

newcolor=[]

graph = {k: [v.strip() for v in vs] for k, vs in graph.items()}
edges = {(k,v) for k, vs in graph.items() for v in vs}        
df = pd.DataFrame(edges)
border_matrix = pd.crosstab(df[0], df[1])
Matrix=np.array(border_matrix)


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]\
                            for row in range(vertices)]

    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    def graphColourUtil(self, m, colour, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1) == True:
                    return True
                colour[v] = 0

    def graphColouring(self, m):
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 0) == None:
            return False

        # Print the solution
        print ("Result:")
        
        for c in colour:   
            if c==1:
                blue="blue"
                print(blue)
                newcolor.append(blue)
            
            elif c==2:
                red="red"
                print("red")
                newcolor.append(red)
                
            elif c==3:
                yellow="yellow"
                print(yellow)
                newcolor.append(yellow)
          
            else:
                green="green"
                print(green)
                newcolor.append(green)

        return True


# Do not modify this method, only call it with an appropriate argument.
# colormap should be a dictionary having countries as keys and colors as values.
def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    fig.show()


# Implement main to call necessary functions
if __name__ == "__main__":   
       
   
    # coloring test
    colormap_test = {"Argentina": "blue", 
                     "Bolivia": "red", 
                     "Brazil": "yellow", 
                     "Chile": "yellow", 
                     "Colombia": "red",
                     "Ecuador": "yellow", 
                     "Falkland Islands": "yellow", 
                     "Guyana": "red", 
                     "Paraguay": "green",
                     "Peru": "green", 
                     "Suriname": "green", 
                     "Uruguay": "red", 
                     "Venezuela": "green"}
    
    g = Graph(13)
    g.graph =Matrix
    m = len(colors)
    g.graphColouring(m)
    
    my_dict = {k: v for k, v in zip(countries, newcolor)}
    plot_choropleth(my_dict)
    

    
    
    
