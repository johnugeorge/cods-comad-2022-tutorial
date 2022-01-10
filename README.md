# CODS-COMAD 2022 Tutorial
## End-to-end Machine Learning using Kubeflow
      
   In this tutorial, attendees will learn about the basic components of an end-to-end ML system including model training, hyperparameter tuning, and model deployment. The tutorial will be based on Kubeflow, a widely used open-source machine learning toolkit for Kubernetes. In this tutorial, standard autoencoder based [Keras anomaly detection](https://keras.io/examples/timeseries/timeseries_anomaly_detection/) model is used. 

## Model training using Training operator

In `train` folder,
   
    docker build -t <image-name> -f Dockerfile .
    docker push <image-name>

Replace image in train.yaml with the newly built image tag and deploy the config

    kubectl create -f train.yaml

## Model tuning using Katib

In `tune` folder, 

    docker build -t <image-name> -f Dockerfile .
    docker push <image-name>

Replace image in tune.yaml with the newly built image tag and deploy the config

    kubectl create -f tune.yaml


## Model Serving using AWS SageMaker

In `inference` folder,

    sh  build_and_push.sh <image-name>
    
 
## ML Worklow using Kubflow Pipelines

You can create a new workflow run by

1. using KF pipelines UI, upload `e2e_pipeline.tar.gz` directly or
2. using KF Pipelines SDK, execute `anomaly-prediction.ipynb` in Kubeflow Notebooks 


