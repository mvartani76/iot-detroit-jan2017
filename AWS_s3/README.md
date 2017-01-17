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

And finally "Edit Bucket Policy"

![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/s3-bucket-properties-policy.jpg "Edit Bucket Policy")
