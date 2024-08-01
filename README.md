# ChatGPT plugins or actions quickstart

Get a ChatGPT plugin or action up and running in under 5 minutes using Python. This plugin is designed to work in conjunction with the [ChatGPT GPT actions documentation](https://platform.openai.com/docs/plugins).

## Demo

For integration with [io.livecode.ch](https://io.livecode.ch), see and feel free to use [io-gpt.livecode.ch](https://io-gpt.livecode.ch/).

## Setup locally

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

To run the plugin, enter the following command:

```bash
python main.py
```

Note that you can no longer use `localhost` with GPT actions (this was possible with the deprecated plugins).
For testing, perhaps you could a remote tunneling option?

## Setup remotely

### [DigitalOcean](deploy)

## Getting help

If you run into issues or have questions building a plugin or action, please join OpenAI's [Developer community forum](https://community.openai.com/c/chat-plugins/20).
