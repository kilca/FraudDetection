import sys

# appending a path
sys.path.append('fraudar-master')

import fraudar
graph = fraudar.ReviewGraph(6, fraudar.aveDegree)


graph = fraudar.ReviewGraph(6, fraudar.aveDegree)

# Create reviewers and products.
reviewers = [graph.new_reviewer("reviewer-{0}".format(i)) for i in range(2)]
products = [graph.new_product("product-{0}".format(i)) for i in range(3)]

# Add reviews.
graph.add_review(reviewers[0], products[0], 0.2)
graph.add_review(reviewers[0], products[1], 0.9)
graph.add_review(reviewers[0], products[2], 0.6)
graph.add_review(reviewers[1], products[0], 0.1)
graph.add_review(reviewers[1], products[1], 0.7)

# Run the algorithm.
graph.update()

print("Anomalous reviewers.")
for r in graph.reviewers:
  if r.anomalous_score == 1:
    print(r.name)

# Print summarized rating scores.
print("Summaries.")
for p in graph.products:
    print(p.name, p.summary)