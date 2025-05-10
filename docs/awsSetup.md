# Installing AWS CLI

AWS CLI should be installed before being able to use AWS SAM. Here is the [link](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) to install it depending on which os you use.

# Installing AWS SAM CLI

After installing AWS CLI, you will have to install AWS SAM CLI using this [link](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html).

# AWS Configure

After installing both AWs CLI and AWS SAM CLI, you need to use AWS configure to link your AWS CLI to your AWS account. You need to first get your access key and secret access keys in order to do this.

## Getting Access Keys and Secret Access Keys

In order to do this, you need to login to your console and go to IAM. Then click Users and find your name. After clicking on your name, go to Security credentials and click Create access key. Your access key can be found at any time, but your secret access key only appears once when you are creating it, so you can download it as a csv file or take a picture of it and keep it somewhere safe. 

## Running aws configure in your command line

Now you can go back to your command line and type `aws configure`. It should prompts you to put in your access key and secret access key in which you just put down the access key and secret access key you just obtained. Then you need to put down eu-west-2 as the region as we are using London region for samaggi-samagom. You can just press enter for default output format. You have now finished setting up your AWS CLI and AWS SAM CLI for use. 