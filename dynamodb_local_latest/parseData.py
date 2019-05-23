#
#  Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#  This file is licensed under the Apache License, Version 2.0 (the "License").
#  You may not use this file except in compliance with the License. A copy of
#  the License is located at
# 
#  http://aws.amazon.com/apache2.0/
# 
#  This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#  CONDITIONS OF ANY KIND, either express or implied. See the License for the
#  specific language governing permissions and limitations under the License.
#
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Releases')

with open("release_data.json") as json_file:
    releases = json.load(json_file, parse_float = decimal.Decimal)
    for data in releases:
        # fields that all data entries have
        i_d = int(data['id'])
        name = data['name']
        start = data['realtime_start']
        end = data['realtime_end']
        press = data['press_release']

        # optional fields
        link = 'None'
        notes = 'None'
        try:
          link = data['link']
        except:
          pass
        try:
          notes = data['notes']
        except:
          pass
        

        table.put_item(
           Item={
               'id': i_d,
               'realtime_start': start,
               'realtime_end': end,
               'name': name,
               'press_release': press,
               'link': link
            }
        )
        
        print("Adding movie:", i_d, name)

