import os
from rich.console import Console

console = Console()

settings = {
    'show_logo': True,
}

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("[cyan]Screen cleared![/cyan]")
    
    if settings['show_logo']:
        from main import logo 
        logo()

def toggle_logo_display():
    """Toggle the display of the logo after clearing the screen."""
    settings['show_logo'] = not settings['show_logo']
    state = "enabled" if settings['show_logo'] else "disabled"
    console.print(f"[yellow]Logo display after clearing is now {state}.[/yellow]")

def set_command(args):
    """Set a specific configuration option."""
    if len(args) < 2:
        console.print("[red]The 'set' command requires two arguments: option and value.[/red]")
        return

    option, value = args[0].lower(), args[1].lower()

    if option in settings:
        if value in ['true', '1']:
            settings[option] = True
        elif value in ['false', '0']:
            settings[option] = False
        else:
            console.print(f"[red]Invalid value '{value}' for setting '{option}'. Use 'true/1' or 'false/0'.[/red]")
            return
        console.print(f"[green]Setting '{option}' updated to '{value}'.[/green]")
    else:
        console.print(f"[red]Unknown setting '{option}'. Available settings: {', '.join(settings.keys())}[/red]")

def get_commands():
    """Return a dictionary of commands in this module."""
    return {
        'cls': {'func': clear_screen, 'args': None},
        'set': {'func': set_command, 'args': 'required'}
    }
