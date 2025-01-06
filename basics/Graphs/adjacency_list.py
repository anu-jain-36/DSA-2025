class Graph:
    def __init__(self,size):
        self.size = size
        self.adj_matrix=[[0]* size for _ in range(size)]
        self.vertex_info= ['']*size
    
    def edge_info(self,i, j):
        if 0 <= i< self.size and 0 <= j < self.size:
            self.adj_matrix[i][j] = 1
            self.adj_matrix[j][i] = 1
    
    def add_vertex_info(self, vertex, data):
        if 0 <= vertex < self.size:
            # print("data is",data)
            self.vertex_info[vertex] = data


    def print_graph(self):
        # print("anu")
        print(self.adj_matrix)
        for row in self.adj_matrix:
            # print(row)
            print(' '.join(map(str,row)))
        for i in range(self.size):
            print(self.vertex_info[i],":",end=" ")
            for j in range(self.size):
                if self.adj_matrix[i][j]:
                    print(self.vertex_info[j],end=" ")
            print()

def main():
    g=Graph(4)
    g.add_vertex_info(0,'A')
    g.add_vertex_info(1,'B')
    g.add_vertex_info(2,'C')
    g.add_vertex_info(3,'D')
    g.edge_info(0,1)
    g.edge_info(1,2)
    g.edge_info(2,3)
    g.edge_info(3,0)
    g.print_graph()


if __name__=="__main__":
    main()