# How to deploy a ChatGPT plugin or action to production with DigitalOcean

[![DigitalOcean](https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg)](https://www.digitalocean.com/?refcode=10856c6c1ff2)

These steps have been tested on a [DigitalOcean](https://www.digitalocean.com/?refcode=10856c6c1ff2) (referral link) docker application droplet.

## Prerequisites

Follow all the prerequisites, all the step 1 and and part of step 2 (only the first `sudo apt-get install ...`) of [this guide](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04#prerequisites).

## Steps on Server

- Clone the repository in `/var/www/` directory.
  - `cd /var/www/`
  - `git clone https://github.com/namin/io-chatgpt.livecode.ch.git io-gpt`
- `cd io-gpt`
- `python3 -m venv io-gpt-env`
- `source io-gpt-env/bin/activate`
- `pip install -r requirements.txt`
- `sudo cp deploy/io-gpt.service /etc/systemd/system/`
- `sudo systemctl start io-gpt`
- `sudo systemctl enable io-gpt`
- `sudo systemctl status io-gpt` (to check all OK)
- Edit `YOUR_DOMAIN` in `deploy/io-gpt`
- `sudo cp deploy/io-gpt /etc/nginx/sites-available/`
- `sudo ln -s /etc/nginx/sites-available/io-gpt /etc/nginx/sites-enabled`
- `sudo nginx -t`
- `sudo systemctl restart nginx`
- `sudo certbot --nginx -d YOUR_DOMAIN` (for SSL)

## Steps to setup a GPT action in ChatGPT
- Go to [chat.openai.com](https://chat.openai.com)
- Explore -> Create a GPT -> Configure.
- Scroll down to create new action.
- Import from URL. Put _YOUR_DOMAIN/openapi.yaml_ just configured above. Import.
- For the Privacy Policy, you can put _YOUR_DOMAIN_.
- Test it!
