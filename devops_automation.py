import os
import subprocess
import random
import string
import hashlib
import requests
import boto3
import psutil
import paramiko
import docker
import ssl
import socket
from datetime import datetime, timedelta
from kubernetes import client, config

# --- Python Functions ---

def parse_log_files():
    with open('server.log', 'r') as file:
        for line in file:
            if "ERROR" in line:
                print(line.strip())

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def api_calls_to_cloud_providers():
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']} - State: {instance['State']['Name']}")

def file_integrity_monitoring(filepath):
    def get_file_hash(filepath):
        with open(filepath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()

    initial_hash = get_file_hash(filepath)
    while True:
        if initial_hash != get_file_hash(filepath):
            print("File has been modified!")
            break

def trigger_jenkins_build(job_name, jenkins_url, user, token):
    url = f"{jenkins_url}/job/{job_name}/build"
    response = requests.post(url, auth=(user, token))
    print(response.status_code, response.text)

def database_backups(db_name):
    backup_file = f"{db_name}_backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.sql"
    subprocess.run(["mysqldump", "-u", "root", "-p", db_name, "-r", backup_file])
    print(f"Backup saved as {backup_file}")

def validate_terraform(path):
    result = subprocess.run(["terraform", "validate", path], capture_output=True, text=True)
    if result.returncode == 0:
        print("Validation passed")
    else:
        print("Validation failed:", result.stderr)

def kubernetes_cluster_monitoring():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    for pod in v1.list_pod_for_all_namespaces().items:
        print(f"{pod.metadata.namespace}/{pod.metadata.name} - {pod.status.phase}")

def check_website_availability(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Website {url} is up.")
        else:
            print(f"Website {url} returned status code {response.status_code}.")
    except requests.ConnectionError:
        print(f"Website {url} is down.")

def server_health_monitoring():
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")

def rotate_logs(log_dir, archive_dir):
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    for log_file in os.listdir(log_dir):
        if log_file.endswith(".log"):
            shutil.move(os.path.join(log_dir, log_file), archive_dir)
    print("Logs rotated successfully.")

def ssh_automation(host, username, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read().decode())
    ssh.close()

def container_cleanup():
    client = docker.from_env()
    containers = client.containers.list(all=True)
    for container in containers:
        if container.status == "exited":
            container.remove()
            print(f"Removed container: {container.name}")

def aws_cost_optimization():
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'stopped':
                print(f"Instance {instance['InstanceId']} is stopped and incurring no charges.")

def monitor_open_ports(ports, host='127.0.0.1'):
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is open.")
            else:
                print(f"Port {port} is closed.")

def custom_load_balancer_checker(servers):
    for server in servers:
        try:
            response = requests.get(server, timeout=5)
            if response.status_code == 200:
                print(f"{server} is healthy.")
            else:
                print(f"{server} responded with status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to {server}: {e}")

def aws_s3_bucket_cleaner(bucket_name, retention_days):
    s3 = boto3.client('s3')
    cutoff_date = datetime.now() - timedelta(days=retention_days)
    objects = s3.list_objects_v2(Bucket=bucket_name)
    if "Contents" in objects:
        for obj in objects["Contents"]:
            if obj["LastModified"] < cutoff_date:
                print(f"Deleting {obj['Key']} (Last Modified: {obj['LastModified']})")
                s3.delete_object(Bucket=bucket_name, Key=obj["Key"])

def log_analyzer_with_regex(log_file, error_pattern):
    with open(log_file, 'r') as file:
        for line in file:
            match = error_pattern.search(line)
            if match:
                error_code, error_message = match.groups()
                print(f"Error Code: {error_code}, Message: {error_message}")

def ssl_certificate_expiry_checker(domains, threshold_days):
    for domain in domains:
        expiry_date = get_cert_expiry(domain)
        days_left = (expiry_date - datetime.now()).days
        if days_left < threshold_days:
            print(f"WARNING: {domain}'s SSL certificate expires in {days_left} days!")
        else:
            print(f"{domain}'s SSL certificate is valid for {days_left} more days.")

def get_cert_expiry(domain, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((domain, port)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()
            expiry_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            return expiry_date

def aws_ec2_instance_health_check(region):
    ec2_client = boto3.client('ec2', region_name=region)
    statuses = ec2_client.describe_instance_status(IncludeAllInstances=True)
    for status in statuses['InstanceStatuses']:
        instance_id = status['InstanceId']
        state = status['InstanceState']['Name']
        health = status['InstanceStatus']['Status']
        print(f"Instance {instance_id}: State={state}, Health={health}")

def dynamic_inventory_for_ansible(region):
    ec2 = boto3.client('ec2', region_name=region)
    instances = ec2.describe_instances()
    inventory = {"all": {"hosts": []}}
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'running':
                inventory['all']['hosts'].append(instance['PrivateIpAddress'])
    print(json.dumps(inventory, indent=2))

# --- Shell Scripts ---

def disk_space_alert(threshold):
    subprocess.run(['bash', '-c', f'''
    THRESHOLD={threshold}
    df -h | awk '$5 ~ /[0-9]+%/ {{ gsub("%", "", $5); if ($5 > $THRESHOLD) print $1, $5 }}' | while read -r fs usage; do
        echo "Disk usage on $fs is $usage%"
    done
    '''])

def create_backup(source_dir, backup_dir):
    subprocess.run(['bash', '-c', f'''
    tar -czf {backup_dir}/backup_$(date +%Y%m%d).tar.gz {source_dir}
    '''])

def user_management(users_file):
    subprocess.run(['bash', '-c', f'''
    for user in $(cat {users_file}); do
        useradd $user
        echo "Created user: $user"
    done
    '''])

def service_health_check(service_name):
    subprocess.run(['bash', '-c', f'''
    if ! systemctl is-active --quiet {service_name}; then
        echo "{service_name} is down. Restarting..."
        systemctl restart {service_name}
    fi
    '''])

def network_latency_monitoring(host):
    subprocess.run(['bash', '-c', f'''
    ping -c 1 {host} &> /dev/null
    if [ $? -ne 0 ]; then
        echo "Network is down"
    else
        echo "Network is up"
    fi
    '''])

def kubernetes_node_autoscaler():
    subprocess.run(['bash', '-c', '''
    NODE_COUNT=$(kubectl get nodes | grep -c Ready)
    POD_COUNT=$(kubectl get pods --all-namespaces | wc -l)
    if [ $POD_COUNT -gt $((NODE_COUNT * 50)) ]; then
        echo "Scaling nodes..."
        kubectl scale node-pool my-pool --replicas=$((NODE_COUNT + 1))
    fi
    '''])

def high_availability_cluster_failover(vip, check_port):
    subprocess.run(['bash', '-c', f'''
    if ! nc -z {vip} {check_port}; then
        echo "Primary is down. Switching to secondary."
        ip addr add {vip}/24 dev eth0
    fi
    '''])

def ssl_certificate_expiry_checker_shell(domain):
    subprocess.run(['bash', '-c', f'''
    EXPIRY_DATE=$(echo | openssl s_client -servername {domain} -connect {domain}:443 2>/dev/null | openssl x509 -noout -dates | grep 'notAfter' | cut -d= -f2)
    echo "SSL Certificate for {domain} expires on $EXPIRY_DATE"
    '''])

def docker_image_cleanup():
    subprocess.run(['bash', '-c', '''
    docker image prune -f
    docker images | grep "<none>" | awk '{print $3}' | xargs docker rmi -f
    '''])

def automated_system_update():
    subprocess.run(['bash', '-c', '''
    apt-get update -y && apt-get upgrade -y
    '''])

# --- Main Menu ---

def main_menu():
    print("""
    === DevOps Automation Script ===
    1. Parse Log Files
    2. Generate Secure Password
    3. API Calls to Cloud Providers
    4. File Integrity Monitoring
    5. Trigger Jenkins Build
    6. Database Backup
    7. Validate Terraform Configurations
    8. Kubernetes Cluster Monitoring
    9. Check Website Availability
    10. Server Health Monitoring
    11. Rotate Logs
    12. SSH Automation
    13. Container Cleanup
    14. AWS Cost Optimization
    15. Monitor Open Ports
    16. Custom Load Balancer Checker
    17. AWS S3 Bucket Cleaner
    18. Log Analyzer with Regex
    19. SSL Certificate Expiry Checker
    20. AWS EC2 Instance Health Check
    21. Dynamic Inventory for Ansible
    22. Disk Space Alert (Shell)
    23. Create Backup (Shell)
    24. User Management (Shell)
    25. Service Health Check (Shell)
    26. Network Latency Monitoring (Shell)
    27. Kubernetes Node Autoscaler (Shell)
    28. High Availability Cluster Failover (Shell)
    29. SSL Certificate Expiry Checker (Shell)
    30. Docker Image Cleanup (Shell)
    31. Automated System Update (Shell)
    """)
    choice = input("Enter your choice: ")
    return choice

# --- Execute Based on User Input ---

if __name__ == "__main__":
    choice = main_menu()
    if choice == "1":
        parse_log_files()
    elif choice == "2":
        print(generate_password())
    elif choice == "3":
        api_calls_to_cloud_providers()
    elif choice == "4":
        filepath = input("Enter file path to monitor: ")
        file_integrity_monitoring(filepath)
    elif choice == "5":
        job_name = input("Enter Jenkins job name: ")
        jenkins_url = input("Enter Jenkins URL: ")
        user = input("Enter Jenkins username: ")
        token = input("Enter Jenkins token: ")
        trigger_jenkins_build(job_name, jenkins_url, user, token)
    elif choice == "6":
        db_name = input("Enter database name: ")
        database_backups(db_name)
    elif choice == "7":
        path = input("Enter Terraform path: ")
        validate_terraform(path)
    elif choice == "8":
        kubernetes_cluster_monitoring()
    elif choice == "9":
        url = input("Enter website URL: ")
        check_website_availability(url)
    elif choice == "10":
        server_health_monitoring()
    elif choice == "11":
        log_dir = input("Enter log directory: ")
        archive_dir = input("Enter archive directory: ")
        rotate_logs(log_dir, archive_dir)
    elif choice == "12":
        host = input("Enter host IP: ")
        username = input("Enter SSH username: ")
        password = input("Enter SSH password: ")
        command = input("Enter command to execute: ")
        ssh_automation(host, username, password, command)
    elif choice == "13":
        container_cleanup()
    elif choice == "14":
        aws_cost_optimization()
    elif choice == "15":
        ports = input("Enter ports to check (comma-separated): ").split(',')
        ports = [int(port) for port in ports]
        monitor_open_ports(ports)
    elif choice == "16":
        servers = input("Enter server URLs (comma-separated): ").split(',')
        custom_load_balancer_checker(servers)
    elif choice == "17":
        bucket_name = input("Enter S3 bucket name: ")
        retention_days = int(input("Enter retention days: "))
        aws_s3_bucket_cleaner(bucket_name, retention_days)
    elif choice == "18":
        log_file = input("Enter log file path: ")
        error_pattern = input("Enter error regex pattern: ")
        log_analyzer_with_regex(log_file, re.compile(error_pattern))
    elif choice == "19":
        domains = input("Enter domains (comma-separated): ").split(',')
        threshold_days = int(input("Enter threshold days: "))
        ssl_certificate_expiry_checker(domains, threshold_days)
    elif choice == "20":
        region = input("Enter AWS region: ")
        aws_ec2_instance_health_check(region)
    elif choice == "21":
        region = input("Enter AWS region: ")
        dynamic_inventory_for_ansible(region)
    elif choice == "22":
        threshold = input("Enter disk usage threshold (e.g., 80): ")
        disk_space_alert(threshold)
    elif choice == "23":
        source_dir = input("Enter source directory: ")
        backup_dir = input("Enter backup directory: ")
        create_backup(source_dir, backup_dir)
    elif choice == "24":
        users_file = input("Enter users file path: ")
        user_management(users_file)
    elif choice == "25":
        service_name = input("Enter service name: ")
        service_health_check(service_name)
    elif choice == "26":
        host = input("Enter host to ping: ")
        network_latency_monitoring(host)
    elif choice == "27":
        kubernetes_node_autoscaler()
    elif choice == "28":
        vip = input("Enter VIP: ")
        check_port = input("Enter check port: ")
        high_availability_cluster_failover(vip, check_port)
    elif choice == "29":
        domain = input("Enter domain: ")
        ssl_certificate_expiry_checker_shell(domain)
    elif choice == "30":
        docker_image_cleanup()
    elif choice == "31":
        automated_system_update()
    else:
        print("Invalid choice. Exiting.")