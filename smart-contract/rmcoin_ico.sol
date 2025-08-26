pragma solidity ^0.8.0;

contract RMCOIN_ICO {
    uint256 public max_supply = 1000000;
    uint public usd_to_rmcoin = 1000;
    uint public total_rmcoin_bought = 0;

    mapping(address => uint256) equity_rmcoin;
    mapping(address => uint256) equity_usd;

    modifier can_buy_rmcoin(uint256 usd_invested) {
        require(
            usd_invested * usd_to_rmcoin + total_rmcoin_bought <= max_supply,
            "Exceeds maximum RMCOIN supply"
        );
        _;
    }
    
    function get_equity_rmcoin(address investor) external view returns (uint256) {
        return equity_rmcoin[investor];
    }
    
    function get_equity_usd(address investor) external view returns (uint256) {
        return equity_usd[investor];
    }
    
    function buy_rmcoin(address investor, uint256 usd_invested) external can_buy_rmcoin(usd_invested) {
        uint256 rmcoin_bought = usd_invested * usd_to_rmcoin;
        equity_rmcoin[investor] += rmcoin_bought;
        equity_usd[investor] += usd_invested;
        total_rmcoin_bought += rmcoin_bought;
    }
    
    function sell_rmcoin(address investor, uint256 rmcoin_sold) external {
        require(equity_rmcoin[investor] >= rmcoin_sold, "Insufficient RMCOIN balance");
        uint256 usd_value = rmcoin_sold / usd_to_rmcoin;
        equity_rmcoin[investor] -= rmcoin_sold;
        equity_usd[investor] -= usd_value;
        total_rmcoin_bought -= rmcoin_sold;
    }

    function get_current_price() external view returns (uint256) {
        return usd_to_rmcoin;
    }

    function get_max_supply() external view returns (uint256) {
        return max_supply;
    }
}
