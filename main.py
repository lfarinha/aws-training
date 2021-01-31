import json
from datetime import datetime, timedelta

import boto3


def cloudwatch():
    # Create CloudWatch client
    client = boto3.client('cloudwatch')
    dashboard = client.get_dashboard(DashboardName='default')
    print(dashboard.get("DashboardBody"))


def instances(*args, **kwargs):
    client = boto3.client('ec2')
    response = client.describe_instances()

    print(response)


def ec2_statistics(namespace, metric_name, dimension_name, dimension_value):
    client = boto3.client('cloudwatch', region_name='us-east-1')
    response = client.get_metric_statistics(
        Namespace=namespace,
        MetricName=metric_name,
        Dimensions=[
            {
                'Name': dimension_name,
                'Value': dimension_value
            },
        ],
        StartTime=datetime.utcnow() - timedelta(hours=1),
        EndTime=datetime.utcnow(),
        Period=60,
        Statistics=['Average'],
        Unit='Percent'
    )

    print(response)

    data_points = response.get("Datapoints")

    for data_point in data_points:
        data_point.update({"Timestamp": data_point.get("Timestamp").strftime("%Y-%m-%d %H:%M:%S")})

    print(json.dumps(response, indent=4))


def stuff():
    client = boto3.resource('cloudwatch')
    metric = client.Metric('InstanceId', 'i-0800789997f8de147')

    print(metric.get_available_subresources())


if __name__ == '__main__':
    # instances()
    # cloudwatch()
    ec2_statistics("AWS/EC2", "CPUUtilization", "InstanceId", "i-0684c0a722655dd39")
    ec2_statistics("AWS/EC2", "NetworkPacketsOut", "InstanceId", "i-0684c0a722655dd39")
    # stuff()
