# 🏗️ LEO Infrastructure - GCP Deployment & CI/CD

## 📜 Overview

The **infra/** directory contains **Terraform scripts, Kubernetes manifests, CI/CD workflows, and monitoring configurations** to deploy the LEO backend on **Google Cloud Platform (GCP)**.

---

## 📂 Directory Structure

```
infra/
│── terraform/         # Terraform configs for GCP services
│   ├── main.tf        # Main Terraform file defining infrastructure
│   ├── gke.tf         # Kubernetes cluster setup
│   ├── vertex_ai.tf   # Google Vertex AI configuration
│   ├── cloud_sql.tf   # PostgreSQL Cloud SQL setup
│   ├── storage.tf     # Google Cloud Storage for logs
│   ├── secret_manager.tf # Secrets management setup
│   ├── outputs.tf     # Output variables (API URL, DB credentials, etc.)
│   ├── providers.tf   # Google Cloud provider configuration
│   ├── variables.tf   # Configurable variables for Terraform
│
│── kubernetes/        # Kubernetes manifests for GKE
│   ├── deployment.yaml # Deployment config for LEO API
│   ├── service.yaml    # Service config (LoadBalancer / ClusterIP)
│   ├── ingress.yaml    # Ingress config for external access
│   ├── secrets.yaml    # Secure storage setup (linked to Google Secret Manager)
│   ├── configmap.yaml  # Environment config for LEO API
│
│── github-actions/    # CI/CD Pipelines
│   ├── deploy.yml     # Deployment workflow (build, push to GCP)
│   ├── test.yml       # Runs unit tests & integration tests
│   ├── terraform.yml  # Automates Terraform infrastructure deployment
│
│── docker/            # Docker configurations
│   ├── Dockerfile     # Defines container for LEO backend
│   ├── entrypoint.sh  # Startup script for containerized app
│   ├── docker-compose.yml # Local development setup
│
│── monitoring/        # Logging & monitoring setup
│   ├── cloud_logging.tf  # GCP Cloud Logging configuration
│   ├── alerting.tf       # Monitoring alerts (Google Cloud Monitoring)
│
│── README.md          # Documentation for infrastructure setup
```

---

## 🚀 Deploying Infrastructure with Terraform

```bash
cd infra/terraform
terraform init
terraform apply
```

---

## 📜 License
This project is licensed under the **MIT License**.
