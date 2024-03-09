import tkinter as tk
from tkinter import ttk
import psutil
import platform
import subprocess
import socket

class SystemInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Information")
        self.create_widgets()
        self.update_dynamic_info()

    def get_gpu_info_nvidia_smi(self):
        try:
            smi_output = subprocess.check_output(
                ['nvidia-smi', '--query-gpu=gpu_name,utilization.gpu,memory.total,memory.used,memory.free,temperature.gpu,power.draw,fan.speed', '--format=csv,noheader,nounits'],
                encoding='utf-8'
            )
            gpu_info = []
            for line in smi_output.strip().split("\n"):
                parts = line.split(", ")
                gpu_info.append({
                    "GPU Name": parts[0],
                    "GPU Load": f"{parts[1]}%",
                    "Total Memory": f"{parts[2]} MB",
                    "Used Memory": f"{parts[3]} MB",
                    "Free Memory": f"{parts[4]} MB",
                    "Temperature": f"{parts[5]} °C",
                    "Power Draw": f"{parts[6]} W",
                    "Fan Speed": f"{parts[7]}%"
                })
            return gpu_info
        except subprocess.CalledProcessError as e:
            print(f"Error fetching GPU information: {e}")
            return []

    def get_cpu_info(self):
        cpu_info = {
            "CPU Model": platform.processor(),
            "Physical Cores": psutil.cpu_count(logical=False),
            "Total Cores": psutil.cpu_count(logical=True),
            "Max Frequency": f"{psutil.cpu_freq().max:.2f} MHz",
            "Current Frequency": f"{psutil.cpu_freq().current:.2f} MHz",
            "CPU Usage": f"{psutil.cpu_percent()}%",
            # Additional CPU info (Placeholder for actual values)
            "Cache Size": "N/A",  # This would require specific system calls or third-party modules
            "Features": "N/A"  # Same as above
        }
        return cpu_info

    def get_ram_info(self):
        virtual_memory = psutil.virtual_memory()
        swap_memory = psutil.swap_memory()
        return {
            "Total RAM": f"{virtual_memory.total / (1024**3):.2f} GB",
            "Available RAM": f"{virtual_memory.available / (1024**3):.2f} GB",
            "Used RAM": f"{virtual_memory.used / (1024**3):.2f} GB",
            "RAM Usage Percentage": f"{virtual_memory.percent}%",
            "Total Swap": f"{swap_memory.total / (1024**3):.2f} GB",
            "Used Swap": f"{swap_memory.used / (1024**3):.2f} GB",
            "Free Swap": f"{swap_memory.free / (1024**3):.2f} GB",
            "Swap Usage Percentage": f"{swap_memory.percent}%"
        }

    def get_disk_info(self):
        disk_usage = psutil.disk_usage('/')
        disk_io = psutil.disk_io_counters()
        return {
            "Total Disk Space": f"{disk_usage.total / (1024**3):.2f} GB",
            "Used Disk Space": f"{disk_usage.used / (1024**3):.2f} GB",
            "Free Disk Space": f"{disk_usage.free / (1024**3):.2f} GB",
            "Disk Usage Percentage": f"{disk_usage.percent}%",
            "Read Count": disk_io.read_count,
            "Write Count": disk_io.write_count,
            "Bytes Read": f"{disk_io.read_bytes / (1024**2):.2f} MB",
            "Bytes Written": f"{disk_io.write_bytes / (1024**2):.2f} MB"
        }

    def get_network_info(self):
        network_info = {}
        addrs = psutil.net_if_addrs()
        stats = psutil.net_if_stats()
        io_counters = psutil.net_io_counters(pernic=True)
        for intf, addrs in addrs.items():
            intf_info = {
                "Status": "Up" if stats[intf].isup else "Down",
                "Speed": f"{stats[intf].speed} Mbps" if stats[intf].speed else "Unknown",
                "Packets Sent": io_counters[intf].packets_sent,
                "Packets Received": io_counters[intf].packets_recv,
                "Bytes Sent": f"{io_counters[intf].bytes_sent / (1024**2):.2f} MB",
                "Bytes Received": f"{io_counters[intf].bytes_recv / (1024**2):.2f} MB",
            }
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    intf_info["IPv4"] = addr.address
                elif addr.family == socket.AF_INET6:
                    intf_info["IPv6"] = addr.address
                elif addr.family == psutil.AF_LINK:
                    intf_info["MAC"] = addr.address
            network_info[intf] = intf_info
        return network_info

    def create_widgets(self):
        tab_control = ttk.Notebook(self.root)
        
        # Tabs
        self.gpu_tab = ttk.Frame(tab_control)
        self.cpu_tab = ttk.Frame(tab_control)
        self.ram_tab = ttk.Frame(tab_control)
        self.network_tab = ttk.Frame(tab_control)
        self.disk_tab = ttk.Frame(tab_control)

        tab_control.add(self.gpu_tab, text='GPU')
        tab_control.add(self.cpu_tab, text='CPU')
        tab_control.add(self.ram_tab, text='RAM')
        tab_control.add(self.network_tab, text='Network')
        tab_control.add(self.disk_tab, text='Disk')

        tab_control.pack(expand=1, fill="both")
        self.populate_gpu_tab()
        self.populate_cpu_tab()
        self.populate_ram_tab()
        self.populate_network_tab()
        self.populate_disk_tab()

    def populate_tab(self, tab, info):
        for widget in tab.winfo_children():
            widget.destroy()
        for key, value in info.items():
            ttk.Label(tab, text=f"{key}: {value}").pack(anchor='w')

    def populate_gpu_tab(self):
        gpu_info = self.get_gpu_info_nvidia_smi()
        if gpu_info:
            for gpu in gpu_info:
                self.populate_tab(self.gpu_tab, gpu)
        else:
            ttk.Label(self.gpu_tab, text="No GPU information available").pack(anchor='w')

    def populate_cpu_tab(self):
        cpu_info = self.get_cpu_info()
        self.populate_tab(self.cpu_tab, cpu_info)

    def populate_ram_tab(self):
        ram_info = self.get_ram_info()
        self.populate_tab(self.ram_tab, ram_info)

    def populate_disk_tab(self):
        disk_info = self.get_disk_info()
        self.populate_tab(self.disk_tab, disk_info)

    def populate_network_tab(self):
        network_info = self.get_network_info()
        for interface, info in network_info.items():
            interface_frame = ttk.LabelFrame(self.network_tab, text=f"Interface: {interface}")
            interface_frame.pack(fill="both", expand=True, padx=10, pady=5)
            for key, value in info.items():
                ttk.Label(interface_frame, text=f"{key}: {value}").pack(anchor='w')

    def update_dynamic_info(self):
        self.populate_cpu_tab()
        self.populate_ram_tab()
        self.populate_disk_tab()
        # Update every 5 seconds
        self.root.after(5000, self.update_dynamic_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemInfoApp(root)
    root.mainloop()
