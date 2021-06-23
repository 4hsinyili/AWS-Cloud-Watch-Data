import boto3
from datetime import timedelta, datetime
import pprint


cloudwatch = boto3.client('cloudwatch')
response = cloudwatch.get_metric_statistics(
    Namespace='AWS/States',  # AWS 服務名稱
    MetricName='ExecutionsSucceeded',  # Metric / 指標名稱
    Dimensions=[
        {
            'Name': 'StateMachineArn',  # 不太知道怎麼說，應該是要取得的資料類型，像這個指的是我要找 step function(StateMachine) arn 符合 下方value 的資料
            'Value': 'YourStateMachineARN'
        },
    ],
    Period=86400,  # 要將一天切割成幾秒為單位的時段
    Statistics=['Sum'],  # 要怎麼 aggregate
    StartTime=datetime.utcnow() - timedelta(days=5),  # 起始時間
    EndTime=datetime.utcnow(),  # 結束時間
)
pprint.pprint(response)


response = cloudwatch.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'm1',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/States',
                    'MetricName': 'ExecutionsFailed',
                    'Dimensions': [
                        {
                            'Name': 'StateMachineArn',
                            'Value': 'YourStateMachineARN'
                        },
                    ]
                },
                'Period': 600,
                'Stat': 'Sum',
            },
        },
    ],
    StartTime=datetime(2021, 6, 1),
    EndTime=datetime(2021, 6, 7),
)
pprint.pprint(response)
response = cloudwatch.put_metric_data(
    Namespace='Test',  # 要放到哪一個 Namespace ，最好是自創
    MetricData=[
        {
            'MetricName': 'AWS/Lambda',  # Namespace 自創的話，這個最好也自創
            'Dimensions': [
                {
                    'Name': 'test_dimension_name',
                    'Value': 'test_dimension_value'
                },
            ],
            'Timestamp': datetime.utcnow(),
            'Value': 10,
        },
    ]
)
print(response)
