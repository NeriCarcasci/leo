import os
import sys
import platform
import subprocess
import json
import importlib.util

CONFIG_DIR = os.path.expanduser("~/.leo_cli")
VENV_DIR = os.path.join(CONFIG_DIR, "venv")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def create_virtualenv():
    """Create a virtual environment for LEO CLI if it doesn't exist."""
    if not os.path.exists(VENV_DIR):
        print("🔹 Creating a virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)
    activate_venv()

def activate_venv():
    """Ensure virtual environment is activated before proceeding."""
    venv_python = os.path.join(VENV_DIR, "bin", "python") if platform.system() != "Windows" else os.path.join(VENV_DIR, "Scripts", "python.exe")
    return venv_python

def install_pip_and_questionary():
    """Ensure `pip` and `questionary` are available inside the virtual environment."""
    venv_python = activate_venv()
    pip_executable = os.path.join(VENV_DIR, "bin", "pip") if platform.system() != "Windows" else os.path.join(VENV_DIR, "Scripts", "pip.exe")

    # Ensure pip is up to date
    subprocess.run([venv_python, "-m", "ensurepip"], check=True)
    subprocess.run([pip_executable, "install", "--upgrade", "pip"], check=True)

    package_name = "questionary"
    if importlib.util.find_spec(package_name) is None:
        print(f"🔹 `{package_name}` not found. Installing it inside the virtual environment...")

        subprocess.run([pip_executable, "install", package_name], check=True)
        print(f"✅ Installed `{package_name}` inside virtual environment.\n")

create_virtualenv()  # Ensure virtual environment is set up
install_pip_and_questionary()  # Install dependencies safely inside venv
import questionary  # Now it's safe to import

def install_dependencies():
    """Install dependencies inside the virtual environment."""
    pip_executable = os.path.join(VENV_DIR, "bin", "pip") if platform.system() != "Windows" else os.path.join(VENV_DIR, "Scripts", "pip.exe")

    print("🔹 Installing dependencies inside virtual environment...")
    subprocess.run([pip_executable, "install", "-r", "requirements.txt"], check=True)
    print("✅ Dependencies installed.")

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

    install_dependencies()
    detect_and_store_os()

    print("🎉 LEO CLI is ready! Use `source ~/.leo_cli/venv/bin/activate` to start using it.")