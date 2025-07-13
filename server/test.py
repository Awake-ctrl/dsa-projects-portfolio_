from graph import WeightedGraph

g = WeightedGraph()
users = ['A', 'B', 'C', 'D', 'E']
for u in users:
    g.add_user(u)

# Add weighted interactions
g.add_connection('A', 'B', 3)  # strong connection
g.add_connection('A', 'C', 1)
g.add_connection('B', 'D', 2)
g.add_connection('C', 'D', 1)
g.add_connection('C', 'E', 1)

print("Top suggestions for A:")
print(g.get_weighted_suggestions("A"))
