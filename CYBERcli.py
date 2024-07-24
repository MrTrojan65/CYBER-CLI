import cmd
import asyncio
import logging
import os
import shutil
import subprocess

# Configure logging
logging.basicConfig(filename='cli.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Color themes for terminal output
theme = {
    'okgreen': '\033[92m',
    'warning': '\033[93m',
    'error': '\033[91m',
    'reset': '\033[0m',
    'bold': '\033[1m',
    'underlined': '\033[4m'
}

class TermuxCLI(cmd.Cmd):
    intro = f"""
{theme['bold']}{theme['okgreen']}


___  _  _  ____  ____  ____     ___  __    ____
 / __)( \/ )(  _ \( ___)(  _ \   / __)(  )  (_  _)
( (__  \  /  ) _ < )__)  )   /  ( (__  )(__  _)(_
 \___) (__) (____/(____)(_)\_)   \___)(____)(____)
    

{theme['reset']}
{theme['bold']}{theme['okgreen']}Welcome to CYBER CLI - Your HACKING Toolbox{theme['reset']}
    """
    prompt = f'{theme["bold"]}{theme["okgreen"]}CYBER-CLI>>>{theme["reset"]} '
    file = None
    loop = asyncio.get_event_loop()
    current_directory = os.getcwd()

    async def run_command(self, command):
        process = await asyncio.create_subprocess_shell(command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        return stdout.decode(), stderr.decode()

    def do_list_tools(self, arg):
        'List all available tools and their descriptions'
        tool_list = {
            'nmap': 'Network scanning tool for discovering hosts and services.',
            'sqlmap': 'Automated tool for SQL injection and database takeover.',
            'msfconsole': 'Metasploit Framework Console for penetration testing.',
            'nikto': 'Web server scanner to find vulnerabilities.',
            'john': 'Password cracking tool.',
            'hydra': 'Password cracking tool for various protocols.',
            'aircrack': 'Wi-Fi network cracking tool.',
            'ettercap': 'Network sniffing and man-in-the-middle attack tool.',
            'reaver': 'Tool for brute-forcing WPA/WPA2 handshakes.',
            'wifite': 'Automated wireless attack tool.',
            'gobuster': 'Directory and file brute-forcing tool.',
            'curl': 'Command-line tool for transferring data with URLs.',
            'wireshark': 'Network protocol analyzer.',
            'msfd': 'Metasploit Framework Daemon.',
            'burp': 'Burp Suite for web application security testing.',
            'zap': 'OWASP ZAP for web application security testing.',
            'netcat': 'Network utility for reading and writing data across network connections.'
        }

        print(f'{theme["bold"]}{theme["okgreen"]}Available Tools:{theme["reset"]}')
        for tool, description in tool_list.items():
            print(f'{theme["bold"]}{tool}{theme["reset"]}: {description}')

    def do_ls(self, arg):
        'List directory contents'
        try:
            files = os.listdir(self.current_directory)
            print(f'{theme["okgreen"]}Contents of {self.current_directory}:{theme["reset"]}')
            for file in files:
                print(file)
            logging.info(f'Listed contents of directory: {self.current_directory}')
        except Exception as e:
            print(f'{theme["error"]}Error: {e}{theme["reset"]}')
            logging.error(f'Error listing directory contents: {e}')

    def do_cd(self, arg):
        'Change directory: cd <directory>'
        try:
            if not arg:
                print(f'{theme["error"]}Usage: cd <directory>{theme["reset"]}')
                return
            new_dir = os.path.join(self.current_directory, arg)
            if os.path.isdir(new_dir):
                self.current_directory = new_dir
                print(f'{theme["okgreen"]}Changed directory to: {self.current_directory}{theme["reset"]}')
                logging.info(f'Changed directory to: {self.current_directory}')
            else:
                print(f'{theme["error"]}Directory not found: {arg}{theme["reset"]}')
                logging.error(f'Directory not found: {arg}')
        except Exception as e:
            print(f'{theme["error"]}Error: {e}{theme["reset"]}')
            logging.error(f'Error changing directory: {e}')

    def do_mkdir(self, arg):
        'Make directory: mkdir <directory>'
        try:
            if not arg:
                print(f'{theme["error"]}Usage: mkdir <directory>{theme["reset"]}')
                return
            new_dir = os.path.join(self.current_directory, arg)
            os.makedirs(new_dir, exist_ok=True)
            print(f'{theme["okgreen"]}Created directory: {new_dir}{theme["reset"]}')
            logging.info(f'Created directory: {new_dir}')
        except Exception as e:
            print(f'{theme["error"]}Error: {e}{theme["reset"]}')
            logging.error(f'Error creating directory: {e}')

    def do_rmdir(self, arg):
        'Remove directory: rmdir <directory>'
        try:
            if not arg:
                print(f'{theme["error"]}Usage: rmdir <directory>{theme["reset"]}')
                return
            dir_path = os.path.join(self.current_directory, arg)
            shutil.rmtree(dir_path)
            print(f'{theme["okgreen"]}Removed directory: {dir_path}{theme["reset"]}')
            logging.info(f'Removed directory: {dir_path}')
        except Exception as e:
            print(f'{theme["error"]}Error: {e}{theme["reset"]}')
            logging.error(f'Error removing directory: {e}')

    def do_rm(self, arg):
        'Remove file: rm <file>'
        try:
            if not arg:
                print(f'{theme["error"]}Usage: rm <file>{theme["reset"]}')
                return
            file_path = os.path.join(self.current_directory, arg)
            os.remove(file_path)
            print(f'{theme["okgreen"]}Removed file: {file_path}{theme["reset"]}')
            logging.info(f'Removed file: {file_path}')
        except Exception as e:
            print(f'{theme["error"]}Error: {e}{theme["reset"]}')
            logging.error(f'Error removing file: {e}')

    def do_clear(self, arg):
        'Clear the screen'
        os.system('cls' if os.name == 'nt' else 'clear')
        logging.info('Cleared the screen.')

    def do_exit(self, arg):
        'Exit the CLI'
        print('Exiting Termux CLI.')
        return True

    def do_nmap(self, arg):
        'Run nmap scan: nmap <options>'
        command = f'nmap {arg}'
        print(f'Running: {command}')
        logging.info(f'Running nmap with options: {arg}')
        asyncio.run(self.run_tool(command))

    def do_sqlmap(self, arg):
        'Run sqlmap: sqlmap <options>'
        command = f'sqlmap {arg}'
        print(f'Running: {command}')
        logging.info(f'Running sqlmap with options: {arg}')
        asyncio.run(self.run_tool(command))

    def do_msfconsole(self, arg):
        'Run msfconsole'
        command = 'msfconsole'
        print(f'Running: {command}')
        logging.info('Running msfconsole')
        subprocess.call(command, shell=True)

    def do_nikto(self, arg):
        'Run nikto scan: nikto <options>'
        command = f'nikto {arg}'
        print(f'Running: {command}')
        logging.info(f'Running nikto with options: {arg}')
        asyncio.run(self.run_tool(command))

    def do_john(self, arg):
        'Run John the Ripper: john <options>'
        command = f'john {arg}'
        print(f'Running: {command}')
        logging.info(f'Running john with options: {arg}')
        asyncio.run(self.run_tool(command))

    def do_hydra(self, arg):
        'Run Hydra: hydra <options>'
        command = f'hydra {arg}'
        print(f'Running: {command}')
        logging.info(f'Running hydra with options: {arg}')
        asyncio.run(self.run_tool(command))

    def do_aircrack(self, arg):
        'Run Aircrack-ng: aircrack-ng <options>'
        command = f'aircrack-ng {arg}'
        print(f'Running: {command}')
        logging.info(f'Running aircrack-ng with options: {arg}')
        asyncio.run(self.run_tool(command))

    def do_ettercap(self, arg):
        'Run Ettercap: ettercap <options>'
        command = f'ettercap {arg}'
        print(f'Running: {command}')
        logging.info(f'Running ettercap with options: {arg}')
        asyncio.run(self.run_tool(command))

    def do_reaver(self, arg):
        'Run Reaver: reaver <options>'
        command = f'reaver {arg}'
        print(f'Running: {command}')
        logging.info(f'Running reaver with options: {arg}')
        asyncio.run(self.run_tool(command))

    def do_wifite(self, arg):
        'Run Wifite: wifite <options>'
        command = f'wifite {arg}'
        print(f'Running: {command}')
        logging.info(f'Running wifite with options: {arg}')
        asyncio.run(self.run_tool(command))

    def do_gobuster(self, arg):
        'Run Gobuster: gobuster <options>'
        command = f'gobuster {arg}'
        print(f'Running: {command}')
        logging.info(f'Running gobuster with options: {arg}')
        asyncio.run(self.run_tool(command))

    def do_curl(self, arg):
        'Run Curl: curl <options>'
        command = f'curl {arg}'
        print(f'Running: {command}')
        logging.info(f'Running curl with options: {arg}')
        asyncio.run(self.run_tool(command))

    def do_wireshark(self, arg):
        'Run Wireshark: wireshark <options>'
        command = f'wireshark {arg}'
        print(f'Running: {command}')
        logging.info(f'Running wireshark with options: {arg}')
        asyncio.run(self.run_tool(command))

    def do_msfd(self, arg):
        'Run Metasploit Framework Daemon: msfd <options>'
        command = f'msfd {arg}'
        print(f'Running: {command}')
        logging.info(f'Running msfd with options: {arg}')
        asyncio.run(self.run_tool(command))

    def do_burp(self, arg):
        'Run Burp Suite: burp <options>'
        command = f'burp {arg}'
        print(f'Running: {command}')
        logging.info(f'Running burp with options: {arg}')
        asyncio.run(self.run_tool(command))

    def do_zap(self, arg):
        'Run OWASP ZAP: zap <options>'
        command = f'zap {arg}'
        print(f'Running: {command}')
        logging.info(f'Running zap with options: {arg}')
        asyncio.run(self.run_tool(command))

    def do_netcat(self, arg):
        'Run Netcat: nc <options>'
        command = f'nc {arg}'
        print(f'Running: {command}')
        logging.info(f'Running netcat with options: {arg}')
        asyncio.run(self.run_tool(command))

    async def run_tool(self, command):
        stdout, stderr = await self.run_command(command)
        if stdout:
            print(f'{theme["okgreen"]}{stdout}{theme["reset"]}')
        if stderr:
            print(f'{theme["error"]}{stderr}{theme["reset"]}')
        logging.info(f'Command output: {stdout}')
        logging.error(f'Command error: {stderr}')

if __name__ == '__main__':
    TermuxCLI().cmdloop()
