# Spark3 GPU XGboost Applications

## Launch Setup EC2 Instance on AWS

Before you start the application you need to follow the steps in the repository linked below.

[https://github.com/ozgunakin/spark3-gpu-nvidia-rapidsai-setup-on-aws-ec2](https://github.com/ozgunakin/spark3-gpu-nvidia-rapidsai-setup-on-aws-ec2)

## Download the Datasets and the Application Files.

We will use mortgage, agaricus and taxi datasets for XGboost examples. All datasets and jupyter notebooks are placed in this repository.&#x20;

* [x] Clone this repository to /opt/xgboost directory.

```
cd /opt/xgboost

git clone https://github.com/ozgunakin/spark3-gpu-xgboost-applications.git

cd spark3-gpu-xgboost-applications/dataset

#EXTRACT AGARICUS FILES
tar -xvf agaricus-small.tar

#EXTRACT MORTGATE FILES
tar -xvf mortgage-small-2.tar

#EXTRACT TAXI FILES
tar -xvf taxi-small.tar
```

## GPU Based XGBoost Applications

You can find notebooks for XGBoost applications designed by using three different datasets in the notebooks directory of the repository that we have downloaded in the previous section.

* [x] Open Jupyter Notebook in /opt/xgboost/ directory.

```
cd /opt/xgboost/spark3-gpu-xgboost-applications

nohup jupyter notebook --ip 0.0.0.0 &

```

* [x] Get the Jupyter Notebook Token

```
jupyter notebook list
```

![](<.gitbook/assets/image (1).png>)

* [x] Open Jupyter Notebook in Your Browser

![](.gitbook/assets/image.png)

####
