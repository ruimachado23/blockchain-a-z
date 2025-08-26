# Basic Blockchain Implementation


## Features

### Core Blockchain Functionality
- **Block Creation**: Each block contains index, timestamp, proof, and previous hash
- **Proof-of-Work Mining**: SHA-256-based mining with adjustable difficulty (4 leading zeros)
- **Chain Validation**: Verify the integrity of the entire blockchain
- **Genesis Block**: Automatic creation of the first block

### REST API Endpoints
- `GET /mine_block` - Mine a new block
- `GET /get_chain` - Retrieve the complete blockchain
- `GET /is_valid` - Validate the blockchain integrity

## Architecture

### Files Structure
```
blockchain/
├── blockchain.py      # Core blockchain implementation
├── app.py            # Flask web application
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

### Core Classes and Methods

#### `Blockchain` Class (`blockchain.py`)
```python
class Blockchain:
    def __init__(self)                    # Initialize with genesis block
    def create_block(proof, previous_hash) # Create and add new block
    def get_previous_block()              # Get the last block in chain
    def proof_of_work(previous_proof)     # Mine new proof-of-work
    def hash(block)                       # Generate SHA-256 hash
    def is_chain_valid(chain)             # Validate blockchain integrity
```

## How It Works

### 1. Block Structure
Each block contains:
```json
{
    "index": 1,
    "timestamp": "2024-01-15 10:30:45.123456",
    "proof": 92582,
    "previous_hash": "0abc123..."
}
```

### 2. Proof-of-Work Algorithm
The mining process involves:
1. Take the proof from the previous block
2. Try different values for new proof
3. Calculate: `SHA256(new_proof² - previous_proof²)`
4. Check if hash starts with "0000" (difficulty = 4)
5. If not, increment proof and try again
6. Return valid proof when found

### 3. Chain Validation
Validation checks:
- Each block's `previous_hash` matches the hash of the previous block
- Each block's proof-of-work is valid (hash starts with "0000")
- Chain integrity from genesis to current block

## Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation
```bash
# Navigate to blockchain directory
cd blockchain/

# Install dependencies
pip install -r requirements.txt
```

### Running the Blockchain
```bash
# Start the Flask application
python app.py
```

The blockchain will be available at: http://localhost:5000

### Basic Usage Examples

#### 1. Mine Your First Block
```bash
curl http://localhost:5000/mine_block
```

**Response:**
```json
{
    "message": "Congratulations: You just mined a block!",
    "index": 2,
    "timestamp": "2024-01-15 10:30:45.123456",
    "proof": 92582,
    "previous_hash": "0abc123def456..."
}
```

#### 2. View the Complete Blockchain
```bash
curl http://localhost:5000/get_chain
```

#### 3. Validate the Blockchain
```bash
curl http://localhost:5000/is_valid
```