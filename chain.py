from datetime import datetime
from block import Block
from util import iterate_pairwise
from chain_db import ChainDb

db = ChainDb()


class Chain:
    def __init__(self):
        self.blocks: [Block] = []
        self.sync()

        if len(self) < 1:
            self.initialize_chain()

    def __len__(self):
        return len(self.blocks)

    def sync(self):
        self.blocks = db.get_blocks()

    def initialize_chain(self):
        print('initializing chain')

        first_block = Block(0, datetime.utcnow().timestamp(), 'first block', None, 420)
        db.add(first_block)

        self.sync()

    def verify(self) -> bool:
        for prev_block, curr_block in iterate_pairwise(self.blocks):
            if prev_block.get_hash() != curr_block.prev_hash:
                print('invalid block', curr_block.index)
                return False
        return True

    def verify_rev(self) -> bool:
        for block_idx in range(len(self.blocks) - 1, 0, -1):
            curr_block = self.blocks[block_idx]
            prev_block = self.blocks[block_idx - 1]
            print(curr_block.index, prev_block.index)

            if curr_block.prev_hash != prev_block.get_hash():
                print('invalid block', prev_block.index)
                return False

        return True

    def add_block(self, data):
        self.sync()
        last_block = self.blocks[-1]

        next_block = Block(last_block.index + 1, datetime.utcnow().timestamp(), data, last_block.get_hash())

        while not next_block.get_hash().startswith('420'):
            next_block.nonce += 1

        db.add(next_block)
        self.sync()
