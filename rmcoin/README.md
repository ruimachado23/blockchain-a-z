# RMCoin Blockchain Network

A distributed blockchain implementation with multiple nodes supporting mining, transactions, and consensus.

## Features

- **Mining**: Proof-of-work mining with adjustable difficulty
- **Transactions**: Send and receive RMCoin between addresses
- **Consensus**: Longest chain rule for network synchronization
- **Multiple Nodes**: Run multiple nodes on different ports
- **REST API**: Full HTTP API for all blockchain operations

## Files Structure

- `rmcoin.py` - Core blockchain implementation
- `app.py` - Main node (port 5000)
- `node_5001.py` - Node 2 (port 5001)
- `node_5002.py` - Node 3 (port 5002) 
- `node_5003.py` - Node 4 (port 5003)
- `start_nodes.sh` - Script to start all nodes
- `test_nodes.py` - Test script for network functionality
- `nodes.json` - Node configuration
- `transation.json` - Transaction template

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start All Nodes
```bash
./start_nodes.sh
```

### 3. Test the Network
```bash
python3 test_nodes.py
```

## API Endpoints

All nodes support the following endpoints:

### GET Endpoints
- `GET /get_chain` - Get the complete blockchain
- `GET /mine_block` - Mine a new block
- `GET /is_valid` - Validate the blockchain
- `GET /replace_chain` - Sync with the longest chain
- `GET /get_node_address` - Get node's unique address

### POST Endpoints
- `POST /add_transaction` - Add a new transaction
- `POST /connect_node` - Connect to other nodes

## Manual Usage Examples

### Start Individual Nodes
```bash
# Start main node (port 5000)
python3 app.py

# Start additional nodes
python3 node_5001.py  # port 5001
python3 node_5002.py  # port 5002
python3 node_5003.py  # port 5003
```

### Connect Nodes
```bash
curl -X POST http://localhost:5000/connect_node \
  -H "Content-Type: application/json" \
  -d '{"nodes": ["http://localhost:5001", "http://localhost:5002", "http://localhost:5003"]}'
```

### Add Transaction
```bash
curl -X POST http://localhost:5000/add_transaction \
  -H "Content-Type: application/json" \
  -d '{"sender": "Alice", "receiver": "Bob", "amount": 10}'
```

### Mine Block
```bash
curl http://localhost:5000/mine_block
```

### Get Blockchain
```bash
curl http://localhost:5000/get_chain
```

### Sync Chains
```bash
curl http://localhost:5000/replace_chain
```

## Network Ports

- Node 1 (Main): http://localhost:5000
- Node 2: http://localhost:5001
- Node 3: http://localhost:5002
- Node 4: http://localhost:5003

## Consensus Algorithm

The network uses the **Longest Chain Rule**:
- Nodes automatically sync to the longest valid chain
- Invalid chains are rejected
- Proof-of-work ensures consensus security

## Mining

- Mining reward: 1 RMCoin per block
- Difficulty: 4 leading zeros in hash
- Algorithm: SHA-256 proof-of-work
- Reward goes to the miner's node address

## Testing

The `test_nodes.py` script performs comprehensive testing:
1. Checks node connectivity
2. Connects all nodes
3. Adds sample transactions
4. Mines blocks on different nodes
5. Verifies chain synchronization

## Troubleshooting

### Nodes Not Starting
- Check if ports are already in use
- Ensure Python 3 and dependencies are installed
- Verify file permissions for scripts

### Connection Issues
- Make sure all nodes are running
- Check firewall settings
- Verify correct port numbers in requests

### Chain Sync Problems
- Use `/replace_chain` endpoint to force sync
- Check network connectivity between nodes
- Verify all nodes are connected via `/connect_node`
