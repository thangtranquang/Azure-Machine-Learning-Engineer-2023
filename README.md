# Capstone Project - Azure Machine Learning Engineer - Thang Tran



This project, I will create two models: one using Automated ML (denoted as AutoML from now on) and one customized model whose hyperparameters are tuned using HyperDrive. I will then compare the performance of both the models and deploy the best performing model.

## Project Workflow

![ef730eb0-8ef9-46ad-bfe0-18b3e3b3b963](./image/ef730eb0-8ef9-46ad-bfe0-18b3e3b3b963.png)



## Dataset: Heart Failure Prediction

The link dataset from Kaggle: [Heart Failure Prediction](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data) 

### Overview

Cardiovascular diseases (CVDs) are the **number 1 cause of death globally**, taking an estimated **17.9 million lives each year**, which accounts for **31% of all deaths worlwide**.  
Heart failure is a common event caused by CVDs and this dataset contains 12 features that can be used to predict mortality by heart failure.

Most cardiovascular diseases can be prevented by addressing behavioural risk factors such as tobacco use, unhealthy diet and obesity, physical inactivity and harmful use of alcohol using population-wide strategies.

People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need **early detection** and management wherein a machine learning model can be of great help.



**This dataset contains the following features:**

![48dbd13b-1857-4468-92ac-734e004dc91e](./image/48dbd13b-1857-4468-92ac-734e004dc91e.png)

![a4477e89-0a88-4f67-8a82-b159e8ae6a79](./image/a4477e89-0a88-4f67-8a82-b159e8ae6a79.png)

![bccbf978-115a-4781-84fd-30a14191b92f](./image/bccbf978-115a-4781-84fd-30a14191b92f.png)



![399af0d7-73ce-4a94-a5d5-36ca435589a4](./image/399af0d7-73ce-4a94-a5d5-36ca435589a4.png)



![00aa6574-278d-4a79-8b4a-1f3f89d277b6](./image/00aa6574-278d-4a79-8b4a-1f3f89d277b6.png)
![59ec096d-f671-4dd5-a1a5-4bc4141a7d9d](./image/59ec096d-f671-4dd5-a1a5-4bc4141a7d9d.png)

### Task

At the end of this task, I will have finished training models on the dataset and deployed the best model.

### Access

The dataset is hosted [here](https://raw.githubusercontent.com/thangtranquang/Azure-Machine-Learning-Engineer-2023/main/data/heart_failure_clinical_records_dataset.csv) . I will use the ` Dataset.Tabular.from_delimited_files()` to get the data from the url and save it to the datastore by using dataset.register().

## Automated ML

Automated ML select an algorithm and hyperparameters and generates a model ready for deployment model

![d052183d-9d67-404c-b919-8a615122b99e](./image/d052183d-9d67-404c-b919-8a615122b99e.png)

### Results

The best performing model is the `VotingEnsemble` with an Accuracy value of **0.87054**.

![073f21fd-2ae0-4530-a0e7-a9811ddfa54d](./image/073f21fd-2ae0-4530-a0e7-a9811ddfa54d.png)
![83a0db7a-c81e-4f3e-abc8-59c449d46741](./image/83a0db7a-c81e-4f3e-abc8-59c449d46741.png)


Best Model

![4f05f2e7-d963-4565-bb1b-f690f3b7cc6e](./image/4f05f2e7-d963-4565-bb1b-f690f3b7cc6e.png)

![a6f908ef-3b97-4bca-b260-c125f7df8dda](./image/a6f908ef-3b97-4bca-b260-c125f7df8dda.png)

### Improve AutoML

* Engineer more new features to improve model performance..
* Explore other AutoML configurations.

## Hyperparameter Tuning

I tried LogisticRegression for this experiment. Since this model is simple to understand and also handle both categorical and numerical data for this classification task.

### Results

![c69c4df4-58b0-45d5-ba51-dae218e9bb83](./image/c69c4df4-58b0-45d5-ba51-dae218e9bb83.png)



![aa1916b3-b018-4f10-aca1-c5f7a97b79dc](./image/aa1916b3-b018-4f10-aca1-c5f7a97b79dc.png)



![ab68b3f7-e565-45c5-9bf9-d24916fcb99e](./image/ab68b3f7-e565-45c5-9bf9-d24916fcb99e.png)



## Model Deployment

The AutoML model outperforms than the HyperDrive model, So

 I will have to deploy your best model as a webservice and test the model endpoint

![cdfd3fbd-7c69-4cc6-a509-b9d0e0071a18](./image/cdfd3fbd-7c69-4cc6-a509-b9d0e0071a18.png)

![b0d75246-3e0f-488a-9bbb-c1d7d7a2a338](./image/b0d75246-3e0f-488a-9bbb-c1d7d7a2a338.png)

![33917880-7cf3-45ac-be03-79bc30697e48](./image/33917880-7cf3-45ac-be03-79bc30697e48.png)



## Screen Recording

[Video Link](https://www.loom.com/share/a8eb241bde0a4413853735e25c5df876)

## Standout Suggestions

* Engineer more new features to improve model performance..
* Explore other AutoML configurations.
