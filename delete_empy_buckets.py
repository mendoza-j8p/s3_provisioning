import boto3
from aws_session import get_session

session = get_session()

# Creación de un cliente de servicio
s3 = session.client('s3')

# Obtener la lista de buckets
response = s3.list_buckets()

# Recorrer la lista de buckets y eliminar los vacíos
for bucket in response['Buckets']:
    bucket_name = bucket['Name']
    if bucket_name.startswith('my-bucket-'):
        response = s3.list_objects(Bucket=bucket_name)

    if 'Contents' in response:
        print(f"Bucket '{bucket_name}' no está vacío, no se elimina")
    else:
        print(f"Bucket '{bucket_name}' está vacío, se eliminará")
        s3.delete_bucket(Bucket=bucket_name)
print("Operación completada")
