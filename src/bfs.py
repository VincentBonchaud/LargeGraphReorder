import igraph
import numpy as np
from utils import write_renumbering

def bfs(filepath, graph, mode=igraph.ALL, iter_from_root=True, root_mode='MAX'):

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

    # Compute BFS
    bfsiter = graph.bfsiter(root.index, mode=mode)

    # Iter BFS & Renumbering
    renumbering = np.zeros(len(vertices), dtype=int)
    v = next(bfsiter)
    i = 0

    try:
        if iter_from_root:
            while v is not None:
                renumbering[v.index] = i
                v = next(bfsiter)
                i += 1
        else:
            while v is not None:
                renumbering[v.index] = len(renumbering) - 1 - i
                v = next(bfsiter)
                i += 1
    except StopIteration:
        pass

    # Write renumbering
    write_renumbering(filepath, graph, renumbering)

