# drf-boilerplate
django rest framework kullanım için hazır araç gereç ve örnek bir admin uygulaması

## Neler var
* Arkayüzde için django, django-rest-framework, postgresql
* Önyüz için webpack
* Geliştirme ve canlı ortam için docker

### Kurulum
İnternet yavaş olduğu için imajı dockera pushlayamadım. O yüzden lokalde build etmelisiniz.


#### localhost uzerinden projeyi ayaga kaldirmak
docker-compose.yml dosyası içerisinde 28.satırdaki port şu şekilde değiştirilir;


...
web:
    image: drf-boilerplate:latest
    restart: on-failure
    command: gunicorn --error-logfile /var/log/gunicorn-error-log --bind 0.0.0.0:8080 admin.wsgi
    volumes:
      - .:/code
    ports:
      - 8000:8000 // bu kısım
    depends_on:
      - database
...



cp .env.example .env
make bundle && make build
docker-compose up

### Çalıştırma
Geliştirme ortamı (attach)

make development 


Canlı ortam (nginx)

make production 


## Docker içine girme
docker ps
drf-boilerplate:latest container id ile docker exe edilir (ORN container id = 92d7d60c4e44)
docker exec -it 92d7d60c4e44 /bin/bash

## Super User oluşturma

python manage.py createsuperuser


api endpoints
http://localhost/api/v1/categories/
http://localhost/api/v1/posts/