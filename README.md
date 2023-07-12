# Spark3 GPU XGboost Applications

### These instructions are prepared for "Introduction to Big Data with Apache Spark" lectures given by Prof. Dr. Altan Çakır in "BigDat 2023 Summer - 7th International School on Big Data"

## Setup & Launch GPU Based Spark3&#x20;

Before you start the application you need to follow the steps in the repository linked below. You can find the instructions for launching an EC2 instance on AWS and setting up Spark3 with GPU configuration in the link.&#x20;

[GPU-Based-Spark3-on-EC2](https://github.com/ozgunakin/spark3-gpu-nvidia-rapidsai-setup-on-aws-ec2)

AWS EC2 instructions will be followed in this lecture. However, If you want to install Spark3 on your local machine you can find the instructions below.&#x20;

[Spar3-Setup-on-Ubuntu\_20.04](https://github.com/ozgunakin/spark3-pseudo-cluster-installation-on-ubuntu20.04)

[Spark3-Setup-on-Windows](spark\_installation\_for\_windows.pdf)

You can also find the comparison table of the cloud services classified according to cloud providers in the following link.

[Compare-Cloud](https://comparecloud.in)

## Download the Dataset and the Application Files.

We will use mortgage, agaricus and taxi datasets for XGboost examples. All datasets and jupyter notebooks are placed in this repository.&#x20;

* [x] Clone this repository to /opt/xgboost directory.

```
cd /opt/xgboost

git clone https://github.com/ozgunakin/spark3-gpu-xgboost-applications.git

cd spark3-gpu-xgboost-applications/dataset

#EXTRACT and MOVE AGARICUS FILES
tar -xvf agaricus-small.tar
mv agaricus /opt/xgboost

#EXTRACT and MOVE MORTGATE FILES
tar -xvf mortgage-small-2.tar
mv mortgage /opt/xgboost

#EXTRACT and MOVE TAXI FILES
tar -xvf taxi-small.tar
mv taxi /opt/xgboost
```

## Run GPU Based XGBoost Applications

You can find notebooks for XGBoost applications designed by using three different datasets in the notebooks directory of the repository that we have downloaded in the previous section.

* [x] Install findspark library for Jupyter-Spark Integration.

```
pip3 install -q findspark
```

* [x] Install and open Jupyter Notebook in /opt/xgboost/ directory.

```
pip3 install notebook==6.4.9

cd /opt/xgboost/spark3-gpu-xgboost-applications

nohup jupyter notebook --ip 0.0.0.0 &

```

* [x] Get the Jupyter Notebook Token

```
jupyter notebook list
```

![](<.gitbook/assets/image (1) (1).png>)

* [x] Open Jupyter Notebook in Your Browser

![Jupyter Notebook](<.gitbook/assets/image (1).png>)

* [x] All notebooks are placed in the notebooks file. You can run them for testing your GPU integrated Spark with XGboost models.&#x20;
* [x] Those notebooks are customized versions of the notebooks in spark-rapids-exmaples repository of NVIDIA. You can find more examples at [https://github.com/NVIDIA/spark-rapids-examples](https://github.com/NVIDIA/spark-rapids-examples) and [https://nvidia.github.io/spark-rapids/Getting-Started/](https://nvidia.github.io/spark-rapids/Getting-Started/)

## Check GPU Usage

* [x] While running notebooks you can check GPU usage from your terminal using nvidia-smi command.&#x20;

![](.gitbook/assets/image.png)
