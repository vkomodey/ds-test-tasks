G = [
    [0, 2, 1, 4, None, 4],
    [2, 0, None, 7, 2.5, None],
    [1, None, 0, 5, 1, None],
    [4, 7, 5, 0, None, 5],
    [None, 2.5, 1, None, 0, 1],
    [4, None, None, 5, 1, 0],
]

def Vertex(index, label=float('inf'), visited=False):
    return {
        "label": label,
        "visited": visited,
        "index": index,
        "prev": None
    }

start = 0
finish = 5

vertexes = [Vertex(i) for i in range(len(G))]
vertexes_len = len(vertexes)

active_index = start
vertexes[0]["label"] = 0

while True:
    min_unvisited = -1
    min_label = float('inf')

    for i in range(vertexes_len):
        vertex = vertexes[i]

        if vertex["visited"] == True:
            continue

        if vertex["label"] < min_label:
            min_unvisited = i
            min_label = vertex["label"]

    neighbors = G[min_unvisited]

    for j in range(vertexes_len):
        if vertexes[j]["visited"] == True:
            continue

        vertex_len = neighbors[j]
        if vertex_len == None:
            continue

        sum_label = min_label + vertex_len

        if sum_label < vertexes[j]["label"]:
            vertexes[j]["label"] = sum_label
            vertexes[j]["prev"] = min_unvisited

    vertexes[min_unvisited]["visited"] = True
    
    if min_unvisited == finish:
        break


index = 0
curr_vertex = vertexes[finish]
prev_v_index = curr_vertex["prev"]

path = [finish]

while True:
    path = [prev_v_index] + path
    if prev_v_index == start:
        break
    curr_vertex = vertexes[prev_v_index]
    prev_v_index = curr_vertex["prev"]

print(path)
