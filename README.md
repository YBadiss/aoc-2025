# AoC 2025

https://adventofcode.com/2025

![Final AoC tree](./aoc.gif)

## Getting started

```bash
uv init
./main.py --help
./main.py 1a  # run day 1, part 1 (a)
./main.py -t 1b  # test day 1, part 2 (b)
```

## Solving a new day `x`

1. Create a new folder called `day-<x>`
2. Add your input data as `day-<x>/data`
3. Make the folder `day-<x>` into a python module that exposes
    1. `delimiter`: the delimiter to use to split the input data into individual items
    2. `parser`: a function that parses each individual item and returns an equivalent dataclass
    3. `solver_<y>`: functions accepting a list of dataclass items and returning the result for part `y`
4. For each part of the day
    1. Expose a function `solver_<y>` accepting a list of dataclass items and returning the result this part
    2. Add the test input data as `day-<x>/<y>.data.test`, with an extra `delimiter` separated item at the end containing only the expected result
    3. Run `./main.py -t <x><y>` to run your solution against your test data
    4. Run `./main.py <x><y>` to get the result for the main data
