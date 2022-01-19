### Example of REDIS with TLS

#### Generate certificates
```bash
make
```
Certificates will be created in **ops/tls/** directory

#### Run app
```bash
docker-compose build
docker-compose run app
```