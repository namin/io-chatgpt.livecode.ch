server {
    server_name io-chatgpt.livecode.ch;
    listen 80;
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/namin/io-chatgpt.livecode.ch/io-chatgpt.sock;
    }
}