import os

# Define project structure
project_structure = {
    "client": [
        "leo.py",
        "config.py",
        "prompts.py",
        "executor.py",
        "logger.py",
        "secrets.py",
        "requirements.txt",
        "README.md"
    ],
    "server": [
        "main.py",
        "routes.py",
        "vertex_ai.py",
        "execution_engine.py",
        "db.py",
        "models.py",
        "logging.py",
        "security.py",
        "secrets.py",
        "config.py",
        "requirements.txt",
        "README.md"
    ],
    "infra/terraform": [
        "main.tf",
        "gke.tf",
        "vertex_ai.tf",
        "cloud_sql.tf",
        "storage.tf",
        "secret_manager.tf",
        "outputs.tf",
        "providers.tf",
        "variables.tf",
        "README.md"
    ],
    "infra/kubernetes": [
        "deployment.yaml",
        "service.yaml",
        "ingress.yaml",
        "secrets.yaml",
        "configmap.yaml",
        "README.md"
    ],
    "infra/github-actions": [
        "deploy.yml",
        "test.yml",
        "terraform.yml",
        "README.md"
    ],
    "infra/docker": [
        "Dockerfile",
        "entrypoint.sh",
        "docker-compose.yml",
        "README.md"
    ],
    "infra/monitoring": [
        "cloud_logging.tf",
        "alerting.tf",
        "README.md"
    ],
}

# Function to create directories and files
def setup_project():
    for folder, files in project_structure.items():
        os.makedirs(folder, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder, file)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    if file.endswith(".py"):
                        f.write("# " + file + "\n")  # Add placeholder comment
                    elif file.endswith(".yaml"):
                        f.write("# YAML Configuration\n")
                    elif file.endswith(".tf"):
                        f.write("# Terraform Configuration\n")
                    elif file.endswith(".sh"):
                        f.write("#!/bin/bash\n")  # Ensure scripts are bash compatible
                    elif file.endswith(".txt"):
                        f.write("# Dependencies list\n")
                    elif file == "README.md":
                        f.write(f"# {folder.split('/')[-1].capitalize()} \n\n")
                        f.write("This directory contains configurations for " + folder.split("/")[-1] + ".\n")

    print("✅ Project structure created successfully!")

# Run setup
if __name__ == "__main__":
    setup_project()
