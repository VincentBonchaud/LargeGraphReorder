# LargeGraphReorder

The goal of this project is to allow the user to either reorder graph's nodes indexes, or execute Louvain algorithm.
In order to do so, you have to execute the 'main.py' file, in the src folder.

There's multiple options to this program:
- '--help' will display program options.
- '-r RENUM' will reorder nodes of the given graph, following RENUM reordering.
- '-d' specify if the graph file has a header of nodes degrees.
- '-f FILE' specify the file from which the graph will be load.
- '-l' execute Louvain algorithm.
- '-o FILE' will store Louvain output into a logfile.
- '-g FILE' specify the file where reodered graph should be written.

There's also a bash file named compute_graph.sh that can be used to execute all possible reordering
and Louvain computation of a graph.
