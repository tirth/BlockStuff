from typing import Iterator
from pymongo import MongoClient
from pymongo.cursor import Cursor
from block import Block
from chain import Chain

CONNECTION_STRING = 'mongodb://localhost:27017/'
DATABASE_NAME = 'blockDb'
COLLECTION_NAME = 'chain'


class ChainDb:
    def __init__(self):
        self._client = MongoClient(CONNECTION_STRING)
        self._db = self._client[DATABASE_NAME]
        self._chain = self._db[COLLECTION_NAME]

    def _block_cursor(self) -> Cursor:
        return self._chain.find()

    def get_blocks(self) -> Iterator[Block]:
        return (Block.from_db(db_block) for db_block in self._block_cursor())

    def get_chain(self) -> Chain:
        return Chain([b for b in self.get_blocks()])

    def add(self, block: Block):
        self._chain.insert(block.to_dict())

    def add_many(self, blocks: [Block]):
        self._chain.insert_many(b.to_dict() for b in blocks)

    def sync(self, chain: Chain):
        new_blocks = chain.get_new()

        if len(new_blocks) < 1:
            print('no new blocks')
            return

        if not chain.verify():
            print('invalid chain')
            return

        print(f'syncing chain, {len(new_blocks)} new blocks')
        self.add_many(new_blocks)

        chain.synced()
