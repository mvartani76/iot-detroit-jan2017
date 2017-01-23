#AWS S3 Bucket Code / Documentation

The code and information in this repository provides guidance on how to configure an S3 bucket through the AWS Management Console and then interface that bucket in python via the Python AWS SDK, `boto`.

##S3 Bucket Creation / Configuration
Before we can upload/download files to an S3 bucket, we need to have an AWS account and create an S3 bucket. We will use the AWS Management Console to create this S3 bucket.

After logging into the AWS Management Console, we need to navigate to the S3 Admin Panel (can get there via Services Page as shown below)

![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/aws-services-page.jpg "AWS Services Page")

In the S3 Admin Panel, click the "Create Bucket" button in the upper left hand corner as shown below.

![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/s3-management-console.jpg "S3 Management Console")

Next we need to give the S3 bucket a **UNIQUE** name.

![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/create-bucket-2.jpg "Create S3 Bucket")

After we create our S3 bucket, we need to update the policy to give permissions to access the bucket. This is done by first clicking on "Properties".

![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/s3-bucket-properties.jpg "S3 Bucket Properties")

And then clicking on Permissions

![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/s3-bucket-permissions.jpg "S3 Bucket Permissions")

And finally "Add Bucket Policy"

![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/s3-bucket-properties-policy.jpg "Add Bucket Policy")

Bucket policies are written in JSON and you can use this template as a guide:

![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/s3-bucket-policy.jpg "Bucket Policy Template")

Save the policy and the bucket should be configured to allow public access to retrieve files.

After we have successfully created the buckey, we need to note this name as we will use it in the code shown below.
```python
s3_bucket = "your-s3-bucket-name"
```

##Security Credentials
To access the S3 bucket from the python application, we need an aws access key and secret which can be created in the Security Credentials page of the AWS Management Console.

Click Show Access Key and we can keep our values for our AWS credentials or download the root key csv file.

You will use these key values in your code shown below.
```python
aws_access_key_id = "your-aws-access-key-id"
aws_secret_key = "your-aws-secret-key"
```
##Install Python S3 SDK
We will install the python s3 SDK using the PIP tool
```
pip install boto
```
