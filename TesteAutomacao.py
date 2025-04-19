import json
import boto3
from io import BytesIO
import zipfile

def lambda_handler(event, context):
    session = boto3.session.Session()
    dev_client = session.client('s3')
    dev_resource = boto3.resource('s3')
    
    print("Iniciando o processo de leitura do arquivo ZIP.")
    
    bucket_name = 'dadosenade'
    key_name = "microdados_enade_2021.zip"  # Corrigido para o arquivo correto

    try:
        print(f"Obtendo o arquivo {key_name} do bucket {bucket_name}.")
        zip_object = dev_resource.Object(bucket_name=bucket_name, key=key_name)
        zipfile_bytes = BytesIO(zip_object.get()["Body"].read())
        print("Arquivo ZIP lido com sucesso.")
        
        # Tenta abrir o arquivo ZIP
        with zipfile.ZipFile(zipfile_bytes, 'r') as z:
            print(f"ZIP contém {len(z.namelist())} arquivos.")
            
            for filename in z.namelist():
                print(f"Copiando arquivo {filename} para dadosdescompactados/dados/")
                response = dev_client.put_object(
                    Body=z.open(filename).read(),
                    Bucket='dadosdescompactados',
                    Key=f'dados/{filename}'
                )
                print(f"Arquivo {filename} copiado com sucesso.")
        
        print("Processo finalizado com sucesso.")
        return {
            'statusCode': 200,
            'body': json.dumps('Arquivos extraídos e copiados com sucesso!')
        }

    except Exception as e:
        print(f"Erro: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro: {str(e)}')
        }
