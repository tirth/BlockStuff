from datetime import datetime


class Block:
    def __init__(self, index: int, timestamp: datetime, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash

    def __repr__(self):
        return f'{self.index}<{self.timestamp}>:{self.data}'

    @classmethod
    def from_db(cls, db_data):
        return Block(db_data['index'], db_data['timestamp'], db_data['data'], db_data['prev_hash'])

    def to_dict(self) -> {}:
        return {'index': self.index,
                'timestamp': self.timestamp,
                'data': self.data,
                'prev_hash': self.prev_hash}

    def save(self):
        pass
