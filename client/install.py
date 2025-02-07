import os
import sys
import platform
import subprocess
import json
import importlib.util

CONFIG_DIR = os.path.expanduser("~/.leo_cli")
VENV_DIR = os.path.join(CONFIG_DIR, "venv")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def install_pip_and_questionary():
    """Ensure `pip` and `questionary` are available before running setup."""
    package_name = "questionary"
    
    if importlib.util.find_spec(package_name) is None:
        print(f"🔹 `{package_name}` not found. Installing it first...")

        subprocess.run([sys.executable, "-m", "ensurepip"], check=True)
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run([sys.executable, "-m", "pip", "install", package_name], check=True)
        
        print(f"✅ Installed `{package_name}`. Restarting installation...\n")
        os.execv(sys.executable, [sys.executable] + sys.argv)  # Restart the script

install_pip_and_questionary()  # Ensure dependencies before running anything else
import questionary  # Now it's safe to import

def create_virtualenv():
    """Create a virtual environment for LEO CLI if it doesn't exist."""
    if not os.path.exists(VENV_DIR):
        print("🔹 Creating a virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)
    activate_venv()

def activate_venv():
    """Activate the virtual environment."""
    if platform.system() == "Windows":
        activate_script = os.path.join(VENV_DIR, "Scripts", "activate")
    else:
        activate_script = os.path.join(VENV_DIR, "bin", "activate")
    
    print(f"🔹 Virtual environment activated: {VENV_DIR}")
    return activate_script

def install_dependencies():
    """Install dependencies inside the virtual environment."""
    pip_executable = os.path.join(VENV_DIR, "bin", "pip") if platform.system() != "Windows" else os.path.join(VENV_DIR, "Scripts", "pip")
    
    print("🔹 Installing dependencies...")
    subprocess.run([pip_executable, "install", "-r", "requirements.txt"], check=True)
    print("✅ Dependencies installed.")

def add_to_path():
    """Ask user to add LEO CLI to their system PATH."""
    cli_path = os.path.join(VENV_DIR, "bin", "leo.py") if platform.system() != "Windows" else os.path.join(VENV_DIR, "Scripts", "leo.py")

    add_to_path = questionary.confirm("Would you like to add LEO CLI to your system PATH?").ask()
    if add_to_path:
        if platform.system() == "Windows":
            path_command = f'setx PATH "%PATH%;{VENV_DIR}\\Scripts"'
        else:
            path_command = f'echo "export PATH={VENV_DIR}/bin:$PATH" >> ~/.bashrc && source ~/.bashrc'

        subprocess.run(path_command, shell=True, check=True)
        print("✅ LEO CLI added to PATH. Restart your shell to apply changes.")

def detect_and_store_os():
    """Detect the OS and store it in the config file."""
    detected_os = platform.system()
    config_data = {"os": detected_os}

    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w") as file:
        json.dump(config_data, file, indent=4)

    print(f"✅ OS detected: {detected_os}. Stored in {CONFIG_FILE}")

if __name__ == "__main__":
    print("🚀 Setting up LEO CLI...")

    create_virtualenv()
    install_dependencies()
    detect_and_store_os()
    add_to_path()

    print("🎉 LEO CLI is ready! You can now use `leo.py` from the terminal.")