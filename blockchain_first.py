import datetime
import hashlib
import json


class Blockchain:
    def __init__(self):
        self.list_blocks = []
        initial_block = Block(0)
        self.list_blocks.append(initial_block)

    def get_blockchain(self):
        return self.list_blocks

    def get_json_blockchain(self):
        list_dicts_blockchain = [block.block_dict() for block in self.list_blocks]
        return json.dumps(list_dicts_blockchain, indent=4, sort_keys=True, default=str)

    def get_latest_block(self):
        return self.list_blocks[-1]

    def add_block(self):
        new_block = Block(self.get_latest_block().hash)
        self.list_blocks.append(new_block)


class Block:
    def __init__(self, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.previous_hash = previous_hash
        self.hash = self.hashing_v2(self.timestamp, self.previous_hash)

    def __repr__(self):
        return f'timestamp: {self.timestamp}, previous hash: {self.previous_hash}, hash: {self.hash}'

    def block_dict(self):
        dict_block = {"timestamp": self.timestamp, "previous_hash": self.previous_hash, "hash": self.hash}
        return dict_block

    def toJSON(self):
        dict_block = {"timestamp": self.timestamp, "previous_hash": self.previous_hash, "hash": self.hash}
        return json.dumps(dict_block)

    def hashing_v2(self, timestamp, previous_hash):
        nonce = 1
        while True:
            hash_tuple = (timestamp, previous_hash, nonce)
            hash_tuple = bytes(str(hash_tuple), encoding='utf-8')
            hash_answer = hashlib.sha256(hash_tuple).hexdigest()
            if str(hash_answer)[0:4] == "0000":
                return hash_answer
            else:
                nonce += 1
