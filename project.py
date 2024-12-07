# defining the block structure
import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0  # Nonce for Proof of Work
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Start with the genesis block

    def create_genesis_block(self):

        # Create the first block in the chain
        
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def proof_of_work(self, block, difficulty):
        target = "0" * difficulty
        while block.hash[:difficulty] != target:
            block.nonce += 1
            block.hash = block.calculate_hash()

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True


# Mining blocks

if __name__ == "__main__":
    blockchain = Blockchain()
    difficulty = 4  # Adjust mining difficulty

    print("Mining block 1...")
    new_block1 = Block(1, time.time(), {"amount": 100}, blockchain.get_latest_block().hash)
    blockchain.proof_of_work(new_block1, difficulty)
    blockchain.add_block(new_block1)

    print("Mining block 2...")
    new_block2 = Block(2, time.time(), {"amount": 50}, blockchain.get_latest_block().hash)
    blockchain.proof_of_work(new_block2, difficulty)
    blockchain.add_block(new_block2)

    print("Blockchain is valid:", blockchain.is_chain_valid())

    # Print the blockchain
    for block in blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Data: {block.data}")
        print(f"Timestamp: {block.timestamp}")

