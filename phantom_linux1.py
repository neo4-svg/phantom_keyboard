#!/usr/bin/env python3
# Phantom Keyboard - Pure Python Linux Version
# Works on all distros (Fedora, Ubuntu, Arch, Debian)

from pynput import keyboard
import random, time, yaml, os
from colorama import Fore, Style

CONFIG_FILE = "phantom_config.yaml"

def ask_questions():
    print(Fore.CYAN + "=== Phantom Keyboard Setup ===" + Style.RESET_ALL)
    chaos = input(Fore.YELLOW + "Choose chaos level (low/medium/high): " + Style.RESET_ALL)
    ghost_freq = int(input(Fore.YELLOW + "Ghost keystroke frequency (1-10): " + Style.RESET_ALL))
    stealth = input(Fore.YELLOW + "Enable stealth mode? (y/n): " + Style.RESET_ALL)
    
    config = {
        "chaos": chaos,
        "ghost_freq": ghost_freq,
        "stealth": stealth.lower() == "y"
    }
    with open(CONFIG_FILE, "w") as f:
        yaml.dump(config, f)
    return config

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return yaml.safe_load(f)
    return ask_questions()

def run_phantom(config):
    print(Fore.GREEN + f"Phantom Keyboard running with chaos={config['chaos']}..." + Style.RESET_ALL)

    def on_press(key):
        try:
            print(Fore.WHITE + f"Key pressed: {key.char}" + Style.RESET_ALL)
            
            # Phantom jitter
            if random.random() < 0.3:
                delay = random.uniform(0.05, 0.2)
                time.sleep(delay)
            
            # Ghost keystroke
            if random.randint(1,10) <= config['ghost_freq']:
                ghost = random.choice(['x','z','q'])
                print(Fore.RED + f"Injected phantom key: {ghost}" + Style.RESET_ALL)
            
            # Fake typo (wrong key then correction)
            if config['chaos'] == "high" and random.random() < 0.2:
                typo = random.choice(['a','s','d'])
                print(Fore.MAGENTA + f"Fake typo injected: {typo}" + Style.RESET_ALL)
                time.sleep(0.1)
                print(Fore.GREEN + f"Auto-corrected typo" + Style.RESET_ALL)

        except AttributeError:
            print(Fore.MAGENTA + f"Special key: {key}" + Style.RESET_ALL)

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    config = load_config()
    run_phantom(config)
