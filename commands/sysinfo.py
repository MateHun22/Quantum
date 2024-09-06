import platform
import psutil
from rich.console import Console
import cpuinfo

console = Console()

def system_info(args=None):
    """Displays basic system information."""
    
    try:
        os_info = platform.system()
        os_release = platform.release()
        os_version = platform.version()
        
        
        
        
        cpu_info = cpuinfo.get_cpu_info()
        cpu_brand = cpu_info['brand_raw']
        
        
        machine_info = platform.machine()
        
        total_memory = psutil.virtual_memory().total // (1024 ** 3)
        available_memory = psutil.virtual_memory().available // (1024 ** 3)
        cpu_cores = psutil.cpu_count(logical=True)
        cpu_physical_cores = psutil.cpu_count(logical=False)
        
        disk_usage = psutil.disk_usage('/')
        total_storage = disk_usage.total // (1024 ** 3)
        used_storage = disk_usage.used // (1024 ** 3)
        free_storage = disk_usage.free // (1024 ** 3)
        
        console.print("[bold green]System Information:[/bold green]")
        console.print(f"    [cyan]Operating System:[/cyan] {os_info} {os_release} (Version: {os_version})")
        console.print(f"    [cyan]Machine Architecture:[/cyan] {machine_info}")
        console.print("  [bold green]CPU Information:[/bold green]")
        console.print(f"    [cyan]CPU:[/cyan] {cpu_brand}")
        console.print(f"    [cyan]CPU Cores:[/cyan] {cpu_cores} (Physical: {cpu_physical_cores})")
        console.print("  [bold green]RAM Information:[/bold green]")
        console.print(f"    [cyan]Total RAM:[/cyan] {total_memory} GB")
        console.print(f"    [cyan]Availale RAM:[/cyan] {available_memory} GB")
        console.print("  [bold green]Disk Information:[/bold green]")
        console.print(f"    [cyan]Total Storage:[/cyan] {total_storage} GB")
        console.print(f"    [cyan]Used Storage:[/cyan] {used_storage} GB")
        console.print(f"    [cyan]Free Storage:[/cyan] {free_storage} GB")
    
    except Exception as e:
        console.print(f"[red]Error retrieving system information: {e}[/red]")
        
def get_commands():
    return {
    "sysinfo": {"func": system_info, "args": "None"},
    }