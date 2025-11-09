# Build des images locales
docker build -t ai-module:latest ./ai-module
docker build -t fastapi:latest ./fastapi
docker build -t nginx-custom:latest ./nginx

# Copier dans k3s (si tu utilises k3d ou containerd)
# k3s ctr images import <(docker save ai-module:latest)
# k3s ctr images import <(docker save fastapi:latest)
# k3s ctr images import <(docker save nginx-custom:latest)


kubectl apply -f k8s/




Préparer les images locales sur le Raspberry
Pour Nginx
cd ~/Documents/AI/k8s/nginx

# Build l'image sur le Pi
docker build -t nginx-custom:latest .
docker save nginx-custom:latest -o nginx-custom.tar
sudo k3s ctr images import nginx-custom.tar
sudo k3s ctr images list | grep nginx-custom

Pour FastAPI
cd ~/Documents/AI/k8s/fastapi
docker build -t fastapi:latest .
docker save fastapi:latest -o fastapi.tar
sudo k3s ctr images import fastapi.tar
sudo k3s ctr images list | grep fastapi

Pour AI module
cd ~/Documents/AI/k8s/ai-module
docker build -t ai-module:latest .
docker save ai-module:latest -o ai-module.tar
sudo k3s ctr images import ai-module.tar
sudo k3s ctr images list | grep ai-module