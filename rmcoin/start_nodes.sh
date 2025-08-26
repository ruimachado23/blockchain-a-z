#!/bin/bash

# Start RMCoin blockchain nodes
echo "Starting RMCoin blockchain network..."

# Start node on port 5000 (main node)
echo "Starting node on port 5000..."
python3 app.py &
NODE1_PID=$!

# Wait a moment for the first node to start
sleep 2

# Start node on port 5001
echo "Starting node on port 5001..."
python3 node_5001.py &
NODE2_PID=$!

# Start node on port 5002
echo "Starting node on port 5002..."
python3 node_5002.py &
NODE3_PID=$!

# Start node on port 5003
echo "Starting node on port 5003..."
python3 node_5003.py &
NODE4_PID=$!

echo "All nodes started successfully!"
echo "Node 1 (main): http://localhost:5000"
echo "Node 2: http://localhost:5001"
echo "Node 3: http://localhost:5002"
echo "Node 4: http://localhost:5003"
echo ""
echo "Press Ctrl+C to stop all nodes"

# Function to handle cleanup when script is terminated
cleanup() {
    echo ""
    echo "Stopping all nodes..."
    kill $NODE1_PID $NODE2_PID $NODE3_PID $NODE4_PID 2>/dev/null
    echo "All nodes stopped."
    exit 0
}

# Trap SIGINT (Ctrl+C) and call cleanup function
trap cleanup SIGINT

# Wait for all background processes
wait
