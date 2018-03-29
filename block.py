from hashlib import sha256


class Block:
    def __init__(self, index: int, timestamp: float, data, prev_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = nonce

    def __repr__(self):
        return f'{self.index}<{self.timestamp}>:{self.data}'

    @classmethod
    def from_db(cls, db_data):

        return Block(db_data['index'], db_data['timestamp'], db_data['data'], db_data['prev_hash'], db_data['nonce'])

    def get_header(self) -> str:
        return f'{self.index}-{self.timestamp}-{self.data}-{self.prev_hash}-{self.nonce}'

    def get_hash(self) -> str:
        sha = sha256()
        sha.update(self.get_header().encode())
        return sha.hexdigest()

    def to_dict(self) -> {}:
        return {'index': self.index,
                'timestamp': self.timestamp,
                'data': self.data,
                'prev_hash': self.prev_hash,
                'nonce': self.nonce}

    def save(self):
        pass
