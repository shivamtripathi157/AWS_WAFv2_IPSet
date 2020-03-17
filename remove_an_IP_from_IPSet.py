import json
import boto3

client = boto3.client('wafv2')

def lambda_handler(event, context):
    getMyIPSet = client.get_ip_set(
    Name='blocklist',
    Scope='REGIONAL',
    Id='47a052b7-c918-4440-a341-911a17dfc9e7'
    )

    lockToken=getMyIPSet["LockToken"]
    myAddresses= getMyIPSet["IPSet"]['Addresses']
    myAddresses.remove('3.9.9.4/32')

    updateMyIpset = client.update_ip_set(
    Name='blocklist',
    Scope='REGIONAL',
    Id='47a052b7-c918-4440-a341-911a17dfc9e7',
    Addresses=myAddresses,
    LockToken=lockToken
   )

    return {
        "newAddresses":myAddresses
    }
