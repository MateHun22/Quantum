import os
import importlib
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
import readline

console = Console()

commands = {}
command_history = []

def logo():
    """Displays the logo screen."""
    
    logo_text = Text("""
    #####################
    *      Quantum      *    
    #####################
    """, style="bold cyan")
    console.print(Panel(logo_text, border_style="green"))
    
def show_help():
    """Displays available commands."""
    help_text = Text("Available Commands:\n", style="bold yellow")
    for command, meta in commands.items():
        command_doc = meta['func'].__doc__ or "No description available."
        help_text.append(f"  {command} - {command_doc}\n")
    console.print(Panel(help_text, style="magenta"))

def load_cogs():
    """Loads the modules from 'commands' directory."""
    for filename in os.listdir('commands'):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = f'commands.{filename[:-3]}'
            module = importlib.import_module(module_name)
            commands.update(module.get_commands())
            
def parse_command_input(user_input):
    """Parses the user input into a command and its arguments."""
    parts = user_input.split()
    command = parts[0]
    args = parts[1:]
    return command, args
            
def main():
    logo()
    load_cogs()
    
    while True:
        user_input = Prompt.ask("[blue]Quantum >> [/blue]").strip().lower()
        command_history.append(user_input)
        readline.add_history(user_input)

        command, args = parse_command_input(user_input)

        if command in commands:
            command_meta = commands[command]

            if command_meta['args'] == 'required' and len(args) == 0:
                console.print(f"[red]Command '{command}' requires arguments. Type 'help' for usage details.[/red]")
                continue
            elif command_meta['args'] is None and len(args) > 0:
                console.print(f"[red]Command '{command}' does not accept any arguments. Type 'help' for usage details.[/red]")
                continue

            try:
                if command_meta['args'] is None:
                    command_meta['func']()
                else:
                    command_meta['func'](args)
            except Exception as e:
                console.print(f"[red]Error executing command '{command}': {str(e)}[/red]")
        elif command == 'help':
            show_help()
        elif command == 'exit':
            break
        else:
            console.print("[red]Unknown command. Type 'help' to see available commands.[/red]")
            
if __name__ == '__main__':
    main()