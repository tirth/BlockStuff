from block import Block
from util import iterate_pairwise


class Chain:
    def __init__(self, blocks: [Block] = None):
        self._blocks: [Block] = blocks or []
        self._num_new = 0

        if len(self) < 1:
            self.initialize_chain()

    def __len__(self):
        return len(self._blocks)

    def get_new(self):
        return self._blocks[-self._num_new:]

    def add_block(self, block: Block):
        self._blocks.append(block)
        self._num_new += 1

    def initialize_chain(self):
        print('initializing chain')
        self.add_block(Block.first())

    def verify(self) -> bool:
        for curr_block, next_block in iterate_pairwise(self._blocks):
            if curr_block.get_hash() != next_block.prev_hash:
                print('invalid block', next_block.index)
                return False

        return True

    def verify_rev(self) -> bool:
        for block_idx in range(len(self) - 1, 0, -1):
            curr_block = self._blocks[block_idx]
            prev_block = self._blocks[block_idx - 1]

            if curr_block.prev_hash != prev_block.get_hash():
                print('invalid block', curr_block.index)
                return False

        return True

    def add_data(self, data):
        self.add_block(Block.next(self._blocks[-1], data))

    def synced(self):
        self._num_new = 0
