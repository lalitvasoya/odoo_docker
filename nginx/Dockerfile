FROM nginx:latest

USER root

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

# RUN apt update
# RUN apt install -y nano apt-utils certbot python3-certbot-nginx
# RUN apt-get install iputils-ping -y
# RUN apt install iproute2 -y
# COPY nginx.conf /etc/nginx/site-enable/nginx.conf
