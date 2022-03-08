import igraph
import numpy as np
from utils import write_renumbering


def random(filepath, graph):

    vertices = igraph.VertexSeq(graph)
    random_list = np.random.choice(len(vertices), len(vertices))
    random_vertices = [vertices[i] for i in random_list]

    # Renumbering
    renumbering = np.zeros(len(vertices), dtype=int)

    for i in range(len(random_vertices)):
        renumbering[random_list[i]] = i

    # Write renumbering
    write_renumbering(filepath, graph, renumbering)