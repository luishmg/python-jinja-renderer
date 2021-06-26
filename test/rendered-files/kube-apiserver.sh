#!/bin/bash

INTERNAL_IP=$(ip addr show eth1 | grep "inet " | awk '{print $2}' | cut -d / -f 1)

cat <<EOF | sudo tee /etc/systemd/system/kube-apiserver.service
[Unit]
Description=Kubernetes API Server
Documentation=https://github.com/kubernetes/kubernetes

[Service]
ExecStart=/usr/local/bin/kube-apiserver \\
  --advertise-address=${INTERNAL_IP} \\
  --allow-privileged=true \\
  --apiserver-count=3 \\
  --audit-log-maxage=30 \\
  --audit-log-maxbackup=3 \\
  --audit-log-maxsize=100 \\
  --audit-log-path=/var/log/audit.log \\
  --authorization-mode=Node,RBAC \\
  --bind-address=0.0.0.0 \\
  --client-ca-file=/var/lib/kubernetes/pki/cat.pem \\
  --enable-admission-plugins= \\
  --enable-swagger-ui=true \\
  --enable-bootstrap-token-auth=true \\
  --etcd-cafile=/var/lib/kubernetes/pki/cat.pem \\
  --etcd-certfile=/var/lib/kubernetes/pki/etcd.pem \\
  --etcd-keyfile=/var/lib/kubernetes/pki/etcd-key.pem \\
  --etcd-servers=https://10.1.0.11:2379,https://10.1.0.12:2379,https://10.1.0.13:2379 \\
  --event-ttl=1h \\
  --encryption-provider-config=/var/lib/kubernetes/encryption-config.yaml \\
  --kubelet-certificate-authority=/var/lib/kubernetes/pki/cat.pem \\
  --kubelet-client-certificate=/var/lib/kubernetes/pki/kubernetes.pem \\
  --kubelet-client-key=/var/lib/kubernetes/pki/kubernetes-key.pem \\
  --kubelet-https=true \\
  --runtime-config=api/all=true \\
  --service-account-key-file=/var/lib/kubernetes/pki/service-account.pem \\
  --service-account-signing-key-file=/var/lib/kubernetes/pki/service-account-key.pem \\
  --service-account-issuer=https://kubernetes.default.svc.cluster.local \\
  --api-audiences=https://10.1.0.21,https://10.1.0.22,https://10.1.0.23 \\
  --service-cluster-ip-range=10.200.0.0 \\
  --service-node-port-range=30000-32767 \\
  --tls-cert-file=/var/lib/kubernetes/pki/kubernetes.pem \\
  --tls-private-key-file=/var/lib/kubernetes/pki/kubernetes-key.pem \\
  --v=1.20.2
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF