#tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
start = 'JFK'
#end = 'SJC'
end = 'SFO'


class Node:
    def __init__(self, ticket, level=0):
        self.ticket = ticket
        self.start = ticket[0]
        self.end = ticket[1]
        self.level = level


stack = []
iter = []


def find_tickets(start, used_tickets):
    results = []
    for t in tickets:
        if t[0] == start and t not in used_tickets:
            results.append(t)
    return sorted(results, key=lambda t: t[1], reverse=True)


def print_iter():
    print([n.ticket for n in iter])


# initial stack
valid = find_tickets(start, [])
stack.extend([Node(t, 0) for t in valid])

# iterate
while len(stack) > 0:
    current_node = stack.pop()
    if current_node.end == end and len(iter) == len(tickets) - 1:
        iter.append(current_node)
        print_iter()
        break
    else:
        used_tickets = [n.ticket for n in iter[:current_node.level]]
        next_valid = find_tickets(current_node.end, used_tickets)
        if len(next_valid) > 0:
            iter.append(current_node)
            for t in next_valid:
                stack.append(Node(t, current_node.level + 1))


def version_1():

    class Node:
        def __init__(self, loc, level = 0):
            self.loc = loc
            self.level = level

    # 1. build hash table for quick search
    mapping = {}
    for t in tickets:
        dest = mapping.get(t[0], [])
        dest.append(t[1])
        dest.sort(reverse=True)
        mapping[t[0]] = dest
    print(mapping)

    # 2. iterate dfs
    stack = []
    iter = []
    stack.append(Node(start))
    while len(stack) > 0:
        node = stack.pop()
        if node.loc == end and node.level == len(tickets) - 1:
            # found
            iter = iter[:node.level] + [node.loc]
            print(iter)
            break
        else:
            dest = mapping.get(node.loc, [])
            visited = set([(iter[i], iter[i+1]) for i in range(node.level - 1)])
            found = False
            for d in dest:
                if not (node.loc, d) in visited:
                    found = True
                    stack.append(Node(d, node.level + 1))
            if found:
                iter = iter[:node.level] + [node.loc]
