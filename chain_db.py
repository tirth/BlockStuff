from pymongo import MongoClient
from block import Block

CONNECTION_STRING = 'mongodb://localhost:27017/'
DATABASE_NAME = 'blockDb'
COLLECTION_NAME = 'chain'


class ChainDb:
    def __init__(self):
        self._client = MongoClient(CONNECTION_STRING)
        self._db = self._client[DATABASE_NAME]
        self._chain = self._db[COLLECTION_NAME]

    def get_blocks(self) -> [Block]:
        return [Block.from_db(db_block) for db_block in self._chain.find()]

    def add(self, block: Block):
        self._chain.insert(block.to_dict())
