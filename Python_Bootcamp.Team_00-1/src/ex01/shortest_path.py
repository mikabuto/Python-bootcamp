import json
import os
import sys

file_dir = os.path.dirname(__file__)
file_name = os.path.join(file_dir, '../../misc/wiki.json')
with open(file_name) as f:
	json_file = f.read()
	json_data = json.loads(json_file)

# json_data = {
#     "a": ["b", "e"],
#     "b": ["a", "f", "e"],
#     "c": ["a", "b", "d"],
#     "d": ["c"],
#     "e": ["c"],
#     "f": ["d"]
# }
 
 
def make_tree_non_directed(src: str, parent: str = None, visited=set()) -> list:
    if parent and parent not in json_data[src]:
        json_data[src].append(parent)
    if src not in visited:
        visited.add(src)
        # print(src, '<-', parent)
        for node in json_data[src]:
            make_tree_non_directed(node, src)
 
 
def tree_traversal(src: str, dest: str, visited=set()) -> list:
    res = []
    if src == dest:
        return [[src]]
    if src not in visited:
        visited.add(src)
        if dest in json_data.get(src, []):
            res += [[dest]]
        else:
            for node in json_data.get(src, []):
                node_res = tree_traversal(node, dest)
                for path in node_res:
                    path.append(node)
                res += node_res
    return res
 
 
def find_the_best(arr: list) -> tuple:
    if arr:
        size = len(arr[0])
        res = arr[0]
        for i, path in enumerate(arr):
            if len(path) < size:
                size = len(path)
                res = path
        return size, res
    return 0, []
 
 
def create_response(src: str, dest: str, print_path=False, non_directed=False) -> None:
    if non_directed:
        make_tree_non_directed(src)
    res = tree_traversal(src, dest)
    size, path = find_the_best(res)
    if size:
        if print_path:
            print(src, "->", " -> ".join(path[::-1]))
        print(size)
    else:
        print("Path not found")
 
 
def get_params():
    src = ""
    dest = ""
    v = False
    non_directed = False
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "--from":
            src = sys.argv[i+1]
        elif sys.argv[i] == "--to":
            dest = sys.argv[i+1]
        elif sys.argv[i] == "--non-directed":
            non_directed = True
        elif sys.argv[i] == "-v":
            v = True
    return src, dest, v, non_directed
 
 
def main():
    if 4 < len(sys.argv) < 8:
        src, dest, v, non_directed = get_params()
 
        if src in json_data and dest in json_data:
            create_response(src, dest, print_path=v, non_directed=non_directed)
        else:
            print("Path not found")
    else:
        print("Error number of arguments")
 
 
if __name__ == '__main__':
    main()