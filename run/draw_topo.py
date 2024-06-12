import json
import networkx as nx
import matplotlib.pyplot as plt
import argparse
import os

# Set up argument parser
parser = argparse.ArgumentParser(description="Draw network topology from a JSON file.")
parser.add_argument('--topo', type=str, required=True, help="Path to the JSON file containing the topology.")

# Parse arguments
args = parser.parse_args()

# Extract base name from input file
base_name = os.path.splitext(os.path.basename(args.topo))[0]

# Load the JSON data
with open(args.topo) as f:
    data = json.load(f)

# Create a directed graph
G = nx.DiGraph()

# Add nodes
for node in data['nodes']:
    G.add_node(node['id'])

# Add edges with capacity as a weight
for link in data['links']:
    G.add_edge(link['source'], link['target'], capacity=link['capacity'])

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes

# Draw the nodes
nx.draw_networkx_nodes(G, pos)

# Draw the edges
nx.draw_networkx_edges(G, pos, edgelist=G.edges, arrowstyle='-|>')

# Draw the node labels
# nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

# Draw the edge labels with capacities
# edge_labels = nx.get_edge_attributes(G, 'capacity')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Set plot title
plt.title("Network Topology")

# Create figures directory if it doesn't exist
figures_dir = "result/figures"
if not os.path.exists(figures_dir):
    os.makedirs(figures_dir)

# Save the plot as a PNG file
png_path = os.path.join(figures_dir, f"{base_name}_topology.png")
plt.savefig(png_path)

# Save the plot as a PDF file
pdf_path = os.path.join(figures_dir, f"{base_name}_topology.pdf")
plt.savefig(pdf_path)

# Show the plot
plt.show()
