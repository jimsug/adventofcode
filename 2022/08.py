from aocd import data
from aocd.models import Puzzle
from numpy import prod

# data = Puzzle(year=2022, day=8).example_data
print(data)
tree_grid = [[t for t in l]for l in data.split("\n") ]
max_score = 0
visible_count = (len(tree_grid)-1)*4
for i in range(1, len(tree_grid)-1):
    for j in range(1, len(tree_grid[i])-1):
        this_tree = int(tree_grid[i][j])
        up_trees = [int(l[j]) for l in tree_grid[:i]]
        down_trees = [int(l[j]) for l in tree_grid[i+1:]]
        left_trees = [int(k) for k in tree_grid[i][:j]]
        right_trees = [int(k) for k in tree_grid[i][j+1:]]
        up_trees.reverse()
        left_trees.reverse()

        tree_views = [up_trees, down_trees, left_trees, right_trees]

        if this_tree > min([max(trees) for trees in tree_views]):
            visible_count+=1

        score = [1 for i in range(len(tree_views))]
        for k in range(len(tree_views)):
            trees = tree_views[k]
            l = 1
            while trees[l-1] < this_tree and l < len(trees) :
                score[k] += 1
                l+=1

        max_score = max(max_score, prod(score))

print(visible_count)
print(max_score)