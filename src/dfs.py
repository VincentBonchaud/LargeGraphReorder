import igraph
import numpy as np
from utils import write_renumbering


def dfs(filepath, graph, iter_from_root=True, root_mode='MAX'):           

    # Root selection
    vertices = igraph.VertexSeq(graph)
    sorted_vertices = sorted(vertices, key=lambda v: v.degree())

    if root_mode == 'MAX':
        root = sorted_vertices[-1]
    elif root_mode == 'MIN':
        root = sorted_vertices[0]
    elif root_mode == 'MED':
        root = sorted_vertices[len(sorted_vertices) // 2]
    else:
        raise ValueError('Wrong type of root_mode: {}\n'.fromat(root_mode))

    visited_node = [0 for i in range(len(vertices))]  
    visited_node_set = set()

    # DFS
    renumbering = np.zeros(len(vertices), dtype=int)
    stack = [] 
    stack.append(root.index) 
    i = 0 

    while len(stack):  
        node_index = stack[-1]  
        stack.pop() 

        if not visited_node[node_index]:  
            visited_node[node_index] = 1
            renumbering[node_index] = i
            i += 1

        for node in graph.neighbors(node_index):  
            if not visited_node[node]:  
                stack.append(node)  


    # Write renumbering
    write_renumbering(filepath, graph, renumbering)