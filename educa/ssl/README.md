To create `educa.crt` and `educa.key` run following command from this directory

```shell
openssl req -x509 -newkey rsa:2048 -sha256 -days 3650 -nodes \
  -keyout educa.key -out educa.crt \
  -subj '/CN=*.educaproject.com' \
  -addext 'subjectAltName=DNS:*.educaproject.com'
```
