#!/usr/bin/env python3
"""
index database(s) for plant data
"""

import sys
import argparse

import pymongo

def main(argv):
    """ main function """
    parser = argparse.ArgumentParser(
        description="index database(s) for plant data",
    )
    args = parser.parse_args(argv)

    client = pymongo.MongoClient()
    client.plantdb.categories.create_index(
        [
            ("name", pymongo.ASCENDING),
        ],
        unique=True,
    )
    client.plantdb.plants.create_index(
        [
            ("name", pymongo.ASCENDING),
        ],
        unique=True,
    )

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
