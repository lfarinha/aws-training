import json
from datetime import datetime

import boto3
from dotenv import load_dotenv

load_dotenv()


def cloudwatch():
    # Create CloudWatch client
    client = boto3.client('cloudwatch')

    metrics = client.list_metrics()
    dashboard = client.get_dashboard(DashboardName='default')

    # print(dashboard)

    # print(json.dumps(metrics, indent=4))
    print(json.dumps(dashboard, indent=4))


def instances(*args, **kwargs):
    client = boto3.client('ec2')
    response = client.describe_instances()

    print(response)


def statistics():
    cw = boto3.resource('cloudwatch')
    metric = cw.Metric('InstanceId', 'i-0800789997f8de147')

    response = metric.get_statistics(
        # Dimensions=[
        #     {
        #         'Name': 'InstanceId',
        #         'Value': 'i-0800789997f8de147'
        #     },
        # ],
        StartTime=datetime(2020, 1, 1),
        EndTime=datetime(2021, 1, 26),
        Period=6000,
        # Statistics=['Average'],
        ExtendedStatistics=['p10'],
        # Unit='Percent'
    )

    print(json.dumps(response, indent=4))


def stuff():
    client = boto3.resource('cloudwatch')
    metric = client.Metric('InstanceId', 'i-0800789997f8de147')

    print(metric.get_available_subresources())


if __name__ == '__main__':
    # instances()
    # cloudwatch()
    # statistics()
    stuff()