class Graph: 
     # number of vertices 
     __n = 0
  
     # adjacency matrix 
     __g =[[0 for x in range(10)] for y in range(10)] 
       
     # constructor 
     def __init__(self, x): 
        self.__n = x 
  
        # initializing each element of the adjacency matrix to zero 
        for i in range(0, self.__n): 
            for j in range(0, self.__n): 
                self.__g[i][j]= 0) 
  
