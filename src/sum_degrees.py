import igraph
import numpy as np
from tqdm import tqdm
from utils import write_renumbering


def sum_degree(filepath, graph, inversed=False, neighbors_treshold=1):

    # Nodes
    degrees = np.zeros(graph.vcount(), dtype=int)
    for vid in range(graph.vcount()):
        degrees[vid] = graph.degree(vid)

    sum_neighbors = np.zeros(graph.vcount(), dtype=int)

    for vid in tqdm(range(len(degrees))):
        d_sum = degrees[vid]

        # Sum neighbors degrees
        for nid in graph.neighbors(vid):
            d_sum += degrees[nid]

        sum_neighbors[vid] = d_sum

    if neighbors_treshold == 2:
        sum_neighbors_2 = np.zeros(graph.vcount(), dtype=int)

        for vid in tqdm(range(len(degrees))):
            d_sum = degrees[vid]

            # Sum neighbors degrees and neighbors of neighbors degrees
            for nid in graph.neighbors(vid):
                d_sum += sum_neighbors[nid]

            sum_neighbors_2[vid] = d_sum

        vertices = [(vid, sum_neighbors_2[vid]) for vid in range(len(sum_neighbors_2))]
    else:
        vertices = [(vid, sum_neighbors[vid]) for vid in range(len(sum_neighbors))]

    sorted_vertices = sorted(vertices, key=lambda v: v[1], reverse=inversed)

    # Renumbering
    renumbering = np.zeros(len(vertices), dtype=int)

    for i in range(len(sorted_vertices)):
        renumbering[sorted_vertices[i][0]] = i

    # Write renumbering
    write_renumbering(filepath, graph, renumbering)
