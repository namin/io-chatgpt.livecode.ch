# Steps to deploy in production

[![DigitalOcean](https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg)](https://www.digitalocean.com/?refcode=10856c6c1ff2)

These steps have been tested on a [DigitalOcean](https://www.digitalocean.com/?refcode=10856c6c1ff2) (referral link) docker application droplet.

- Clone the repository in `/var/www/` directory.
- `cd io-gpt`
- `python3 -m venv io-gpt-env`
- `source io-gpt-env/bin/activate`
- `pip install -r requirements.txt`
- `sudo cp deploy/io-gpt.service /etc/systemd/system/`
- `sudo systemctl start io-gpt`
- `sudo systemctl enable io-gpt`
- `sudo systemctl status io-gpt` (to check all OK)
- Edit `YOUR_DOMAIN` in deploy/io-gpt
- `sudo cp deploy/io-gpt /etc/nginx/sites-available/`
- `sudo ln -s /etc/nginx/sites-available/io-gpt /etc/nginx/sites-enabled`
- `sudo nginx -t`
- `sudo systemctl restart nginx`
- `sudo certbot --nginx -d YOUR_DOMAIN` (for SSL)
