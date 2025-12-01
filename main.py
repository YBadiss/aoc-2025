#!/usr/bin/env -S uv --quiet run --script
import argparse
from lib import DayModule

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='AoC-2025',
        description='Solving Advent of Code 2025'
    )
    parser.add_argument('day')
    parser.add_argument('-t', '--test', action='store_true')
    args = parser.parse_args()

    day_module = DayModule(args.day)
    try:
        result = day_module.test() if args.test else day_module.run()
    except Exception as e:
        print(f'Day {args.day} failed ❌')
        print(e)
        exit(1)
    else:
        if args.test:
            print(f'Day {args.day} is working ⭐️')
        else:
            print(f'Day {args.day} result: {result}')
