# Blockchain A-Z

This repository contains the complete implementation of a blockchain learning project based on the Udemy course *Blockchain A-Z: Learn How To Build Your First Blockchain* by Hadelin de Ponteves and Kirill Eremenko.

## Overview

This project demonstrates the fundamental concepts of blockchain technology through practical implementation, covering:

- **Blockchain Fundamentals**: Understanding blocks, hashing, proof-of-work, and chain validation
- **Cryptocurrency Creation**: Building a complete cryptocurrency with mining and transactions
- **Smart Contracts**: Implementing and deploying smart contracts for Initial Coin Offering (ICO)

## Project Structure

The project is organized into three main components, each representing a different aspect of blockchain technology:

### 1.  [blockchain/](./blockchain/) - Basic Blockchain Implementation
A foundational blockchain implementation that demonstrates core concepts:
- **Purpose**: Learn basic blockchain structure and mining
- **Features**: Block creation, proof-of-work mining, chain validation
- **Technology**: Python with Flask for REST API
- **Key Files**: 
  - `blockchain.py` - Core blockchain logic
  - `app.py` - Web API interface

### 2.  [rmcoin/](./rmcoin/) - Cryptocurrency Implementation  
A complete cryptocurrency system with distributed network capabilities:
- **Purpose**: Build a fully functional cryptocurrency (RMCoin)
- **Features**: 
  - Multi-node distributed network
  - Transaction system with sender/receiver/amount
  - Mining rewards and consensus mechanism
  - Network synchronization using longest chain rule
- **Technology**: Python with Flask, distributed across multiple nodes
- **Key Files**:
  - `rmcoin.py` - Enhanced blockchain with transactions and networking
  - `app.py` + `node_*.py` - Multiple node implementations
  - `start_nodes.sh` - Network startup script
  - `test_nodes.py` - Comprehensive network testing

### 3.  [smart-contract/](./smart-contract/) - Smart Contract & ICO
Smart contract implementation for RMCoin Initial Coin Offering:
- **Purpose**: Learn smart contract development and ICO mechanics
- **Features**:
  - ICO contract with supply limits and pricing
  - Investor equity tracking
  - Buy/sell functionality with automatic price calculation
- **Technology**: Solidity smart contracts, MyEtherWallet integration
- **Key Files**:
  - `rmcoin_ico.sol` - ICO smart contract
  - `etherwallet-v3.21.20/` - Local MyEtherWallet interface

## Quick Start Guide

### Prerequisites
- Python 3.7+
- Flask
- Basic understanding of blockchain concepts

### Option 1: Try the Basic Blockchain
```bash
cd blockchain/
pip install -r requirements.txt
python app.py
```
Visit http://localhost:5000 to interact with the basic blockchain.

### Option 2: Run the Complete RMCoin Network
```bash
cd rmcoin/
pip install -r requirements.txt
./start_nodes.sh
```
This starts a 4-node network. Use the test script to see it in action:
```bash
python test_nodes.py
```

### Option 3: Deploy the Smart Contract
1. Install and run [Ganache](https://trufflesuite.com/ganache/) for local blockchain
2. Navigate to `smart-contract/etherwallet-v3.21.20/`
3. Open `index.html` in your browser
4. Deploy `rmcoin_ico.sol` contract
5. Interact with the ICO through the web interface

##  Technologies Used

- **Backend**: Python 3, Flask framework
- **Blockchain**: Custom implementation with SHA-256 hashing
- **Smart Contracts**: Solidity ^0.8.0
- **Frontend**: MyEtherWallet (forked version)
- **Development Tools**: Ganache for local blockchain testing
- **Networking**: HTTP REST APIs for node communication

