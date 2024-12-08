import json
import boto3
import geoip2.database

s3 = boto3.client('s3')
kinesis = boto3.client('kinesis')
geo_reader = geoip2.database.Reader('C:\\Users\\darun\\OneDrive\\Desktop\\Placement\\Task-3\\GeoLite2-City.mmdb')

S3_BUCKET = 'my-real-time-data-bucket'

def lambda_handler(event, context):
    for record in event['Records']:
        payload = json.loads(record['kinesis']['data'])

        ip_address = payload['ip_address']
        location = get_geo_location(ip_address)
        payload['geo_location'] = location

        store_in_s3(payload)

        put_transformed_data(payload)
        
    return {'statusCode': 200, 'body': json.dumps('Processing completed.')}

def get_geo_location(ip_address):
    try:
        response = geo_reader.city(ip_address)
        return {
            'city': response.city.name,
            'country': response.country.name,
            'latitude': response.location.latitude,
            'longitude': response.location.longitude
        }
    except geoip2.errors.AddressNotFoundError:
        return {}

def store_in_s3(data):
    s3.put_object(
        Bucket=S3_BUCKET,
        Key=f"{data['sensor_id']}/{data['timestamp']}.json",
        Body=json.dumps(data)
    )

def put_transformed_data(payload):
    kinesis.put_record(
        StreamName='TransformedStream',
        Data=json.dumps(payload),
        PartitionKey=str(payload['sensor_id'])
    )
