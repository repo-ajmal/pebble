## Getting Started

How to install KEDA

## 1. Install KEDA
Add helm repo

``` bash
helm repo add kedacore https://kedacore.github.io/charts
```
Update Repo

``` bash
helm repo update
```

Install KEDA

``` bash
helm install keda kedacore/keda --namespace keda --create-namespace

kubectl get deployment -n keda
```


## 2. Deploy sample nginx deployment

``` bash
kubectl create -f https://k8s.io/examples/application/deployment.yaml

kubectl get deployment
```

## 3. Deploy ScaledObjects

Prometheus Scaler

``` bash
kubectl apply -f PrometheusScaler.yaml

kubectl apply -f CronScaler.yaml
```