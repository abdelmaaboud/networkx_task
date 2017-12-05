import networkx as nx
import matplotlib.pyplot as plt

# Build the corresponding network (G) with Networkx
from networkx.algorithms.distance_measures import diameter

G = nx.readwrite.edgelist.read_weighted_edgelist("CE-LC.txt")

# What are the number of nodes, number of edges and the average degree of the network
number_of_edges = G.number_of_edges()
number_of_nodes = G.number_of_nodes()
average_degree_connectivity = nx.average_degree_connectivity(G)
print "number of edges : %s"%  number_of_edges
print "number of nodes : %s"% number_of_nodes
print "average degree of the network : %s"% average_degree_connectivity

density = nx.density(G)
# What is the density of the network.
print "density of the network : %s"% density


# Find the minimum spanning tree in G and draw it.
T=  nx.minimum_spanning_tree(G)

#draw minimum_spanning_tree
nx.draw_networkx(T, with_labels=False, node_size = 15)
plt.title("minimum_spanning_tree")
plt.savefig("minimum_spanning_tree.png")

plt.show()

#nx.degree_histogram(G)

# Find LC
Lc = max(nx.connected_component_subgraphs(G), key=len)

nx.draw(Lc,with_labels=False, node_size = 15)
plt.title("largest connected component of the network")
plt.savefig("largest connected component.png")

plt.show()

print "----LC----"
Lc_diameter = nx.diameter(Lc)
Lc_center = nx.center(Lc)
print "diameter : %s"% Lc_diameter
print "center : %s"% Lc_center

# number of clique communities with 3 nodes
all_cliques = nx.find_cliques(Lc)
cliques = [clique for clique in all_cliques if len(clique) == 3]
cliques_len= len(cliques)
print "number of clique communities with 3 nodes : %s"% cliques_len


#write report.txt to answer some questions

report = open("report.txt",'w')
report.write("number of edges : %s\n"% number_of_edges)
report.write("number of nodes : %s\n"% number_of_nodes)
report.write("average degree of the network : %s\n"% average_degree_connectivity)

report.write( "density of the network : %s\n"% density)
report.write("---the largest connected component of the network  (LC) --\n")
report.write("diameter  : %s\n"% Lc_diameter)

report.write("center  : %s\n"% Lc_center)

report.write("number of clique communities with 3 nodes : %s\n"% cliques_len)