#!/usr/bin/env python3

"""Basic scaffold for a Python script."""

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="A simple scaffolded Python script.")
    parser.add_argument("--name", default="World", help="Name to greet.")
    return parser.parse_args()


def main():
    args = parse_args()
    print(f"Hello, {args.name}!")
    print("Welcome to DEVASC")


if __name__ == "__main__":
    main()
