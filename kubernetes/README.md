# Kubernetes Deployment

This folder contains Kubernetes manifests for deploying the TalentIQ AI Candidate Ranking System.

## Resources

- Namespace
- Deployment
- Service
- ConfigMap
- Secret
- Horizontal Pod Autoscaler
- Ingress

## Commands

kubectl apply -f namespace.yaml

kubectl apply -f deployment.yaml

kubectl apply -f service.yaml

kubectl apply -f configmap.yaml

kubectl apply -f secret.yaml

kubectl apply -f hpa.yaml

kubectl apply -f ingress.yaml