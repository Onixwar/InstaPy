#!/bin/bash

# InstaPy Restart Script for Linux
# This script stops all InstaPy processes and restarts them

echo "🔄 Restarting InstaPy..."

# Function to kill processes by name
kill_processes() {
    local process_name=$1
    local pids=$(pgrep -f "$process_name")
    
    if [ ! -z "$pids" ]; then
        echo "🛑 Stopping $process_name processes: $pids"
        kill -TERM $pids 2>/dev/null || true
        sleep 2
        
        # Force kill if still running
        pids=$(pgrep -f "$process_name")
        if [ ! -z "$pids" ]; then
            echo "💀 Force killing $process_name processes: $pids"
            kill -KILL $pids 2>/dev/null || true
        fi
    else
        echo "✅ No $process_name processes found"
    fi
}

# Stop all related processes
echo "🛑 Stopping all InstaPy related processes..."

# Stop InstaPy Python processes
kill_processes "python.*quickstart"
kill_processes "python.*instapy"

# Stop Firefox processes
kill_processes "firefox"

# Stop Xvfb processes
kill_processes "Xvfb"

# Wait a moment for processes to fully stop
sleep 3

# Clean up any remaining temporary files
echo "🧹 Cleaning up temporary files..."
rm -rf /tmp/.X99-lock 2>/dev/null || true
rm -rf /tmp/.X11-unix/X99 2>/dev/null || true

# Check if any processes are still running
echo "🔍 Checking for remaining processes..."
remaining_pids=$(pgrep -f "instapy\|firefox\|Xvfb")
if [ ! -z "$remaining_pids" ]; then
    echo "⚠️  Some processes are still running: $remaining_pids"
    echo "   You may need to manually stop them"
else
    echo "✅ All processes stopped successfully"
fi

echo ""
echo "🚀 Ready to restart InstaPy!"
echo "Run: ./run_instapy.sh"
echo ""
