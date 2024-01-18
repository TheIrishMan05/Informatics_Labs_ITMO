import timeit


def space_count(str):
     return len(str) - len(str.lstrip())


def gr_parser(file_in, file_out, max_space):
    root = {}
    hierarchy = []
    with open(file_in, "r", encoding="utf-8") as f_in:
        buffer = f_in.readlines()
    buffer.remove(buffer[0])
    for i in buffer:
        key, value = i.split(':', 1)
        layer, key = space_count(key) // max_space, key.lstrip()
        hierarchy.insert(layer, key)
        while hierarchy[-1] != key:
            hierarchy.pop()
        if value == "\n":
            current_tree = root
            for node in hierarchy:
                if node in current_tree:
                    current_tree = current_tree[node]
                else:
                    current_tree[node] = {}
        else:
            current_tree = root
            for node in hierarchy:
                if node in current_tree:
                    current_tree = current_tree[node]
                else:
                    current_tree[node] = value.strip()

    ans = str(root).replace("\'", '\"')
    with open(file_out, "w", encoding="utf-8") as f_out:
        f_out.write(ans)


time_addtask3 = 0
for k in range(100):
    gr_parser(r'../task3/invoice.yaml', r'invoice.json', 4)
    time_addtask3 += timeit.timeit()
print(str(time_addtask3) + " - addtask3")

