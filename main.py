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

# Carga de un archivo a un bucket de Amazon S3
s3.upload_file('file.txt', bucket_name, 'file.txt')

response = s3.list_objects_v2(Bucket=bucket_name)
print(response)

# Descarga de un archivo de un bucket de Amazon S3
try:
    s3.download_file(bucket_name, 'file.txt', './tmp/file1.txt')
    print("Archivo descargado correctamente en '/tmp/'")
except Exception as e:
    print(f"Error al descargar el archivo: {str(e)}")

