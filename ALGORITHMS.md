# Algorithms and complexity

| Algorithm | Worst-case time | Extra space | Purpose |
|---|---|---|---|
| Dijkstra (matrix) | O(V^2) | O(V) | Nearest reachable lot |
| Greedy assignment | O(D(V^2 + P + R)) | O(P+V) | Fast baseline |
| Exact min-cost flow | O(F N^3) conservative | O(N^2) | Maximum matching with minimum distance |
| Merge sort | O(n log n) | O(n) | Ordered workloads |
| Quick sort | O(n^2) | O(n) worst recursion | Sorting comparison |
| KMP | O(n+m) | O(m) | Driver/event text |
| Rabin-Karp | O(nm) worst | O(1) | Text search |
| Knapsack | O(nC) | O(C) | Capacity budgeting |
| Floyd-Warshall | O(V^3) | O(V^2) | All-pairs routing |
| TSP exhaustive | O(n!) | O(n) | Small patrol route |
| Ford-Fulkerson (BFS) | O(V E^2) | O(V^2) | Capacity flow |
| N-Queens | exponential | O(n) | Backtracking demonstration |

## Correctness checks
- Adjacent reservation windows do not conflict: `[10,12)` and `[12,14)`.
- Overlapping bookings must never exceed lot capacity.
- Exact allocation must not assign the same unit twice.
- For the same feasible driver set, exact matching cannot allocate fewer drivers than greedy; when counts match, exact travel distance cannot exceed greedy.
- Shortest path lengths are nonnegative and satisfy triangle inequality on connected nodes.

## Benchmark caveats
CPU times vary by machine. Run repeated trials, report medians, and record compiler, flags, and dataset seed. `benchmark` is a small smoke benchmark, not a full empirical study.
