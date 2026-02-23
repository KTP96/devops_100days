# 1) Linux (must-have)

### 1.1 File system + shell basics

* Linux directory structure: `/`, `/etc`, `/var`, `/home`, `/usr`, `/tmp`
* Navigation & file ops: `ls`, `cd`, `cp`, `mv`, `rm`, `mkdir`, `touch`
* Viewing files: `cat`, `less`, `head`, `tail`
* Find/search: `find`, `grep`, `xargs`
* Text processing (basic): `awk`, `sed`, `cut`, `sort`, `uniq`, `wc`
* Redirection: `>`, `>>`, `2>`, pipes `|`
* Permissions: rwx, `chmod`, `chown`, `umask`
* Users/groups: `id`, `useradd`, `groupadd`, `passwd`, `sudo`
* Environment vars: `export`, `.bashrc`, PATH
* Archives: `tar`, `gzip`, `zip`

### 1.2 Processes + services

* Processes: `ps`, `top/htop`, `kill`, signals
* Jobs: `&`, `jobs`, `bg`, `fg`, `nohup`
* systemd: `systemctl` start/stop/enable/status
* Logs: `journalctl`, `/var/log/*`

### 1.3 Networking on Linux

* IP & routes: `ip a`, `ip r`
* Ports: `ss -tulpn`, `netstat` (legacy)
* Connectivity: `ping`, `traceroute`, `curl`, `wget`, `dig/nslookup`
* SSH: keys, `ssh`, `scp`, `sftp`, agent basics
* Firewall concept: `ufw` / `iptables` (basic understanding)

### 1.4 Storage + performance basics

* Disk: `df -h`, `du -sh`, `lsblk`, mount basics
* Memory/CPU: `free -m`, `uptime`, `vmstat` (basic)
* File permissions & ownership issues (common debug)

---

# 2) Networking Fundamentals (must-have)

### 2.1 IP & subnetting (very important)

* IPv4, CIDR notation
* Subnet masks concept
* Private vs public IP ranges
* NAT basics
* Default gateway

### 2.2 Core protocols

* TCP vs UDP
* Ports and sockets
* DNS (A/AAAA/CNAME), TTL basics
* HTTP basics: methods, status codes
* HTTPS/TLS basics: certificates, handshake concept

### 2.3 Network components

* Firewall concepts
* Load balancing concepts (L4 vs L7)
* Reverse proxy concept
* CDN concept
* Routing basics

---

# 3) Git + GitHub (must-have)

### 3.1 Git fundamentals

* repo, commit, branch
* staging area
* merge vs rebase (basic)
* conflict resolution
* tags + releases (basic)

### 3.2 Collaboration

* pull requests, reviews
* branching strategies (simple: feature branches)
* commit message hygiene

### 3.3 GitHub essentials

* README, issues, project boards (basic)
* GitHub Actions basics (you’ll use later)

---

# 4) Programming / Scripting (minimum required)

(You don’t need to be a software engineer, but you must automate.)

### 4.1 Bash scripting

* variables, arguments (`$1`), exit codes
* if/else, loops
* functions
* quoting, heredocs
* parsing command output
* writing safe scripts (set -e, set -u basics)

### 4.2 Python basics (recommended)

* venv, pip, requirements.txt
* reading env vars
* HTTP calls (requests)
* JSON parsing
* basic logging
* simple CLI script (argparse)
* AWS SDK concept (boto3 basics) (optional)

---

# 5) Cloud Fundamentals (AWS-first)

### 5.1 Cloud concepts

* IaaS vs PaaS vs SaaS
* Regions, AZs
* Shared Responsibility Model
* HA vs DR basics
* Scalability vs elasticity
* CAPEX vs OPEX concept

### 5.2 AWS account basics

* AWS Organizations (concept)
* Billing + cost awareness
* Free tier safety + budget alarms

---

# 6) AWS Core Services (must-have)

## 6.1 IAM (security backbone)

* Users vs groups vs roles
* Policies: JSON structure (Effect/Action/Resource)
* Managed vs inline policies
* Role assumption (STS)
* Least privilege
* MFA
* Access keys: why to avoid on servers
* Instance profiles (EC2 role)
* Permission boundaries (concept)

## 6.2 VPC Networking (very important)

* VPC, CIDR, subnets
* Public vs private subnets
* Route tables
* Internet Gateway
* NAT Gateway
* Security Groups (stateful)
* NACLs (stateless)
* VPC endpoints (S3 gateway endpoint concept)
* Peering (concept)
* VPN / Direct Connect (concept)

## 6.3 EC2 (compute)

* AMI, instance types, key pairs
* User data (bootstrapping)
* EBS volumes (gp3, io1 concept)
* Elastic IP concept
* Auto Scaling Group (concept + basic)
* ALB vs NLB (concept)

## 6.4 S3 (object storage)

* Buckets, objects, prefixes
* Versioning
* Lifecycle rules
* Encryption (SSE-S3, SSE-KMS concept)
* Bucket policies vs IAM policies
* Static website hosting (optional)
* Pre-signed URLs (concept)

