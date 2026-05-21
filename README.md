## Files to prepare before deployment:
1. Model training and pipelines
2. requirement.txt file
3. API code using FastAPI
4. Docker file to create docker image


## Deployment prerequisite
To create a CI-CD pipeline for deploying the model using Docker on EC2
1. Create ECR (elastic container registry) on AWS
2. Create EC2 instance. Make sure that EC2 instance and ECR are in the same region
    - while creating the instance create new IAM role under 'advanced' options and grant this role `full access to ERC`
3. Install docker on EC2 instance other setup commands
    - `sudo yum update -y` to update the environment
    - `sudo dnf install docker -y` to install docker
    - `sudo systemctl start docker` to start docker
    - `sudo service docker status` to check is docker is running or not
    - `sudo groupadd docker` create a linux usergroup named docker
    - `sudo usermod -a -G docker ec2-user` add default user (ec2-user) to the group (docker)
    - `newgrp docker` add the current user into docker group enabling to run docker commands without `sudo`
4. Go to ECR and click on `get push command`. Paste the command into Linux terminal to check if EC2 can access ECR
5. Setup github repository by adding following to Github secret action
    - `AWS_SECRET_KEY_ID`: create access key on IAM user in AWS and add it to the repository (repo -> settings -> secrets and variables -> action)
    - `AWS_SECRET_ACCESS_KEY`: available on the same page as `AWS_SECRET_KEY_ID`
    - `EC2_HOST`: create new secret for ec2 host. copy `public DNS from EC2 instance` and paste it in github secret variable
    - `EC2_SSH_KEY`: contents of  `.pem` file which was downloaded during EC2 instance creation
    - `EC2_USERNAME`: ec2 username generally `ec2-user`. check the instance before adding
    - `AWS_ACCOUNT_ID`: AWS account id
    - `AWS_REGION`: us-east-1 (check the region of ec2 and ecr)
