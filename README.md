# PandaLayer
Simple python example using Pandas and NumPy in a Lambda Layer


### SAM Local
uses template.yaml to define the Lambda, Layer, and API Gateway endpoints

```
1. sam build
2. sam local start-api
3. 127.0.0.1:3000/sum/5,4. (or max)
```

### AWS manual deploy

1. `./get_layer_packages.sh`
  This executes a docker run command that installs the lambda appropriate version of requirements.txt into the python/lib/python3.7/site-packages folder. This is necessary because pandas is compiled for the OS you're running on
  Requirments.txt only includes pandas and pytz, not numpy
  
2. `zip -r my-Python37-Pandas23.zip ./python`
  Creates a zip of the python/lib/python3.7/site-packages folder
  
3. Upload this zip as a lambda layer with python 3.7 compatibility

4. Create your lambda function and add your newly created layer.
  Be sure to also choose the AWS provided numpy scipy layer.
  
<br /><br />
Created from this great tutorial by Quy Tang https://medium.com/@qtangs/creating-new-aws-lambda-layer-for-python-pandas-library-348b126e9f3e
