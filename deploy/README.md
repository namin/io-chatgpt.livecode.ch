# How to deploy a ChatGPT plugin or action to production with DigitalOcean

[![DigitalOcean](https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg)](https://www.digitalocean.com/?refcode=10856c6c1ff2)

These steps have been tested on a [DigitalOcean](https://www.digitalocean.com/?refcode=10856c6c1ff2) (referral link) docker application droplet.

## Showcase

We can create a GPT similar to the [io.livecode.ch GPT](https://chat.openai.com/g/g-PfamS7B7f-io-livecode-ch).
Here is some example transcript:
- [_Explain a MaxSAT problem and write it in the z3-solver python library._](https://chat.openai.com/share/c897b33c-6919-4638-a005-334015205cc8)

## Prerequisites

Follow all the prerequisites, all the step 1 and and part of step 2 (only the first `sudo apt-get install ...`) of [this guide](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04#prerequisites).

## Steps on Server

- Clone the repository in `/var/www/` directory.
  - `cd /var/www/`
  - `git clone https://github.com/namin/io-chatgpt.livecode.ch.git io-gpt`
  - If you get permission denied, you need to give your user permissions to write in this directory:
    - `sudo chown root:www-data /var/www`
    - `sudo chmod g+w /var/www`
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
- Import from URL. Put https://_YOUR_DOMAIN_/openapi.yaml just configured above. Import.
- For the Privacy Policy, you can put _YOUR_DOMAIN_.
- Test it!
- (You can try my server io-gpt.livecode.ch for _YOUR_DOMAIN_.) 

## Debugging
As explained in the [prerequisite guide](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04#step-6-securing-the-application), you can access the logs of your application with `sudo journalctl -u io-gpt`.

To restart the service after a change, `sudo systemctl restart io-gpt`.

You can manually send a POST request to the server.

```
curl -X POST 'https://io-gpt.livecode.ch/run/namin/pyfun' \
-H 'Content-Type: application/json' \
-d '{"main": "print(41+1)"}'
```

should return

```
{"result": "42\n"}%
```
