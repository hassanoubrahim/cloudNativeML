# Project Title: XGBoost Hyperparameter Tuning with Amazon SageMaker

## Overview

This project focuses on training an XGBoost model by tuning its hyperparameters using Amazon SageMaker. The XGBoost algorithm is a powerful and scalable machine learning algorithm that is particularly effective for regression and classification tasks. By leveraging Amazon SageMaker, we can easily deploy and manage the entire machine learning workflow.

## Prerequisites

Before running the provided code, ensure that you have the following set up:

1. An AWS account with the necessary permissions to use Amazon SageMaker.
2. Data stored in an S3 bucket, with separate paths for training and validation datasets.

## Code Overview

### Step 1: Set Up Environment

```python
import boto3
from sagemaker import image_uris

# Retrieve the XGBoost container URI
region = boto3.Session().region_name    
container = image_uris.retrieve('xgboost', region, version='1.2-1')
```

### Step 2: Define XGboost Estimator
```python
import sagemaker

# Set up SageMaker role and create an XGBoost estimator
role = sagemaker.get_execution_role() 

xgb = sagemaker.estimator.Estimator(container,
                                    role,
                                    instance_count=1,
                                    instance_type='ml.m4.xlarge',
                                    output_path='s3://{}/{}/output'.format(bucket, prefix),
                                )
```
### Deploy the model

```python
# Deploy the XGBoost model as an endpoint
xgb_predictor = xgb.deploy(endpoint_name=endpoint_name, 
                          initial_instance_count=1, 
                          instance_type='ml.t2.medium')

```

## Amazon deployment process
Once everything is done, we can clearly find in training job our model as the following image demonstrate.
![image descript](https://media.discordapp.net/attachments/1179056718064386200/1183436775969005598/image.png?ex=65885462&is=6575df62&hm=189bcc24d6f3938c1ef8c711469efc40b5f266929778a2e2d9496bcd06e4bbe0&=&format=webp&quality=lossless&width=1343&height=640)

We can also observe the status history

![image](https://media.discordapp.net/attachments/1179056718064386200/1183436776279380120/image.png?ex=65885462&is=6575df62&hm=759aea3ceea59aee4059ccf704088e1b15d7489732e8a8e42efdbe2f6322425e&=&format=webp&quality=lossless&width=1343&height=640)

Now, lets move to production deployment 
![image](https://media.discordapp.net/attachments/1179056718064386200/1183436776908529744/image.png?ex=65885462&is=6575df62&hm=18d68786fdbccdad89fbe2d173eec51a5a286506f0277410b86830a782b44b96&=&format=webp&quality=lossless&width=1343&height=640)

Finally, we can set an endpoint for using our model.

![image](https://media.discordapp.net/attachments/1179056718064386200/1183436777525104670/image.png?ex=65885462&is=6575df62&hm=f2bee572aaba36aab873937ee1affcb471f761f1125535118f1cee6946e47b85&=&format=webp&quality=lossless&width=1343&height=640)