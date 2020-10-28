docker build -t kanbanfrontend .
docker run \
-p 8080:80 \
-d --name vueApp \
kanbanfrontend