# k8s-secret-gen

Given this Kubernetes deployment YAML

```yaml
apiVersion: v1
kind: Deployment
metadata:
  name: my-awesome-pod
spec:
  replicas: 1
  selector:
    app_name: my-awesome-pod
  template:
    metadata:
      labels:
        app_name: my-awesome-pod
    spec:
      containers:
        - name: my-awesome-pod
          image: my-awesome-container-image:latest
          imagePullPolicy: Always
          env:
            - name: ENV
              value: production
            - name: DB_DATABASE
              value: "my_awesome_database"
            - name: DB_PASSWORD
              value: "my_awesome_password"
            - name: DB_PORT
              value: "12345"
            - name: DB_USER
              value: "my_awesome_user"
            - name: ANY_API_KEY
              value: "GallowsUnicycleLanguageJollyNavigateThrive"
```

The output will be

```yaml
apiVersion: v1
data:
  - ENV: cHJvZHVjdGlvbg==
  - DB_DATABASE: bXlfYXdlc29tZV9kYXRhYmFzZQ==
  - DB_PASSWORD: bXlfYXdlc29tZV9wYXNzd29yZA==
  - DB_PORT: MTIzNDU=
  - DB_USER: bXlfYXdlc29tZV91c2Vy
  - ANY_API_KEY: R2FsbG93c1VuaWN5Y2xlTGFuZ3VhZ2VKb2xseU5hdmlnYXRlVGhyaXZl
kind: Secret
metadata:
  name: secrets-my-awesome-pod
type: Opaque

---
env:
  - name: ENV
    valueFrom:
      secretKeyRef:
        key: ENV
        name: secrets-my-awesome-pod
  - name: DB_DATABASE
    valueFrom:
      secretKeyRef:
        key: DB_DATABASE
        name: secrets-my-awesome-pod
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        key: DB_PASSWORD
        name: secrets-my-awesome-pod
  - name: DB_PORT
    valueFrom:
      secretKeyRef:
        key: DB_PORT
        name: secrets-my-awesome-pod
  - name: DB_USER
    valueFrom:
      secretKeyRef:
        key: DB_USER
        name: secrets-my-awesome-pod
  - name: ANY_API_KEY
    valueFrom:
      secretKeyRef:
        key: ANY_API_KEY
        name: secrets-my-awesome-pod
---

```
