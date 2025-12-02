# Quantum
 An open-source multitool command line application. This project was made in 2022-23, when I was learning Python. Uploaded for archival. This will not be updated.

## Usage
 1. Install dependencies: `pip install -r requirements.txt`.
 2. Run the program: `python main.py`
### Available Commands:
  ```txt
  cls - Clears the console screen.
  set - Sets a specific configuration option. USAGE: set <setting_name> <value>
  list - Lists files in a given directory, the current one if not provided. USAGE: list <directory>
  tree - Displays the files in the given directory in a tree format. USAGE: tree <directory>
  copy - Copies a file to a specified destination. USAGE: <source> <destination>
  rm - Deletes the specified item. USAGE: rm <type> <path> <extra>
  mk - Creates a directory with a specified name in the current folder. USAGE: mk <type> <path>
  cd - Switches to the specified directory. USAGE: cd <path>
  ping - Pings a host and displays the response time. USAGE: ping <url>
  traceroute - Performs a traceroute to a host. USAGE: traceroute <url>
  sysinfo - Displays basic system information.
  help - Displays all commands.
 ```

## Other
Please note that the `traceroute` command will be denied permission by default on Linux systems.