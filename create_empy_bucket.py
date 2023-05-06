import boto3
import random
import string
from aws_session import get_session

session = get_session()

# Creación de un cliente de servicio
s3 = session.client('s3')

# Creación de un recurso
s3_resource = session.resource('s3')


# Manipulación de objetos de Amazon S3
# Genera un nombre aleatorio para el bucket
bucket_name = 'my-bucket-' + ''.join(random.choices(string.ascii_lowercase, k=8))

# Creación de un nuevo bucket
response = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})

bucket = s3_resource.Bucket(bucket_name)

print(f"Bucket {bucket_name} creado exitosamente")
print(f"Nombre del bucket: {bucket_name}")
print(f"Fecha de creación: {bucket.creation_date}")

