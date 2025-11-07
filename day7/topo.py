if __name__ == '__main__':
    with open('input') as f:
        instructions = f.readlines()
    graph = {}
    adj_list = []
    for i in instructions:
        l,r = i.strip().split(' -> ')
        if l.isnumeric():
            graph[r] = ([],int(l))
        elif l.count('AND') or l.count('OR'):
            a,_,b = l.split()
            if a.isnumeric():
                graph[r] = ([[b,r]],l)
            else:
                graph[r] = ([[a,r],[b,r]],l)
        elif l.count('SHIFT'):
            a,_,__ = l.split()
            graph[r] = ([[a,r]],l)
        elif l.count('NOT'):
            _,a = l.split()
            graph[r] = ([[a,r]],l)
        else:
            graph[r] = ([[l,r]],l)

    def topo_sort(graph):
        def get_incoming_edge_count(edgelist, vertex):
            edge_count = 0
            for e in edgelist:
                if e[1] == vertex:
                    edge_count += 1
            return edge_count
        result_list = []
        no_incoming = []
        remaining_edges = []
        for k,v in graph.items():
            if v[0] == []:
                no_incoming.append(k)
            else:
                remaining_edges += v[0]
        while no_incoming:
            current_v = no_incoming.pop(0)
            outgoing_edges = []
            result_list.append(current_v)
            edges_to_remove = []
            for e in remaining_edges:
                if e[0] == current_v:
                    outgoing_edges.append(e)
                    edges_to_remove.append(e)
            for e in edges_to_remove:
                remaining_edges.remove(e)
            for e in outgoing_edges:
                in_count = get_incoming_edge_count(remaining_edges, e[1])
                if in_count == 0:
                    no_incoming.append(e[1])
        return result_list
    
    