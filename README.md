
DevOps Automation Script
This repository contains a collection of Python and Shell scripts designed to automate various DevOps and cloud operations tasks. That allows users to select and execute tasks based on their needs.


Features
- Parse Log Files: Extract and analyze log files for troubleshooting.
- Generate Secure Passwords: Create secure passwords for automation.
- API Calls to Cloud Providers: Interact with AWS, Azure, or GCP.
- File Integrity Monitoring: Monitor file changes using SHA-256 hashes.
- Trigger Jenkins Pipelines: Automate Jenkins build triggers.
- Database Backups: Automate MySQL database backups.
- Validate Terraform Configurations: Validate Terraform infrastructure as code.
- Kubernetes Cluster Monitoring: Monitor Kubernetes pods across all namespaces.
- Check Website Availability: Monitor website uptime.
- Server Health Monitoring: Monitor CPU, memory, and disk usage.
- Rotate Logs: Archive and rotate log files.
- SSH Automation: Execute commands on remote servers via SSH.
- Container Cleanup: Remove unused Docker containers.
- AWS Cost Optimization: Identify stopped EC2 instances.
- Monitor Open Ports: Check which ports are open on a server.
- Custom Load Balancer Checker: Verify backend server health.
- AWS S3 Bucket Cleaner: Delete old files from an S3 bucket.
- Log Analyzer with Regex: Extract specific information from logs.
- SSL Certificate Expiry Checker: Monitor SSL certificate expiry dates.
- AWS EC2 Instance Health Check: Check the health status of EC2 instances.
- Dynamic Inventory for Ansible: Generate a dynamic inventory of EC2 instances.
- Disk Space Alert: Send alerts when disk usage exceeds a threshold.
- Create Backup: Backup important data using tar.
- User Management: Add users from a list.
- Service Health Check: Restart a service if it fails.
- Network Latency Monitoring: Check network connectivity.
- Kubernetes Node Autoscaler: Scale Kubernetes nodes based on pod count.
- High Availability Cluster Failover: Switch to a secondary node if the primary fails.
- SSL Certificate Expiry Checker: Check SSL certificate expiry dates.
- Docker Image Cleanup: Remove unused Docker images.
- Automated System Update: Update the system automatically.


Usage
Clone the repository:
git clone https://github.com/your-username/devops-automation-scripts.git
cd devops-automation-scripts

Install Python dependencies:
pip install -r requirements.txt

Run the script:
python3 devops_automation.py
Follow the prompts to select and execute the desired operation.