server {
    server_name io-gpt.livecode.ch;
    listen 80;
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/namin/io-gpt.livecode.ch/io-gpt.sock;
    }
}