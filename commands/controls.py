import os
from rich.console import Console
import json

SETTINGS_FILE = 'settings.json'

console = Console()

settings = {
    'show_logo'
}

def initialize_settings():
    """Initializes the settings with default values if not present."""
    default_settings = {
        "show_logo": True
    }
    
    if not os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'w') as file:
            json.dump(default_settings, file, indent=4)
            
    with open(SETTINGS_FILE, 'r') as file:
        return json.load(file)
    
def save_settings(settings):
    """Saves the settings to the settings.json file."""
    with open(SETTINGS_FILE, 'w') as file:
        json.dump(settings, file, indent=4)
        
def load_settings():
    """Loads the settings from the settings.json file, ensuring correct types."""
    if not os.path.exists(SETTINGS_FILE):
        initialize_settings()

    with open(SETTINGS_FILE, 'r') as f:
        settings = json.load(f)
    
    if 'show_logo' in settings:
        if isinstance(settings['show_logo'], str):
            settings['show_logo'] = settings['show_logo'].lower() in ['true', '1']
        elif isinstance(settings['show_logo'], bool):
            settings['show_logo'] = settings['show_logo']
    
    return settings

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("[blue]Screen cleared![/blue]")
    
    if load_settings()['show_logo']:
        from main import logo 
        logo()

def toggle_logo_display():
    """Toggles the display of the logo after clearing the screen."""
    settings['show_logo'] = not settings['show_logo']
    state = "enabled" if settings['show_logo'] else "disabled"
    console.print(f"[green]Logo display after clearing is now {state}.[/green]")

def set_command(args):
    """Sets a specific configuration option."""
    if len(args) != 2:
        console.print("[red]Usage: set <setting_name> <value>[/red]")
        return
    
    setting_name, setting_value = args
    settings = load_settings()
    
    if setting_name not in settings:
        console.print(f"[red]Setting '{setting_name}' does not exist.[/red]")
        return
    
    if setting_value.lower() in ['true', '1']:
        settings[setting_name] = True
    elif setting_value.lower() in ['false', '0']:
        settings[setting_name] = False
    elif setting_value.lower() in ['3']:
        settings[setting_name] = setting_value
    
    save_settings(settings)
    console.print(f"[green]Setting '{setting_name}' updated to '{settings[setting_name]}'[/green]")


def get_commands():
    """Returns a dictionary of commands in this module."""
    return {
        'cls': {'func': clear_screen, 'args': None},
        'set': {'func': set_command, 'args': 'required'}
    }
