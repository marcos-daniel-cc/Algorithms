class Graph: 
   
  n = 0
  
      
  g =[[0 for x in range(10)] for y in range(10)] 
       
     # constructor 
  def __init__(self, x): 
    self.n = x 
  
    for i in range(0, self.n): 
      for j in range(0, self.n): 
        self.g[i][j]= 0
                
                
  def displayAdjacencyMatrix(self): 
    print("\n\n Adjacency Matrix:", end ="") 
          
        
    for i in range(0, self.n): 
      print() 
      for j in range(0, self.n): 
        print("", self.g[i][j], end ="") 
                
        
        
  def addEdge(self, x, y): 
   
    if(x>= self.n) or (y >= self.n): 
      print("Vertex does not exists !") 
   
    if(x == y): 
      print("Same Vertex !") 
    else: 
      self.g[y][x]= 1
      self.g[x][y]= 1
             
             
  

             
             
  def addVertex(self): 
    self.n = self.n + 1; 
           
    for i in range(0, self.n): 
      self.g[i][self.n-1]= 0
      self.g[self.n-1][i]= 0
             
             
             
                        
  def removeVertex(self, x):
    if(x>self.n): 
      print("Vertex not present !") 
    else: 
		
      while(x<self.n): 
			 
        for i in range(0, self.n): 
          self.g[i][x]= self.g[i][x + 1] 
			
			 
        for i in range(0, self.n): 
          self.g[x][i]= self.g[x + 1][i] 
         
        x = x + 1
 
      self.n = self.n - 1




obj = Graph(4); 
       

obj.addEdge(0, 1); 
obj.addEdge(0, 2); 
obj.addEdge(1, 2); 
obj.addEdge(2, 3); 
 
obj.displayAdjacencyMatrix(); 
   
 
obj.addVertex(); 
 
obj.addEdge(4, 1); 
obj.addEdge(4, 3); 

obj.displayAdjacencyMatrix(); 
       

obj.removeVertex(1);  
obj.displayAdjacencyMatrix(); 