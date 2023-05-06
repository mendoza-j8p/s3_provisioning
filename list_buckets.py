import boto3
from aws_session import get_session

session = get_session()

# Creación de un cliente de servicio
s3 = session.client('s3')

# Obtener la lista de buckets
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Imprimir la lista de buckets
print("Lista de Buckets:")
for bucket in buckets:
    print(bucket)
