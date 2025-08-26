# RMCoin - Complete Cryptocurrency Implementation

##  Features

### Advanced Blockchain Functionality
- **Transaction System**: Send and receive RMCoin between addresses
- **Mining Rewards**: Miners receive 1 RMCoin per block mined
- **Distributed Network**: Multiple nodes working together
- **Consensus Algorithm**: Longest Chain Rule for network agreement
- **Node Discovery**: Automatic network node management

### Enhanced Security
- **Chain Validation**: Comprehensive blockchain integrity checks
- **Transaction Validation**: Verify sender, receiver, and amount
- **Network Consensus**: Prevent double-spending through agreement
- **Unique Node IDs**: Each node has a unique address

##  Architecture

### Files Structure
```
rmcoin/
├── rmcoin.py           # Enhanced blockchain with transactions & networking
├── app.py             # Main node (port 5000)
├── node_5001.py       # Node 2 (port 5001)
├── node_5002.py       # Node 3 (port 5002)
├── node_5003.py       # Node 4 (port 5003)
├── start_nodes.sh     # Script to start all nodes
├── test_nodes.py      # Comprehensive network testing
├── example_usage.py   # Simple usage examples
├── nodes.json         # Node configuration
├── transation.json    # Transaction template
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

### Network Architecture
```
┌─────────────┐    ┌─────────────┐
│   Node 1    │    │   Node 2    │
│ (port 5000) │◄──►│ (port 5001) │
└─────────────┘    └─────────────┘
       ▲                   ▲
       │                   │
       ▼                   ▼
┌─────────────┐    ┌─────────────┐
│   Node 4    │    │   Node 3    │
│ (port 5003) │◄──►│ (port 5002) │
└─────────────┘    └─────────────┘
```

## How RMCoin Works

### 1. Enhanced Block Structure
Each block now includes transactions:
```json
{
    "index": 2,
    "timestamp": "2024-01-15 10:30:45.123456",
    "proof": 92582,
    "previous_hash": "0abc123...",
    "transactions": [
        {
            "sender": "Alice",
            "receiver": "Bob", 
            "amount": 50
        },
        {
            "sender": "node_address",
            "receiver": "miner_address",
            "amount": 1
        }
    ]
}
```

### 2. Transaction Lifecycle
1. **Transaction Creation**: User submits sender, receiver, amount
2. **Transaction Pool**: Added to pending transactions
3. **Mining**: Miner includes transactions in new block
4. **Reward**: Miner receives 1 RMCoin for successful mining
5. **Broadcast**: Block spreads across network

### 3. Consensus Mechanism - Longest Chain Rule
- Each node maintains its own blockchain copy
- When conflicts arise, nodes adopt the longest valid chain
- This prevents double-spending and ensures network agreement
- Invalid chains are automatically rejected

### 4. Network Synchronization
- Nodes communicate via HTTP REST APIs
- Chain replacement happens automatically
- Network maintains consistency across all nodes

##  Quick Start

### Prerequisites
- Python 3.7+
- curl (for testing)
- Multiple terminal windows (for manual node management)

### Option 1: Automated Network Start
```bash
# Install dependencies
pip install -r requirements.txt

# Start all 4 nodes automatically
./start_nodes.sh

# In another terminal, test the network
python3 test_nodes.py
```

### Option 2: Manual Node Management
```bash
# Terminal 1 - Main node
python3 app.py

# Terminal 2 - Node 2  
python3 node_5001.py

# Terminal 3 - Node 3
python3 node_5002.py

# Terminal 4 - Node 4
python3 node_5003.py

# Terminal 5 - Run tests
python3 test_nodes.py
```

### Option 3: Simple Example
```bash
# Start nodes first, then:
python3 example_usage.py
```

## API Endpoints

All nodes support these endpoints:

### GET Endpoints
| Endpoint | Description | Example |
|----------|-------------|---------|
| `/get_chain` | Get complete blockchain | `curl http://localhost:5000/get_chain` |
| `/mine_block` | Mine a new block | `curl http://localhost:5000/mine_block` |
| `/is_valid` | Validate blockchain | `curl http://localhost:5000/is_valid` |
| `/replace_chain` | Sync with longest chain | `curl http://localhost:5000/replace_chain` |
| `/get_node_address` | Get node's unique ID | `curl http://localhost:5000/get_node_address` |

### POST Endpoints
| Endpoint | Description | Example |
|----------|-------------|---------|
| `/add_transaction` | Add new transaction | See examples below |
| `/connect_node` | Connect to other nodes | See examples below |

## Usage Examples

### 1. Connect All Nodes
```bash
curl -X POST http://localhost:5000/connect_node \
  -H "Content-Type: application/json" \
  -d '{"nodes": ["http://localhost:5001", "http://localhost:5002", "http://localhost:5003"]}'
```

### 2. Add Transactions
```bash
# Alice sends 50 RMC to Bob
curl -X POST http://localhost:5000/add_transaction \
  -H "Content-Type: application/json" \
  -d '{"sender": "Alice", "receiver": "Bob", "amount": 50}'

# Bob sends 25 RMC to Charlie  
curl -X POST http://localhost:5001/add_transaction \
  -H "Content-Type: application/json" \
  -d '{"sender": "Bob", "receiver": "Charlie", "amount": 25}'
```

### 3. Mine Blocks
```bash
# Mine on node 1
curl http://localhost:5000/mine_block

# Mine on node 2
curl http://localhost:5001/mine_block
```

### 4. Check Chain Synchronization
```bash
# Get chain from each node
curl http://localhost:5000/get_chain | jq '.length'
curl http://localhost:5001/get_chain | jq '.length'
curl http://localhost:5002/get_chain | jq '.length'
curl http://localhost:5003/get_chain | jq '.length'
```

### 5. Force Network Sync
```bash
# Sync all nodes to longest chain
curl http://localhost:5000/replace_chain
curl http://localhost:5001/replace_chain
curl http://localhost:5002/replace_chain
curl http://localhost:5003/replace_chain
```


##  Network Monitoring

### Check Network Status
```bash
# Get unique node addresses
curl http://localhost:5000/get_node_address
curl http://localhost:5001/get_node_address
curl http://localhost:5002/get_node_address
curl http://localhost:5003/get_node_address

# Check if chains are synchronized
for port in 5000 5001 5002 5003; do
  echo "Node $port chain length:"
  curl -s http://localhost:$port/get_chain | jq '.length'
done
```

### Monitor Mining Activity
```bash
# Mine on different nodes and watch propagation
curl http://localhost:5000/mine_block
sleep 2
curl http://localhost:5001/replace_chain
curl http://localhost:5002/replace_chain
curl http://localhost:5003/replace_chain
```
