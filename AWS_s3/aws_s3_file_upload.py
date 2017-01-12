from boto.s3.connection import S3Connection
from boto.s3.key import Key

s3_bucket = "your-s3-bucket-name"
aws_access_key_id = "your-aws-access-key-id"
aws_secret_key = "your-aws-secret-key"

# Set the Host to get around 400 Bad Request Error
REGION_HOST = "your-region-host"


def upload_image_to_s3(image_file_path, bucket_name):
	"""Uploads images to Amazon's S3 service.
 
	Arguments:
	image_file_path: Path to image to upload on local machine.
	bucket_name: Name of the S3 bucket where image should be uploaded.
	key_name: Name of the key for the file on S3 (usually the
			timestamp).
	"""
	bucket = s3_connection.get_bucket(bucket_name)
 
	# Create a new key using image_file_path as the key
	key = Key(bucket)
	key.key = image_file_path 
	key.set_contents_from_filename(image_file_path)
	return key


s3_connection = S3Connection(aws_access_key_id, aws_secret_key, host=REGION_HOST)

s3_key = upload_image_to_s3("your-file-to-upload", s3_bucket)
