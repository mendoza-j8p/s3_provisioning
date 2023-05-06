import boto3
from aws_session import get_session

session = get_session()

# Creación de un cliente de servicio
s3 = session.client('s3')

# Nombre del bucket
bucket_name = 'my-bucket-wehpijhg'

# Obtener la lista de objetos
objects = s3.list_objects_v2(Bucket=bucket_name)

# Imprimir la lista de objetos
if 'Contents' in objects:
    for obj in objects['Contents']:
        print(f"Nombre: {obj['Key']}\nTamaño: {obj['Size']}\nÚltima modificación: {obj['LastModified']}\n")
else:
    print(f"No se encontraron objetos en el bucket {bucket_name}")
