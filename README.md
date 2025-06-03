
# DevOps Automation Toolkit

A **Python & Bash-powered DevOps automation script** for system administrators, DevOps engineers, and IT operations teams. This script simplifies common infrastructure tasks, including cloud management, server monitoring, backups, security checks, and more—all accessible via a **menu-driven CLI interface**.

---

## 🚀 Features

✅ Cloud Operations (AWS, Kubernetes, Terraform, Jenkins)  
✅ System & Network Monitoring  
✅ File Integrity & Log Management  
✅ Backup & Restore Utilities  
✅ Container Management (Docker)  
✅ SSL & Security Checks  
✅ Automated Bash Scripts  
✅ Ansible Dynamic Inventory Generator  
✅ And much more...

---

## 🛠️ Setup

### Prerequisites

- Python 3.7+
- Bash shell (for shell script features)
- Install required Python packages:

```bash
pip install -r requirements.txt
```

**`requirements.txt`** (create this file):

```
boto3
psutil
paramiko
docker
requests
kubernetes
```

- AWS credentials configured via `~/.aws/credentials` or environment variables
- `mysqldump`, `nc`, `kubectl`, `openssl`, and other CLI tools installed as required

---

## 📦 Usage

Run the script:

```bash
python3 devops_automation.py
```

Follow the menu prompts to select and execute the desired task.

---

## 📚 Menu Options

| Option | Task                                     |
|--------|------------------------------------------|
| 1      | Parse log files for errors               |
| 2      | Generate a secure password               |
| 3      | API calls to AWS (EC2)                   |
| 4      | File integrity monitoring (SHA-256)      |
| 5      | Trigger Jenkins build                    |
| 6      | Database backup via `mysqldump`          |
| 7      | Validate Terraform configurations        |
| 8      | Monitor Kubernetes cluster pods          |
| 9      | Check website availability               |
| 10     | Server CPU, Memory, Disk usage report    |
| 11     | Rotate and archive log files             |
| 12     | SSH automation and command execution     |
| 13     | Clean up stopped Docker containers       |
| 14     | AWS EC2 cost optimization                |
| 15     | Check open ports on a host               |
| 16     | Custom load balancer checker             |
| 17     | AWS S3 bucket cleanup by retention       |
| 18     | Log analyzer with regex pattern matching |
| 19     | SSL certificate expiry checker (Python)  |
| 20     | AWS EC2 instance health check            |
| 21     | Dynamic Ansible inventory (AWS EC2)      |
| 22-31  | Bash-powered tasks (disk alert, backup, user management, etc.) |

---

## 🧰 Example Usage

- **Check Website Availability:**

  ```bash
  Select option 9 ➔ Enter URL ➔ Get status
  ```

- **Generate Secure Password:**

  ```bash
  Select option 2 ➔ Auto-generates and prints a password
  ```

- **Run EC2 Cost Optimization:**

  ```bash
  Select option 14 ➔ Lists stopped EC2 instances
  ```

---

## ⚠️ Notes

- **AWS Operations:** Ensure your AWS CLI and `boto3` are configured.
- **Kubernetes Tasks:** Requires `kubectl` configured and accessible.
- **SSL Checker (Python):** Uses `ssl` & `socket` libraries for certificate expiry validation.
- **Shell Scripts:** Some features rely on Bash and Linux utilities like `tar`, `df`, `nc`, `openssl`.

---

## 🌐 Contributions

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.
