
import search

ab = search.GPSProblem('G', 'O', search.romania)


print("ANCHURA")
print( search.breadth_first_graph_search(ab).path())
print("\n")

print("DEEP")
print(search.depth_first_graph_search(ab).path())
print("\n")

print("BRANCH AND BOUND")
print(search.cost_graph_search(ab).path())
print("\n")

print("BRANCH AND BOUND con Subestimacion")
print(search.heuristic_graph_search(ab).path())
print("\n")



# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

