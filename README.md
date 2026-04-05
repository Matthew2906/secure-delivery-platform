\# Secure Delivery Platform



This is a production grade CI/CD pipeline built with security and least-privilege access as first class concerns. Shows the most secure software delivery workflow for a team.



\## Architecture

Developer pushes code

↓

GitHub Actions CI/CD Pipeline

↓



&#x20; Job 1: Run Tests                   

&#x20; Job 2: Security Scan (Trivy)       

&#x20; Job 3: Build \& Push to ACR         

&#x20; Job 4: Deploy to Container Apps    



↓

Azure Container Registry (private)



↓

Azure Container Apps (live URL)



\## Security Design





| Control | Implementation 

|---|---|

| No stored credentials | OIDC federated identity — pipeline authenticates with short lived tokens 

| Least privilege push | Service principal scoped only to AcrPush on the registry

| Least privilege pull | Managed identity scoped only to acrPull on the registry 

| Non-root container | app runs as unprivileged user inside Docker 

| Vulnerability scanning | Trivy scans dependencies before any image is built. 

| Branch protection | Pipeline gates all deployments — no direct pushes to main 



\## Tech Stack



\- \*\*App:\*\* Python, Flask

\- \*\*Containerization:\*\* Docker (multi-stage, non-root)

\- \*\*Infrastructure:\*\* Terraform (module pattern, environment separation)

\- \*\*CI/CD:\*\* GitHub Actions

\- \*\*Registry:\*\* Azure Container Registry

\- \*\*Hosting:\*\* Azure Container Apps

\- \*\*Security:\*\* OIDC, Trivy, least-privilege RBAC



\## Pipeline Flow



push to main

│

├── test        → pytest (4 tests, endpoints + health check)

│

├── scan         → Trivy (CRITICAL/HIGH severity gate)

│       needs: test

│

├── build-push   → docker build + push to ACR

│       needs: test, scan

│

└── deploy      → az containerapp update

needs: build-push



\## Infrastructure



made with terraform using a reusable module pattern:

infra/

├── modules/

│   └── container-platform/   # reusable module

│       ├── main.tf

│       ├── variables.tf

│       └── outputs.tf

└── env/

└── dev/                  # environment-specific config

├── main.tf

└── variables.tf



\## Least Privilege identity model

GitHub Actions



└── Service Principal (sp-secure-delivery-github)

└── Role: AcrPush

└── Scope:  securedeliverydevacr only

Azure Container Apps

└── Managed identity (system-assigned)

└── Role: AcrPull

└── Scope: securedeliverydevacr only



\## live Demo



\- \*\*Health endpoint:\*\* https://securedelivery-dev.proudsea-1d1537f7.eastus.azurecontainerapps.io/health

\- \*\*Root endpoint:\*\* https://securedelivery-dev.proudsea-1d1537f7.eastus.azurecontainerapps.io



\## Local Development

```bash

\# Install dependencies

pip install -r app/requirements.txt



\# Run tests

python -m pytest app/tests/ -v



\# Run locally

python app/src/app.py

```