## 6.5 RDS (managed database)

* Engine basics (Postgres/MySQL)
* Multi-AZ (concept)
* Backups, snapshots
* Parameter groups (concept)
* Connectivity via SG rules
* Public accessibility: why usually “NO”

## 6.6 CloudWatch (monitoring)

* Metrics vs logs
* Log groups/streams
* Alarms
* Dashboards
* Agent concept (CloudWatch agent)
* SNS notifications (basic)

## 6.7 SNS / SQS (messaging basics) (good-to-have)

* SNS topics + subscriptions (alerts)
* SQS queue basics (buffering) (concept-level is okay)

## 6.8 Systems Manager (SSM) (very valuable)

* Session Manager (SSH-less access concept)
* Parameter Store (secrets/config)
* Run Command (basic)
* Patch Manager concept

---

# 7) Infrastructure as Code (Terraform) (must-have)

### 7.1 Terraform fundamentals

* provider, resource, data sources
* variables, outputs
* locals
* modules (create and use)
* state file: what it is and why it matters
* remote state (S3)
* state locking (DynamoDB concept)
* plan/apply/destroy lifecycle

### 7.2 Terraform AWS topics

* VPC module patterns
* SG patterns
* outputs for integration
* handling secrets safely (don’t hardcode)
* environments (dev/stage/prod) structure (basic)

### 7.3 Best practices

* formatting (`terraform fmt`)
* validation (`terraform validate`)
* linting (optional)
* separate state per environment
* tagging strategy

---

# 8) Containers (Docker) (must-have)

### 8.1 Docker fundamentals

* image vs container
* Dockerfile basics
* layers + caching
* CMD vs ENTRYPOINT
* exposing ports
* volumes
* networks

### 8.2 Docker Compose

* multi-container apps
* env vars
* volumes
* dependencies (depends_on)

### 8.3 Container registry

* ECR (AWS) basics
* tagging, versioning images

---

# 9) CI/CD (must-have)

### 9.1 CI basics

* build, test, lint
* artifacts
* caching dependencies
* secrets in CI

### 9.2 CD basics

* deploy strategies: rolling / blue-green / canary (concept)
* environment configs
* approvals/manual gates (concept)

### 9.3 GitHub Actions (recommended)

* workflows, jobs, steps
* triggers (push, PR)
* runners
* secrets
* building and pushing Docker image
* deploy to EC2 (SSH or SSM)

(Jenkins is good too, but GitHub Actions is fastest to start.)

---

# 10) Deployment on AWS (entry-level must-have)

### 10.1 EC2-based deployments (most common for beginners)

* Nginx reverse proxy concept
* systemd service for app (or docker run)
* log location and rotation concept
* health check endpoints

### 10.2 Load balancing + TLS (good-to-have)

* ALB target groups
* HTTPS with ACM (concept)
* DNS via Route 53 (concept)

### 10.3 Serverless (optional)

* Lambda + API Gateway (concept-level)

---

# 11) Observability + Operations (must-have)

### 11.1 Monitoring

* what metrics matter (CPU/mem/disk/latency/errors)
* alert basics: threshold vs anomaly (concept)
* alert routing (SNS/email)
* dashboards

### 11.2 Logging

* structured logs concept (JSON)
* log levels
* log retention policies

### 11.3 Incident basics

* severity, triage, mitigation, resolution
* runbooks
* postmortems (what/why/how to prevent)

---

# 12) Security basics (must-have)

* IAM least privilege
* MFA everywhere
* never commit secrets
* encryption at rest & transit concept
* security groups locked down
* private subnets for DB
* SSM Parameter Store / Secrets Manager usage
* basic auditing concept: CloudTrail (concept)

---

# 13) Cost basics (must-have)

* understand where costs come from (NAT gateways, EC2, EBS, RDS, data transfer)
* set budgets + alarms
* shut down resources when not used

---

# 14) “Job-ready” projects you MUST build (to crack interviews)

You should build at least **two**:

### Project A (the flagship)

**3-tier AWS architecture with Terraform**

* VPC + public/private subnets + NAT
* EC2 app in public subnet (or private behind ALB)
* RDS in private subnet
* S3 for artifacts or static content
* CloudWatch logs + alarm
* README + diagram + “how to deploy” + teardown

### Project B (DevOps)

**CI/CD pipeline deploying Docker app to AWS**

* Dockerize app
* GitHub Actions builds/tests
* Push image to ECR
* Deploy to EC2 (restart container)
* Add rollback steps

(Optional strong add-on)

### Project C

**Observability**

* Dashboard + alarm + log-based alert
* runbook + postmortem template

---

# 15) Interview question areas to prepare (must-have)

* Explain your project architecture clearly
* Linux troubleshooting scenarios
* Networking: CIDR, SG rules, DNS, TLS
* AWS: IAM/VPC/EC2/S3/RDS/CloudWatch
* Terraform: state, modules, remote state, plan/apply
* Docker: Dockerfile basics, port mapping, images
* CI/CD: pipeline stages, secrets, deploy strategy
* Ops: incident response, monitoring, logging

---
