#!/usr/bin/env python3
"""
InstaPy Monitoring Script
This script monitors InstaPy processes and provides status information
"""

import os
import sys
import time
import psutil
import json
from datetime import datetime
from pathlib import Path

class InstaPyMonitor:
    def __init__(self, workspace_path=None):
        self.workspace_path = workspace_path or os.path.expanduser("~/InstaPy")
        self.logs_path = os.path.join(self.workspace_path, "logs")
        self.db_path = os.path.join(self.workspace_path, "db")
        
    def check_processes(self):
        """Check if InstaPy processes are running"""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'memory_info', 'cpu_percent']):
            try:
                if 'python' in proc.info['name'].lower():
                    cmdline = ' '.join(proc.info['cmdline'] or [])
                    if 'instapy' in cmdline.lower() or 'quickstart.py' in cmdline:
                        processes.append({
                            'pid': proc.info['pid'],
                            'name': proc.info['name'],
                            'cmdline': cmdline,
                            'memory_mb': proc.info['memory_info'].rss / 1024 / 1024,
                            'cpu_percent': proc.info['cpu_percent']
                        })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return processes
    
    def check_firefox_processes(self):
        """Check Firefox processes"""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'memory_info', 'cpu_percent']):
            try:
                if 'firefox' in proc.info['name'].lower():
                    processes.append({
                        'pid': proc.info['pid'],
                        'name': proc.info['name'],
                        'memory_mb': proc.info['memory_info'].rss / 1024 / 1024,
                        'cpu_percent': proc.info['cpu_percent']
                    })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return processes
    
    def check_xvfb_processes(self):
        """Check Xvfb processes"""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'memory_info', 'cpu_percent']):
            try:
                if 'Xvfb' in proc.info['name']:
                    processes.append({
                        'pid': proc.info['pid'],
                        'name': proc.info['name'],
                        'memory_mb': proc.info['memory_info'].rss / 1024 / 1024,
                        'cpu_percent': proc.info['cpu_percent']
                    })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return processes
    
    def get_log_files(self):
        """Get list of log files"""
        if not os.path.exists(self.logs_path):
            return []
        
        log_files = []
        for file in os.listdir(self.logs_path):
            if file.endswith('.log'):
                file_path = os.path.join(self.logs_path, file)
                stat = os.stat(file_path)
                log_files.append({
                    'name': file,
                    'size_mb': stat.st_size / 1024 / 1024,
                    'modified': datetime.fromtimestamp(stat.st_mtime).isoformat()
                })
        return sorted(log_files, key=lambda x: x['modified'], reverse=True)
    
    def get_database_info(self):
        """Get database information"""
        db_file = os.path.join(self.db_path, "instapy.db")
        if os.path.exists(db_file):
            stat = os.stat(db_file)
            return {
                'exists': True,
                'size_mb': stat.st_size / 1024 / 1024,
                'modified': datetime.fromtimestamp(stat.st_mtime).isoformat()
            }
        return {'exists': False}
    
    def get_system_info(self):
        """Get system information"""
        return {
            'cpu_percent': psutil.cpu_percent(interval=1),
            'memory_percent': psutil.virtual_memory().percent,
            'memory_available_gb': psutil.virtual_memory().available / 1024 / 1024 / 1024,
            'disk_usage': psutil.disk_usage('/').percent,
            'load_average': os.getloadavg() if hasattr(os, 'getloadavg') else None
        }
    
    def get_status_summary(self):
        """Get overall status summary"""
        instapy_procs = self.check_processes()
        firefox_procs = self.check_firefox_processes()
        xvfb_procs = self.check_xvfb_processes()
        
        status = "unknown"
        if instapy_procs and firefox_procs and xvfb_procs:
            status = "running"
        elif instapy_procs:
            status = "partial"
        else:
            status = "stopped"
        
        return {
            'status': status,
            'instapy_processes': len(instapy_procs),
            'firefox_processes': len(firefox_procs),
            'xvfb_processes': len(xvfb_procs),
            'timestamp': datetime.now().isoformat()
        }
    
    def print_status(self, detailed=False):
        """Print status information"""
        print("🚀 InstaPy Status Monitor")
        print("=" * 50)
        
        # Overall status
        summary = self.get_status_summary()
        status_emoji = {
            'running': '🟢',
            'partial': '🟡',
            'stopped': '🔴',
            'unknown': '⚪'
        }
        print(f"Status: {status_emoji.get(summary['status'], '⚪')} {summary['status'].upper()}")
        print(f"Timestamp: {summary['timestamp']}")
        print()
        
        # Process information
        print("📊 Process Information:")
        instapy_procs = self.check_processes()
        if instapy_procs:
            print(f"  InstaPy: {len(instapy_procs)} process(es)")
            for proc in instapy_procs:
                print(f"    PID {proc['pid']}: {proc['cmdline'][:50]}...")
                print(f"      Memory: {proc['memory_mb']:.1f} MB, CPU: {proc['cpu_percent']:.1f}%")
        else:
            print("  InstaPy: No processes running")
        
        firefox_procs = self.check_firefox_processes()
        if firefox_procs:
            print(f"  Firefox: {len(firefox_procs)} process(es)")
        else:
            print("  Firefox: No processes running")
        
        xvfb_procs = self.check_xvfb_processes()
        if xvfb_procs:
            print(f"  Xvfb: {len(xvfb_procs)} process(es)")
        else:
            print("  Xvfb: No processes running")
        
        print()
        
        if detailed:
            # System information
            print("💻 System Information:")
            sys_info = self.get_system_info()
            print(f"  CPU Usage: {sys_info['cpu_percent']:.1f}%")
            print(f"  Memory Usage: {sys_info['memory_percent']:.1f}%")
            print(f"  Available Memory: {sys_info['memory_available_gb']:.1f} GB")
            print(f"  Disk Usage: {sys_info['disk_usage']:.1f}%")
            if sys_info['load_average']:
                print(f"  Load Average: {sys_info['load_average'][0]:.2f}")
            print()
            
            # Log files
            print("📝 Log Files:")
            log_files = self.get_log_files()
            if log_files:
                for log_file in log_files[:5]:  # Show last 5 logs
                    print(f"  {log_file['name']}: {log_file['size_mb']:.2f} MB")
                    print(f"    Modified: {log_file['modified']}")
            else:
                print("  No log files found")
            print()
            
            # Database
            print("🗄️  Database:")
            db_info = self.get_database_info()
            if db_info['exists']:
                print(f"  Status: Exists")
                print(f"  Size: {db_info['size_mb']:.2f} MB")
                print(f"  Modified: {db_info['modified']}")
            else:
                print("  Status: Not found")
            print()
        
        # Recommendations
        print("💡 Recommendations:")
        if summary['status'] == 'running':
            print("  ✅ InstaPy is running normally")
        elif summary['status'] == 'partial':
            print("  ⚠️  Some components are missing. Check Firefox and Xvfb")
        else:
            print("  ❌ InstaPy is not running. Start with: python quickstart.py")
        
        if not firefox_procs:
            print("  🔧 Firefox is not running. Check installation")
        if not xvfb_procs:
            print("  🔧 Xvfb is not running. Start with: Xvfb :99 -screen 0 1024x768x24 &")
    
    def save_status_json(self, output_file="instapy_status.json"):
        """Save status information to JSON file"""
        status_data = {
            'summary': self.get_status_summary(),
            'instapy_processes': self.check_processes(),
            'firefox_processes': self.check_firefox_processes(),
            'xvfb_processes': self.check_xvfb_processes(),
            'system_info': self.get_system_info(),
            'log_files': self.get_log_files(),
            'database_info': self.get_database_info()
        }
        
        with open(output_file, 'w') as f:
            json.dump(status_data, f, indent=2, default=str)
        
        print(f"Status saved to {output_file}")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Monitor InstaPy status')
    parser.add_argument('--detailed', '-d', action='store_true', 
                       help='Show detailed information')
    parser.add_argument('--json', '-j', action='store_true',
                       help='Save status to JSON file')
    parser.add_argument('--workspace', '-w', 
                       help='Path to InstaPy workspace')
    parser.add_argument('--output', '-o', default='instapy_status.json',
                       help='Output JSON file name')
    
    args = parser.parse_args()
    
    monitor = InstaPyMonitor(args.workspace)
    
    if args.json:
        monitor.save_status_json(args.output)
    else:
        monitor.print_status(detailed=args.detailed)

if __name__ == "__main__":
    main()
