## Day 4 | AWS - How to Create Virtual Machines

### What does AWS use for Virtual Machines?

- In AWS, virtual machines are called **EC2 instances**.  
- EC2 stands for **Elastic Compute Cloud**.  
- An EC2 instance is a virtual server in the AWS Cloud.

---

### What is needed before creating a VM in AWS?

Before creating an EC2 instance, you usually need:

- an **AMI** (Amazon Machine Image) → the OS template
- an **instance type** → CPU and memory size
- a **key pair** → used to connect securely
- a **security group** → acts like a firewall
- storage and network settings

---

### Steps to Create a Virtual Machine in AWS

1. Sign in to the **AWS Management Console**
2. Open **EC2**
3. Click **Launch instance**
4. Enter the **instance name**
5. Choose an **AMI**  
   Example: Amazon Linux, Ubuntu, Windows
6. Choose an **instance type**  
   Example: `t2.micro` or `t3.micro`
7. Create or select a **key pair**
8. Configure the **security group**  
   Example:
   - allow **SSH (22)** for Linux
   - allow **RDP (3389)** for Windows
   - allow **HTTP/HTTPS** for web servers
9. Configure storage
10. Review the settings and click **Launch instance** 

---

### What is an AMI?

An **AMI (Amazon Machine Image)** is a template used to launch a VM.

It contains:
- operating system
- software setup
- launch configuration

Example:
- Ubuntu AMI
- Amazon Linux AMI
- Windows Server AMI

---

### What is a Key Pair?

A **key pair** is used to connect securely to the EC2 instance.

- **public key** → stored on the EC2 instance
- **private key** → kept by the user

For Linux instances, the private key is used for **SSH login**.  
For Windows instances, it is used to help access the administrator password.

---

### What is a Security Group?

A **security group** is a virtual firewall for the EC2 instance.

It controls:
- **inbound traffic**
- **outbound traffic**

Example:
- allow SSH from your laptop IP
- allow HTTP for website access

---

### AWS Scripts Can Be Written Using

AWS automation can be done using the following tools:

- **AWS CLI**  
  Command-line tool to create and manage AWS resources.

- **AWS API using Boto3**  
  Python SDK for AWS used to automate AWS services programmatically.

- **AWS CloudFormation (CFT)**  
  Infrastructure as Code tool from AWS used to define resources in YAML or JSON.

- **Terraform**  
  Infrastructure as Code tool used to create and manage AWS resources in a declarative way.

### Simple Understanding

- **AWS CLI** → run commands manually or in shell scripts
- **Boto3** → write Python scripts for AWS automation
- **CloudFormation** → define AWS infrastructure using AWS-native templates
- **Terraform** → define infrastructure using reusable IaC files



