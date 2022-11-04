# EzMetrics
## _The eaziest metrics library ever_

Ez metrics is a library that calculates the fitness metrics of your ML model.

## Features

- Support for fixed binary classification as well as probability based classification
- Support for regression models
- Up to 6 different metrics



And of course EzMetrics itself is open source with a [public repository][ezm] on GitHub.

## Installation

EzMetrics requires no extra libraries to run.

```sh
pip install EzMetrics as ezm
```
## Usage

Create an object containing a list with the predictions of your model and a list 
containing the actual values por each prediction.

```sh
exmpl_obj = EzMetrics( predicted_list, observed_list)
```

Then just choose a metric suited for your data and use it. 
In case of Mean Absolute Error it would be as follows.

```sh
exmpl_obj.mae()
```


## Metrics

EzMetrics has 6 different metrics available, which one to use depends on your data type.

| Discrete classification |  |
| ------ | ------ |
| Accuracy | EzMetrics.accuracy() |
| F1 score | EzMetrics.f1() |


| Probability classification |  |
| ------ | ------ |
| Area Under the Curve (AUC) | EzMetrics.roc_auc() |


| Regression |  |
| ------ | ------ |
| R squared | EzMetrics.r2() |
| Mean Absolute Error | EzMetrics.mae() |
| Mean Squared Error | EzMetrics.mse() |


## License

MIT

   [ezm]: <https://github.com/JieWuu/EzMetrics>
