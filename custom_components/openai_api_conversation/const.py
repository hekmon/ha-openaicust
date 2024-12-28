"""Constants for the Custom OpenAI API Conversation integration."""

import logging

DOMAIN = "openai_api_conversation"
LOGGER = logging.getLogger(__package__)

CONF_INSTANCE_NAME = "instance_name"
RECOMMENDED_API_KEY = "-"
CONF_BASE_URL = "base_url"
RECOMMENDED_BASE_URL = "https://api.openai.com/v1"

CONF_PROMPT = "prompt"
CONF_CHAT_MODEL = "chat_model"
RECOMMENDED_CHAT_MODEL = "gpt-4o-mini"
CONF_MAX_TOKENS = "max_tokens"
RECOMMENDED_MAX_TOKENS = 150
CONF_TOP_P = "top_p"
RECOMMENDED_TOP_P = 1.0
CONF_TEMPERATURE = "temperature"
RECOMMENDED_TEMPERATURE = 1.0
CONF_REPETITION_PENALTY = "repetition_penalty"
RECOMMENDED_REPETITION_PENALTY = 1.0

CONF_IMAGE_MODEL = "image_model"
RECOMMENDED_IMAGE_MODEL = "dall-e-3"
