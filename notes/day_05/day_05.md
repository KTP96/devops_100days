# Day-5 | AWS CLI 

## What is AWS CLI?

- AWS CLI is a unified command-line tool used to manage AWS services.
- It lets you talk to AWS APIs from the terminal.
- General format:
  ```
  aws <service> <command> <options>
  ```
- Ex:
  ```
  aws s3 ls
  aws ec2 describe-instances
  ```
## Installation and checking version

- `aws --version` is used to verify the installation.
- `aws configure` is used to configure the Access key ID and Secret Access Key.
  - This AWS CLI configuration is stored in
    - ~/.aws/config
    - ~/.aws/credentials
    -   
