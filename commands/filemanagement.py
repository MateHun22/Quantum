import os
import shutil
from rich.console import Console
from rich.tree import Tree

console = Console()

def list_files(args):
    """Lists files in a given directory, the current one if not provided."""
    target_dir = args[0] if args else os.getcwd()
    
    try:
        items = os.listdir(target_dir)
        console.print(f"[cyan]Contents of {target_dir}:[/cyan]")
        for item in items:
            item_path = os.path.join(target_dir, item)
        
            if os.path.isdir(item_path):
                console.print(f"[📁] {item}")
            elif os.path.isfile(item_path):
                console.print(f"[📄] {item}")
            else:
                console.print(f"[yellow]Unknown item type: {item}[/yellow]")
    except Exception as e:
        console.print(f"[red]Error listing files: {e}[/red]")
        
def show_tree(args):
    """Displays the files in the given directory in a tree format."""
    target_dir = args[0] if args else os.getcwd()
    
    try:
        tree = Tree(f"[bold cyan]{target_dir}[/bold cyan]")
        for root, dirs, files in os.walk(target_dir):
            for dir in dirs:
                sub_tree = tree.add(f"[cyan][📁] {dir}[/cyan]")
                for sub_file in os.listdir(os.path.join(root, dir)):
                    sub_tree.add(f"[white][📄] {sub_file}[/white]")
            break
            
        for file in files:
            tree.add(f"[white][📄] {file}[/white]")
            break
    
        console.print(tree)
    except Exception as e:
        console.print(f"[red]Error displaying tree: {e}[/red]")
        
def copy_file(args):
    """Copies a file to a specified destination."""
    
    if len(args) < 2:
        console.print("[red]Usage: copy <source> <destination>.[/red]")
        return
    
    source = args[0]
    destination = args[1]
    
    try:
        shutil.copy(source, destination)
        console.print(f"[green]File copied from {source} to {destination}.[/green]")
    except Exception as e:
        console.print(f"[red]Error copying file: {e}[/red]")
        
        
def get_commands():
    return {
    "list": {"func": list_files, "args": "optional"},
    "tree": {"func": show_tree, "args": "optional"},
    "copy": {"func": copy_file, "args": "required"},
    }