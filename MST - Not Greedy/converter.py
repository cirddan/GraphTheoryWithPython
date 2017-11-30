def matrix_to_list(adj_matrix):
    """Converts Adjacency Matrix of graph to it's Adjacency List"""

    adj_list = {}
    for i, node in enumerate(adj_matrix):
        node_adj = []
        for j, connected_to in enumerate(node):
            if connected_to != 'inf' and connected_to != '0':
                node_adj.append((j, connected_to))
                adj_list[i] = node_adj

    return adj_list
