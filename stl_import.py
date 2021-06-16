def edge_verticies(verticies):
    n = 0
    edges = []
    for i in range(int(len(verticies) / 3)):
        edges.append((n, n + 1))
        edges.append((n, n + 2))
        edges.append((n + 1, n + 2))

        n += 3
    return edges


def stl_verticies_edges(file_name):
    f = open(file_name, "r")
    verticies = []
    for line in f:
        line = line.strip()
        if line[0] == 'v':
            verticies.append((float(line[7:19]), float(line[20:32]), float(line[33:45])))
    f.close()
    edges = edge_verticies(verticies)

    return verticies, edges
