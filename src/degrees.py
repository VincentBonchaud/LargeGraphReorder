import igraph
import numpy as np
from tqdm import tqdm
from utils import write_renumbering

def degree(filepath, graph, inversed=False):

    # Nodes
    vertices = igraph.VertexSeq(graph)
    sorted_vertices = sorted(vertices, key=lambda v: v.degree(), reverse=inversed)

    # Renumbering
    renumbering = np.zeros(len(vertices), dtype=int)

    for i in range(len(sorted_vertices)):
        renumbering[sorted_vertices[i].index] = i

    # Write renumbering
    write_renumbering(filepath, graph, renumbering)
