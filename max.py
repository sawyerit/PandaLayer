import pandas as pd
import numpy as np
import json

def handler(event, context):
    event_list = event['pathParameters']['values']
    my_list = [int(e) for e in event_list.split(',')]
    my_series = pd.Series(my_list)
    
    return {
        'statusCode': str(200),
        'body': json.dumps(str(my_series.max())),
        }
