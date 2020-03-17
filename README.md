# AWS_WAFv2_IPSet
Lambda function to add or remove an IP address from a WAFv2 IPSet

1. The add_an_IP_in_IPSet.py file contains a lambda function to insert an IP address in the IPSet

----[OUTPUT]-------
Response:
{
  "newAddresses": [
    "1.9.9.4/32",
    "2.9.9.4/32",
    "3.9.9.4/32"
  ]
}
----------------------

2. The remove_an_IP_from_IPSet.py file contains a lambda function to remove an IP Address from the IPSet

------[OUTPUT]-------
Response:
{
  "newAddresses": [
    "1.9.9.4/32",
    "2.9.9.4/32"
  ]
}
---------------------
