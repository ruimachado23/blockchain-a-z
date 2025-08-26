#!/usr/bin/env python3
"""
Simple example demonstrating RMCoin blockchain usage.
Run this after starting the nodes with ./start_nodes.sh
"""

import requests
import json
import time

# Main node URL
NODE_URL = "http://localhost:5000"

def make_request(method, endpoint, data=None):
    """Helper function to make HTTP requests."""
    url = f"{NODE_URL}{endpoint}"
    try:
        if method == "GET":
            response = requests.get(url, timeout=10)
        elif method == "POST":
            response = requests.post(url, json=data, timeout=10)
        
        if response.status_code in [200, 201]:
            return True, response.json()
        else:
            return False, {"error": f"HTTP {response.status_code}: {response.text}"}
    except requests.exceptions.RequestException as e:
        return False, {"error": str(e)}

def main():
    """Demonstrate basic blockchain operations."""
    print("RMCoin Blockchain Example")
    print("=" * 30)
    
    # 1. Get initial chain
    print("\n1. Getting initial blockchain...")
    success, result = make_request("GET", "/get_chain")
    if success:
        print(f"Initial chain length: {result['length']}")
    else:
        print(f"Error: {result['error']}")
        return
    
    # 2. Add a transaction
    print("\n2. Adding a transaction...")
    transaction = {
        "sender": "Alice",
        "receiver": "Bob", 
        "amount": 25
    }
    success, result = make_request("POST", "/add_transaction", transaction)
    if success:
        print(f"Transaction added: {result['message']}")
    else:
        print(f"Error: {result['error']}")
    
    # 3. Mine a block
    print("\n3. Mining a block...")
    success, result = make_request("GET", "/mine_block")
    if success:
        print(f"Block mined successfully!")
        print(f"Block index: {result['index']}")
        print(f"Transactions in block: {len(result['transactions'])}")
    else:
        print(f"Error: {result['error']}")
    
    # 4. Get updated chain
    print("\n4. Getting updated blockchain...")
    success, result = make_request("GET", "/get_chain")
    if success:
        print(f"Updated chain length: {result['length']}")
        
        # Show last block details
        if result['chain']:
            last_block = result['chain'][-1]
            print(f"Last block index: {last_block['index']}")
            print(f"Last block transactions: {len(last_block['transactions'])}")
    else:
        print(f"Error: {result['error']}")
    
    # 5. Connect to other nodes
    print("\n5. Connecting to other nodes...")
    other_nodes = {
        "nodes": [
            "http://localhost:5001",
            "http://localhost:5002", 
            "http://localhost:5003"
        ]
    }
    success, result = make_request("POST", "/connect_node", other_nodes)
    if success:
        print(f"Connected to {len(result['total_nodes'])} nodes")
    else:
        print(f"Error: {result['error']}")
    
    # 6. Validate chain
    print("\n6. Validating blockchain...")
    success, result = make_request("GET", "/is_valid")
    if success:
        print(f"Validation result: {result['message']}")
    else:
        print(f"Error: {result['error']}")
    
    print("\n" + "=" * 30)
    print("Example completed!")
    print("You can now interact with the blockchain using the API endpoints.")

if __name__ == "__main__":
    main()
