import louvain
import settings
from bfs import bfs
from degrees import degree
from dfs import dfs
from rand import random
from sum_degrees import sum_degree
from utils import time_context, \
                  parse_args,   \
                  load_graph

if __name__ == '__main__':

    (options, args) = parse_args()

    with time_context('loading function'):
        graph = load_graph(options.filepath, options.has_degrees_header)
    
    # Renumbering
    if options.renumbering == 'BFS_MAX_ROOT':
        bfs(options.graphfile, graph, root_mode='MAX')
    elif options.renumbering == 'BFS_MIN_ROOT':
        bfs(options.graphfile, graph, root_mode='MIN')
    elif options.renumbering == 'BFS_MED_ROOT':
        bfs(options.graphfile, graph, root_mode='MED')

    elif options.renumbering == 'BFS_MAX_LEAF':
        bfs(options.graphfile, graph, iter_from_root=False, root_mode='MAX')
    elif options.renumbering == 'BFS_MIN_LEAF':
        bfs(options.graphfile, graph, iter_from_root=False, root_mode='MIN')
    elif options.renumbering == 'BFS_MED_LEAF':
        bfs(options.graphfile, graph, iter_from_root=False, root_mode='MED')

    elif options.renumbering == 'DEG':
        degree(options.graphfile, graph)
    elif options.renumbering == 'DEG_INV':
        degree(options.graphfile, graph, inversed=True)

    elif options.renumbering == 'SUM_DEG':
        sum_degree(options.graphfile, graph)
    elif options.renumbering == 'SUM_DEG_INV':
        sum_degree(options.graphfile, graph, inversed=True)
    elif options.renumbering == 'SUM_DEG_2':
        sum_degree(options.graphfile, graph, neighbors_treshold=2)
    elif options.renumbering == 'SUM_DEG_INV_2':
        sum_degree(options.graphfile, graph, inversed=True, neighbors_treshold=2)

    elif options.renumbering == 'RAN':
        random(options.graphfile, graph)

    elif options.renumbering == 'DFS_MAX_ROOT':
        dfs(options.graphfile, graph, root_mode='MAX')
    elif options.renumbering == 'DFS_MIN_ROOT':
        dfs(options.graphfile, graph, root_mode='MIN')
    elif options.renumbering == 'DFS_MED_ROOT':
        dfs(options.graphfile, graph, root_mode='MED')


    # Louvain
    if options.louvain:
        with time_context('louvain'):
            partition = louvain.find_partition(graph, louvain.ModularityVertexPartition);

        print("Edge count: {}\nVertice count: {}".format(graph.ecount(), graph.vcount()))
        print("Modularity: {}\n{}".format(partition.modularity, partition.summary()))

        # Log writing
        with open(options.logfile, 'w+') as f:
            f.write("Graph loaded from: {}\n".format(options.filepath))
            f.write("Edge count: {}\nVertice count: {}\n".format(graph.ecount(), graph.vcount()))
            f.write("Louvain results:\n - Modularity: {}\n".format(partition.modularity))
            f.write(" - {}\n".format(partition.summary()))
            f.write(" - Computed in {} ms\n".format(settings.ELAPSED_TIME_LAST_TIME_CONTEXT))