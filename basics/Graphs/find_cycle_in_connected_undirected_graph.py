class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # if there is cycle number of edges = number of nodes 
        # in a A tree - no of edges is one less than the number of nodes 
       
        #every node is it's own parent
        parent = [i for i in range(len(edges) + 1)]

        #every node has a rank one
        rank = [1] * (len(edges) + 1)

        def find(v):
            #find the parent
            #find the ultimate parent - path compression 
            if v == parent[v]:
                return v
            parent[v] = find(parent[v])
            return parent[v]
        def union(v1, v2):
            p1, p2 = find(v1), find(v2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

        for v1, v2 in edges:
            if union(v1,v2)==False:
                return [v1,v2]
    

            