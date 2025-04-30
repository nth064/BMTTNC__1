from block import Block
import hashlib
import time 

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = Block(len(self.chain) + 1, previous_hash, time.time(), self.current_transactions, proof)
        self.current =_transactions = []
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hediest()
            if hash_operation[:4] == '0000':
                check_proof += 1
        return new_proof
    
    def add_transaction(self, sender, receiver, amount):
        self.current_transactions.append({'sender': sender, 'receiver': receiver, 'amount': amount})
        return self.get_previous_block().index + 1
     
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index