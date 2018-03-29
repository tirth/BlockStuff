from datetime import datetime
import pprint
from chain_db import ChainDb
from block import Block

db = ChainDb()


def initialize_chain():
    first_block = Block(0, datetime.utcnow(), 'first block', None)
    db.add(first_block)


def sync():
    blocks = db.get_blocks()
    print(f'found {len(blocks)} blocks')
    pprint.pprint(blocks)


def go():
    sync()


if __name__ == '__main__':
    go()
    print('^')
