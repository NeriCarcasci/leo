# 🦁 LEO - AI-Powered Command Line Assistant 🚀

## 📝 Overview
LEO is an intelligent command-line assistant that transforms **natural language prompts** into accurate **system commands** using a **cloud-based Large Language Model (LLM)**.  

Designed for **developers, sysadmins, and power users**, LEO provides **automated command execution, security, and logging**, making it an ideal assistant for **system administration, cloud operations, and development workflows**.  

## 📂 Repository Structure
LEO is now divided into three separate repositories for **better organization and scalability**:

| Repository  | Description |
|------------|------------|
| **[leo](https://github.com/NeriCarcasci/leo)** | Main repository containing **documentation, testing, and project tracking**. |
| **[leo-local](https://github.com/NeriCarcasci/leo-local)** | CLI tool for executing LEO commands locally. |
| **[leo-cloud](https://github.com/NeriCarcasci/leo-cloud)** | Server-side execution engine, backend API, and cloud infrastructure. |

Each repository is independently maintained but works together as part of the **LEO ecosystem**.

## 🚀 Getting Started
### Clone Repositories
```bash
git clone https://github.com/NeriCarcasci/leo.git
git clone https://github.com/NeriCarcasci/leo-local.git
git clone https://github.com/NeriCarcasci/leo-cloud.git
```

### Install CLI Tool
```bash
cd leo-local
python install.py
```

### Deploy Backend & Infrastructure
```bash
cd leo-cloud/infra/terraform
terraform init
terraform apply
```
```bash
kubectl apply -f leo-cloud/infra/kubernetes/
```

## 📌 Contributing
Contributions are welcome! Open an **issue** or create a **pull request** to improve LEO.

## 📜 License
This project is licensed under the **MIT License**.
