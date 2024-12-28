# Custom OpenAI API for Home Assistant

[![Validate with hassfest](https://github.com/hekmon/ha-openaicust/actions/workflows/hassfest.yaml/badge.svg)](https://github.com/hekmon/ha-openaicust/actions/workflows/hassfest.yaml)
[![Validate with HACS](https://github.com/hekmon/ha-openaicust/actions/workflows/hacs.yaml/badge.svg)](https://github.com/hekmon/ha-openaicust/actions/workflows/hacs.yaml)

Custom OpenAI API for Home Assistant is a fork of the [original](https://github.com/home-assistant/core/tree/2024.12.5/homeassistant/components/openai_conversation) [OpenAI Conversation](https://www.home-assistant.io/integrations/openai_conversation/) integration with additional features and improvements such as:

- Custom base URL for OpenAI API allowing to use it with any model/inference server (tools still must be supported by both of them) with OpenAI API support
- Support for multiple instances
- vLLM custom `repetition_penalty` parameter
- Image size free input
- Image generation model name customization

## Installation

### HACS

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=hekmon&repository=ha-openaicust&category=integration)

More on HACS [here](https://hacs.xyz/).

### Manually

Download the integration from the [releases](https://github.com/hekmon/ha-openaicust/releases) page and decompress the `custom_components/openai_api_conversation` folder within your Home Assistant configuration directory. You must get: `/path/to/homeassistant/configdir/custom_components/openai_api_conversation` if your Home Assistant config file is `/path/to/homeassistant/configdir/configuration.yaml`.

## Configuration

Once the integration has been installed and Home Assistant restarted, navigate to the integrations page, select the `Add Integration` button and search for `Custom OpenAI API Conversation`. Set a name, API key and a base URL: setup will test the connection. If the connection is successful, the integration will be added and the advanced configuration options will be available.

If you want to add more targets, simply repeat the process.
