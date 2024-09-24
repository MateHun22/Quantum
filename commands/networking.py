import scapy.all as scapy
from ping3 import ping
from rich.console import Console

console = Console()

def ping_host(args):
    """Pings a host and displays the response time. USAGE: ping <url>"""
    
    host = args[0]
    
    try:
        response = ping(host)
        if response is None:
            console.print(f"[red]No response from {host}[/red]")
        else:
            console.print(f"[green]Ping to {host}: {response * 1000:.2f} ms[/green]")
    except Exception as e:
        console.print(f"[red]Error pinging {host}: {e}[/red]")
        
def traceroute_host(args):
    """Performs a traceroute to a host. USAGE: traceroute <url>"""

    host = args[0]
    try:
        console.print(f"[green]Traceroute to {host}:[/green]")
        traceroute = scapy.traceroute(host, )
        for pkt in traceroute[0]:
            console.print(f"  [cyan]Hop {pkt[0]}:[/cyan] {pkt[1]} ({pkt[2]})")
    except Exception as e:
        console.print(f"[red]Error performing traceroute to {host}: {e}[/red]")
        
def get_commands():
    return {
    "ping": {"func": ping_host, "args": "required"},
    "traceroute": {"func": traceroute_host, "args": "required"},
    }