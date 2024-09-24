import os
import shutil
from rich.console import Console
from rich.tree import Tree
from rich.prompt import Prompt

console = Console()

def list_files(args):
    """Lists files in a given directory, the current one if not provided. USAGE: list <directory>"""
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
    """Displays the files in the given directory in a tree format. USAGE: tree <directory>"""
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
    """Copies a file to a specified destination. USAGE: <source> <destination>"""
    
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
        
def delete_file(args):
    """Deletes the specified item. USAGE: rm <type> <path> <extra>"""

    type = args[0]
    path = args[1]
    
    if len(args) > 2:
        extra = args[2]

    else:
        extra = None

    try:
        if type == "file":
            if extra == "--c":
                confirm = Prompt.ask(f"Are you sure you want to remove {path}?",show_choices=True, choices=["y","n"])
                if confirm == "y":
                    os.remove(path)
                    console.print("[green]Successfully deleted file.[/green]")
                elif confirm == "n":
                    console.print("[red]Deletion aborted.[/red]")
                else:
                    console.print("[red]Enter a valid value.[/red]")
            elif extra is None:
                os.remove(path)
                console.print("[green]Successfully deleted file.[/green]")
        elif type == "dir":
            if extra == "--c":
                confirm = Prompt.ask(f"Are you sure you want to remove {path}?",show_choices=True, choices=["y","n"])

                if confirm == "y":
                    os.rmdir(path)
                    console.print("[green]Successfully deleted directory.[/green]")
                elif confirm == "n":
                    console.print("[red]Deletion aborted.[/red]")
                else:
                    console.print("[red]Enter a valid value.[/red]")
            elif extra is None:
                os.rmdir(path)
                console.print("[green]Successfully deleted directory.[/green]")
    except Exception as e:
        console.print(f"[red]Error deleting item: {e}[/red]")

def make_item(args):
    """Creates a directory with a specified name in the current folder. USAGE: mk <type> <path>"""

    type = args[0]
    path = args[1]

    try:
        if type == "dir":
            os.mkdir(path)
            console.print("[green]Successfully created directory.[/green]")
        elif type == "file":
            with open(path, 'w') as file:
                file.write("")
            console.print("[green]Successfully created file.[/green]")
        else:
            console.print("[red]Invalid type.[/red]")
    except Exception as e:
        print(f"[red]Couldn't create file: {e}[/red]")
    
def change_dir(args):
    """Switches to the specified directory. USAGE: cd <path>"""

    path = args[0]

    try:
        os.chdir(path)
    except Exception as e:
        console.print(f"[red]Couldn't change directory: {e}.[/red]")
        
        
def get_commands():
    return {
    "list": {"func": list_files, "args": "optional"},
    "tree": {"func": show_tree, "args": "optional"},
    "copy": {"func": copy_file, "args": "required"},
    "rm": {"func": delete_file, "args": "required"},
    "mk": {"func": make_item, "args": "required"},
    "cd": {"func": change_dir, "args": "required"}
    }