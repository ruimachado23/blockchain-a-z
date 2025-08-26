#!/usr/bin/env python3
"""
Test script to verify RMCoin blockchain node communication and functionality.
"""

import requests
import json
import time
import sys

# Node URLs
NODES = [
    "http://localhost:5000",
    "http://localhost:5001", 
    "http://localhost:5002",
    "http://localhost:5003"
]

def test_node_connection(node_url):
    """Test if a node is running and responsive."""
    try:
        response = requests.get(f"{node_url}/get_chain", timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def connect_nodes():
    """Connect all nodes to each other."""
    print("Connecting nodes to each other...")
    
    for i, node in enumerate(NODES):
        other_nodes = [n for j, n in enumerate(NODES) if j != i]
        
        try:
            response = requests.post(f"{node}/connect_node", 
                                   json={"nodes": other_nodes},
                                   timeout=10)
            if response.status_code == 201:
                print(f"✓ Node {node} connected to network")
            else:
                print(f"✗ Failed to connect node {node}: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"✗ Error connecting node {node}: {e}")

def add_transaction(node_url, sender, receiver, amount):
    """Add a transaction to a node."""
    try:
        response = requests.post(f"{node_url}/add_transaction",
                               json={
                                   "sender": sender,
                                   "receiver": receiver,
                                   "amount": amount
                               },
                               timeout=10)
        return response.status_code == 201, response.json()
    except requests.exceptions.RequestException as e:
        return False, {"error": str(e)}

def mine_block(node_url):
    """Mine a block on a specific node."""
    try:
        response = requests.get(f"{node_url}/mine_block", timeout=30)
        return response.status_code == 200, response.json()
    except requests.exceptions.RequestException as e:
        return False, {"error": str(e)}

def get_chain(node_url):
    """Get the blockchain from a node."""
    try:
        response = requests.get(f"{node_url}/get_chain", timeout=10)
        return response.status_code == 200, response.json()
    except requests.exceptions.RequestException as e:
        return False, {"error": str(e)}

def sync_chains():
    """Sync chains across all nodes."""
    print("\nSyncing chains across nodes...")
    
    for node in NODES:
        try:
            response = requests.get(f"{node}/replace_chain", timeout=15)
            if response.status_code == 200:
                result = response.json()
                print(f"✓ Node {node}: {result['message']}")
            else:
                print(f"✗ Failed to sync node {node}")
        except requests.exceptions.RequestException as e:
            print(f"✗ Error syncing node {node}: {e}")

def main():
    """Main test function."""
    print("RMCoin Blockchain Network Test")
    print("=" * 40)
    
    # Test node connections
    print("\n1. Testing node connections...")
    active_nodes = []
    for node in NODES:
        if test_node_connection(node):
            print(f"✓ Node {node} is active")
            active_nodes.append(node)
        else:
            print(f"✗ Node {node} is not responding")
    
    if len(active_nodes) < 2:
        print("\nError: Need at least 2 active nodes to test network functionality")
        sys.exit(1)
    
    # Connect nodes
    print("\n2. Connecting nodes...")
    connect_nodes()
    
    # Add some transactions
    print("\n3. Adding transactions...")
    transactions = [
        ("Alice", "Bob", 50),
        ("Bob", "Charlie", 25),
        ("Charlie", "Alice", 10)
    ]
    
    for i, (sender, receiver, amount) in enumerate(transactions):
        node = active_nodes[i % len(active_nodes)]
        success, result = add_transaction(node, sender, receiver, amount)
        if success:
            print(f"✓ Transaction added to {node}: {sender} → {receiver} ({amount} RMC)")
        else:
            print(f"✗ Failed to add transaction to {node}: {result}")
    
    # Mine blocks
    print("\n4. Mining blocks...")
    for i, node in enumerate(active_nodes[:2]):  # Mine on first 2 nodes
        print(f"Mining block on {node}...")
        success, result = mine_block(node)
        if success:
            print(f"✓ Block mined on {node}: Block #{result['index']}")
        else:
            print(f"✗ Failed to mine block on {node}: {result}")
        
        time.sleep(1)  # Brief pause between mining
    
    # Check chain lengths
    print("\n5. Checking chain lengths...")
    for node in active_nodes:
        success, result = get_chain(node)
        if success:
            print(f"✓ Node {node}: Chain length = {result['length']}")
        else:
            print(f"✗ Failed to get chain from {node}")
    
    # Sync chains
    print("\n6. Syncing chains...")
    sync_chains()
    
    # Final chain check
    print("\n7. Final chain verification...")
    for node in active_nodes:
        success, result = get_chain(node)
        if success:
            print(f"✓ Node {node}: Final chain length = {result['length']}")
        else:
            print(f"✗ Failed to get final chain from {node}")
    
    print("\n" + "=" * 40)
    print("Test completed!")

if __name__ == "__main__":
    main()
