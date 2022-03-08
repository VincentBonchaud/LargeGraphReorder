import igraph
import time
import settings
from tqdm import tqdm
from contextlib import contextmanager
from optparse import OptionParser

def load_graph(file_path, has_node_degrees=False):
    """
        Load igraph graph from file_path.
        has_node_degree allow to skip graph header in certain file formats.
    """
    g = igraph.Graph()

    with open(file_path, 'r') as f:
        nb_vertices = int(f.readline())
        g.add_vertices(nb_vertices)

        # Skip nb_vertices lines in case the graph format includes nodes degrees
        if has_node_degrees:
            line = ''
            for i in range(nb_vertices):
                f.readline()

        loaded_edges = 0
        line = f.readline()

        # Load graph with batch to not saturate memory
        while True:
            n = 10000000

            lines = [f.readline().strip().split() for i in range(n)]

            edges = [(int(vertices[0]), int(vertices[1])) for vertices in lines if vertices]
            g.add_edges(edges)

            loaded_edges += n
            print(loaded_edges)

            if len(lines) != len(edges):
                break

    return g


@contextmanager
def time_context(name):
    """
        Context to time actions computed within the context
    """

    print('[{}] Started..'.format(name))
    startTime = time.time()
    yield
    elapsedTime = time.time() - startTime
    print('[{}] finished in {} ms'.format(name, int(elapsedTime * 1000)))

    settings.ELAPSED_TIME_LAST_TIME_CONTEXT = int(elapsedTime * 1000)


def write_renumbering(filepath, graph, renumbering):
    """
        Write renumbering of graph in filepath, based on list renumbering
    """

    vertices = igraph.VertexSeq(graph)
    vid_is_visited = [0 for vid in range(len(renumbering))]

    with open(filepath, 'w+') as file:
        file.write('{}\n'.format(graph.vcount()))

        for v in tqdm(vertices):        
            for n_id in graph.neighbors(v.index):
                # Avoid writing the same edge twice
                if not vid_is_visited[n_id]:
                    file.write('{} {}\n'.format(renumbering[v.index], renumbering[n_id]))

            vid_is_visited[v.index] = 1


def parse_args():
    """
        Parse option of the program
    """

    parser = OptionParser(usage="usage: %prog [options]")

    parser.add_option("-r", "--renumbering",
                      action="store",
                      dest="renumbering",
                      default=False,
                      help="the kind of renumbering to compute")

    parser.add_option("-d", "--file-has-header",
                      action="store_true",
                      dest="has_degrees_header",
                      default=False,
                      help="skip graph file header")

    parser.add_option("-l", "--louvain",
                      action="store_true",
                      dest="louvain",
                      default=False,
                      help="compute louvain on given graph")

    parser.add_option("-f", "--filepath",
                      action="store",
                      dest="filepath",
                      default="default.graph",
                      help="graph file to load")

    parser.add_option("-o", "--logfile",
                      action="store",
                      dest="logfile",
                      default="log.txt",
                      help="log file to write to")

    parser.add_option("-g", "--graphfile",
                      action="store",
                      dest="graphfile",
                      default="default.graph",
                      help="new graph file to write after renumbering")

    return parser.parse_args()