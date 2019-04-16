# PandaLayer
Simple python example using Pandas and NumPy in a Lambda Layer


### SAM Local
You can use SAM local to run the example locally.  template.yaml defines the Lambdas, Layer, and API Gateway endpoints.

```
1. sam build
2. sam local start-api
3. Hit the end point in a browser at 127.0.0.1:3000/sum/5,4. (example defines sum & max methods)
```

### AWS manual deploy using the web console

1. Install: `./get_layer_packages.sh`
  This executes a docker run command that installs the lambda appropriate version of requirements.txt into the python/lib/python3.7/site-packages folder. This is necessary because pandas is compiled for the OS you're running on
  Requirments.txt only includes pandas and pytz, not numpy
  
2. Package: `zip -r my-Python37-Pandas23.zip ./python`
  Creates a zip of the python/lib/python3.7/site-packages folder
  
3. Upload:  upload the zip as a Lambda Layer with python 3.7 compatibility

4. Using the AWS console, create your lambda function and add your newly created layer.
  Be sure to also choose the AWS provided numpy scipy layer.
  
<br /><br />
Created from this great tutorial by Quy Tang https://medium.com/@qtangs/creating-new-aws-lambda-layer-for-python-pandas-library-348b126e9f3e
