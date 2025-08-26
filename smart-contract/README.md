# RMCoin ICO Smart Contract

## Features

### ICO Smart Contract Functionality
- **Token Supply Management**: Maximum supply of 1,000,000 RMCoin
- **Dynamic Pricing**: 1 USD = 1,000 RMCoin exchange rate
- **Investor Tracking**: Individual equity tracking for all investors
- **Buy/Sell Operations**: Secure token purchase and sale functions
- **Supply Validation**: Prevents over-issuance through modifiers

### Security Features
- **Input Validation**: Comprehensive checks on all transactions
- **Supply Limits**: Hard cap preventing infinite token creation
- **Balance Verification**: Ensures sufficient balance before sales
- **Solidity Best Practices**: Modern Solidity ^0.8.0 syntax

## Architecture

### Files Structure
```
smart-contract/
├── rmcoin_ico.sol              # ICO smart contract
├── etherwallet-v3.21.20/       # MyEtherWallet interface
│   ├── index.html              # Main wallet interface
│   ├── js/                     # JavaScript libraries
│   ├── css/                    # Styling
│   ├── images/                 # UI assets
│   └── ...                     # Additional wallet files
└── README.md                   # This file
```

### Technology Stack
- **Smart Contract**: Solidity ^0.8.0
- **Local Blockchain**: Ganache (required)
- **Wallet Interface**: MyEtherWallet (local fork)
- **Development**: Web3.js integration
- **Browser**: Any modern browser for interface

##  Smart Contract Details

### Contract: `RMCOIN_ICO`

#### State Variables
```solidity
uint256 public max_supply = 1000000;      // Maximum RMCoin supply
uint public usd_to_rmcoin = 1000;         // Exchange rate: 1 USD = 1000 RMC
uint public total_rmcoin_bought = 0;      // Total tokens sold
mapping(address => uint256) equity_rmcoin; // Investor token balances
mapping(address => uint256) equity_usd;   // Investor USD invested
```

#### Key Functions

##### 1. Investment Functions
```solidity
function buy_rmcoin(address investor, uint256 usd_invested) 
    external can_buy_rmcoin(usd_invested)
```
- Allows investors to purchase RMCoin with USD
- Automatically calculates token amount based on exchange rate
- Updates investor equity and total supply

```solidity
function sell_rmcoin(address investor, uint256 rmcoin_sold) 
    external
```
- Enables investors to sell their RMCoin back
- Validates sufficient balance before sale
- Updates equity and reduces total supply

##### 2. Query Functions
```solidity
function get_equity_rmcoin(address investor) 
    external view returns (uint256)
```
- Returns investor's RMCoin balance

```solidity
function get_equity_usd(address investor) 
    external view returns (uint256)
```
- Returns investor's total USD investment

```solidity
function get_current_price() external view returns (uint256)
function get_max_supply() external view returns (uint256)
```
- Utility functions for price and supply information

#### Security Modifiers
```solidity
modifier can_buy_rmcoin(uint256 usd_invested) {
    require(
        usd_invested * usd_to_rmcoin + total_rmcoin_bought <= max_supply,
        "Exceeds maximum RMCOIN supply"
    );
    _;
}
```
- Prevents purchases that would exceed maximum supply
- Ensures ICO hard cap compliance

## 🛠️ Setup & Deployment

### Prerequisites
1. **Ganache**: Download from [Trufflesuite](https://trufflesuite.com/ganache/)
2. **Modern Browser**: Chrome, Firefox, or Safari
3. **Basic Ethereum Knowledge**: Understanding of addresses, gas, etc.

### Step 1: Start Local Blockchain
```bash
# Download and install Ganache
# Start Ganache with default settings:
# - Network ID: 5777
# - RPC Server: HTTP://127.0.0.1:7545
# - Gas Limit: 6721975
# - Gas Price: 20000000000
```

### Step 2: Access MyEtherWallet
```bash
# Navigate to the wallet directory
cd etherwallet-v3.21.20/

# Open in browser (choose one):
# Method 1: Direct file open
open index.html  # macOS
xdg-open index.html  # Linux
start index.html  # Windows

# Method 2: Simple HTTP server
python3 -m http.server 8080
# Then visit: http://localhost:8080
```

### Step 3: Connect to Ganache
1. In MyEtherWallet, go to **Network** settings
2. Select **Custom Network**
3. Enter:
   - **Node Name**: Ganache
   - **URL**: http://127.0.0.1:7545
   - **Port**: 7545
   - **Chain ID**: 5777

### Step 4: Import Ganache Account
1. Copy a private key from Ganache
2. In MyEtherWallet, select **Private Key** access
3. Paste the private key and unlock

##  Deploying the ICO Contract

### Method 1: MyEtherWallet Interface
1. Go to **Contracts** tab
2. Select **Deploy Contract**
3. Copy the Solidity code from `rmcoin_ico.sol`
4. Set gas limit to ~500,000
5. Deploy and note the contract address

### Method 2: Manual Deployment
```javascript
// In browser console or Remix IDE
const contract = new web3.eth.Contract(abi);
contract.deploy({
    data: bytecode
}).send({
    from: '0xYourAddress',
    gas: 500000
}).then(instance => {
    console.log('Contract deployed at:', instance.options.address);
});
```

##  ICO Interaction Examples

### Check ICO Status
```javascript
// Get current supply and pricing
contract.methods.get_max_supply().call();
contract.methods.get_current_price().call();
contract.methods.total_rmcoin_bought().call();
```

### Buy RMCoin Tokens
```javascript
// Buy $100 worth of RMCoin (gets 100,000 tokens)
contract.methods.buy_rmcoin(
    '0xInvestorAddress',
    100  // USD amount
).send({
    from: '0xYourAddress',
    gas: 200000
});
```

### Check Investor Balance
```javascript
// Check how many tokens an investor owns
contract.methods.get_equity_rmcoin('0xInvestorAddress').call();

// Check how much USD they've invested
contract.methods.get_equity_usd('0xInvestorAddress').call();
```

### Sell RMCoin Tokens
```javascript
// Sell 50,000 RMCoin tokens
contract.methods.sell_rmcoin(
    '0xInvestorAddress',
    50000  // RMCoin amount
).send({
    from: '0xYourAddress', 
    gas: 200000
});
```


##  ICO Analytics

### Track ICO Progress
```javascript
// ICO completion percentage
const maxSupply = await contract.methods.get_max_supply().call();
const sold = await contract.methods.total_rmcoin_bought().call();
const completion = (sold / maxSupply) * 100;
console.log(`ICO ${completion.toFixed(2)}% complete`);

// Funds raised (in USD)
const fundsRaised = sold / 1000; // Since 1 USD = 1000 RMC
console.log(`Total funds raised: $${fundsRaised}`);
```

### Investor Analysis
```javascript
// Top investors (manual tracking needed)
const investors = ['0xAddr1', '0xAddr2', '0xAddr3'];
for (const investor of investors) {
    const equity = await contract.methods.get_equity_rmcoin(investor).call();
    const usd = await contract.methods.get_equity_usd(investor).call();
    console.log(`${investor}: ${equity} RMC ($${usd})`);
}
```


