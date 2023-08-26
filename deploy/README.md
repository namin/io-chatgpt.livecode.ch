# Steps to deploy in production

[![DigitalOcean](https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg)](https://www.digitalocean.com/?refcode=10856c6c1ff2)

These steps have been tested on a [DigitalOcean](https://www.digitalocean.com/?refcode=10856c6c1ff2) (referral link) docker application droplet.

- Clone the repository in your home directory. Assumes `$USER` is `namin` from now on.
- `cd io-chatgpt.livecode.ch`
- `python3 -m venv io-chatgpt-env`
- `source io-chatgpt-env/bin/activate`
- `pip install -r requirements.txt`
- `sudo cp deploy/io-chatgpt.service /etc/systemd/system/`
- `sudo systemctl start io-chatgpt`
- `sudo systemctl enable io-chatgpt`
- `sudo systemctl status io-chatgpt` (to check all OK)
- `sudo cp deploy/io-chatgpt.livecode.ch /etc/nginx/sites-available/`
- `sudo ln -s /etc/nginx/sites-available/io-chatgpt.livecode.ch /etc/nginx/sites-enabled`
- `sudo nginx -t`
- `sudo systemctl restart nginx`
- `sudo certbot --nginx -d io-chatgpt.livecode.ch` (for SSL)
