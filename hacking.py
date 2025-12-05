import time
import random
import os
from colorama import Fore, Style, init
init(autoreset=True)

pairs = {
    "Vieira": "Lara",
    "Rui": "Jota",
    "Xavi": "Vitoria",
    "Afonso": "Rafa",
    "Diogo": "[FILE CORRUPTED]",
    "Rafa": "Beatriz",
    "Jota": "Xavi",
    "Vitória": "Ana Gil",
    "Beatriz": "Isabel",
    "Lara": "Rui",
    "Isabel": "Diogo",
    "Ana Gil": "[FILE CORRUPTED]"
}

def boot_sequence():
    msgs = [
        "Loading system modules...",
        "Synchronizing components...",
        "Checking integrity...",
        "Initializing sequence...",
        "Adjusting parameters...",
    ]
    for m in msgs:
        print(Fore.CYAN + m)
        time.sleep(0.6)

def glitch_flash():
    for _ in range(4):
        print(Fore.RED + "### ANOMALY DETECTED ###")
        time.sleep(0.15)
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(0.05)

def noise(lines=45, width=70, speed=0.015):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#%&@*"
    for _ in range(lines):
        print(Fore.GREEN + "".join(random.choice(chars) for _ in range(width)))
        time.sleep(speed)

def bar(text, duration=1.5):
    print(Fore.CYAN + text)
    bar = ""
    for _ in range(30):
        bar += "█"
        print(Fore.GREEN + bar, end="\r")
        time.sleep(duration / 30)
    print()

def reveal():
    print(Fore.CYAN + "\nReanalyzing data packets...\n")
    time.sleep(1)

    for k, v in pairs.items():
        print(Fore.YELLOW + f"{k} → ", end="")
        time.sleep(0.35)

        if "CORRUPTED" in v:
            print(Fore.RED + "[FILE CORRUPTED]")
            time.sleep(0.25)
            glitch_flash()
        else:
            scrambled = "".join(
                c if random.random() > 0.2 else random.choice("#$%&?")
                for c in v
            )
            print(Fore.GREEN + scrambled)
        time.sleep(0.3)

    print(Fore.MAGENTA + "\nSequence complete.\n")

# EXECUTION
os.system("cls" if os.name == "nt" else "clear")

boot_sequence()
bar("Processing...")
noise()
glitch_flash()
bar("Reconstructing...")
noise(lines=25, speed=0.02)
reveal()
