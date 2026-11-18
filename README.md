# ParkSmart — Smart Parking Allocation and Reservation Platform

**C11 algorithm engine + Python Tkinter GUI**. Python is only the GUI adapter; parking logic, reservations, routing, matching, and benchmarks are implemented in C.

## Quick start

Requires GCC and Python 3 with Tkinter. No pip packages required.

### Linux / macOS
```sh
make
python3 gui/app.py
```

### Windows (MinGW GCC)
```powershell
gcc -std=c11 -O2 -Wall -Wextra -Iinclude src/main.c src/core.c src/algorithms.c -o parksmart.exe
python gui/app.py
```

Run the GUI from the project folder. The app initializes sample parking spaces and roads when no spaces.csv exists; reservations and occupancy are saved in `data/`.

## CLI examples
```sh
./parksmart list
./parksmart nearest 0 10 12
./parksmart reserve 1 Alex 10 12
./parksmart cancel 1
./parksmart compare 0,1,2,3,4,5 10 12
./parksmart demo
./parksmart benchmark
```

## Core design
- **Dijkstra**: shortest road distance from a driver node to a lot.
- **Greedy**: sequential nearest-feasible allocation.
- **Exact min-cost max-flow**: maximum number of assignments, then minimum total travel distance for up to 32 drivers and 128 parking units.
- **Reservation validation**: half-open time intervals `[start,end)`, per-lot capacity, driver name checks, cancellation.
- **Additional C algorithms**: merge/quick sort, binary search (recursive/iterative), naive/KMP/Rabin-Karp text search, Kadane maximum subarray, fast power, knapsack, LCS, N-Queens, subset sum, CRT pair, Prim/Kruskal, Bellman-Ford, Floyd-Warshall, bounded exact TSP, bipartite matching, Ford-Fulkerson.

## Limitations / next engineering milestones
This is a functional **hackathon MVP**, not a production parking payment system. Hour values are integer simulation slots (not real timestamps). It is single-process, CSV persistence is not transactional, there is no authentication or payment integration, and the additional algorithm library is not yet exposed in the GUI. Maximum driver count for exact allocation is 32. More syllabus-specific algorithms (Strassen, interval partitioning, Huffman, optimal BST, matrix chain, activity selection, finite automaton matching, celebrity discovery, and branch-and-bound variants) remain to be added for full 8-week rubric coverage.

## Data model
`spaces.csv`: id,node,capacity,occupied,rate,active,name. `roads.csv`: from,to,distance (undirected). `reservations.csv`: id,space_id,start,end,active,driver.

## Demo narrative
1. **Normal:** show nearest parking and compare greedy vs exact allocation.
2. **Shock:** temporarily disable the first four lots in memory, then rerun the comparison.
3. **Stress:** allocate 32 drivers to the remaining capacity and compare assignment count, travel distance, and CPU time.

See `docs/ALGORITHMS.md` for complexity and verification.
