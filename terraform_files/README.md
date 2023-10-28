## Description
This folder contains the terraform files used to set up the 82peaks web app. All infrastructure is set up in AWS.

There are three main components:
1. Frontend infra, these files have the `frontend` prefix
2. API infra, these files have the `api` prefix
3. Web Scraper infra, these files have the `web_scraper` prefix.  

### To set up these resources in AWS run:
1. `terraform init`
2. `terraform plan`
3. `terraform apply`