from os import getenv

from common.enums import ProviderType

DEFAULT_PROVIDER = ProviderType.GEMINI

# Router model groups
PROVIDER_MODELS = {
    ProviderType.GEMINI: "gemini",
    ProviderType.GROQ: "groq",
    ProviderType.OPENAI: "openai",
}

MODEL_LIST = [
    {
        "model_name": "gemini",
        "litellm_params": {
            "model": "gemini/gemini-3.5-flash",
            "api_key": getenv("GOOGLE_API_KEY"),
        },
    },
    {
        "model_name": "groq",
        "litellm_params": {
            "model": "groq/llama-3.3-70b-versatile",
            "api_key": getenv("GROQ_API_KEY"),
        },
    },
]

FALLBACKS = [
    {
        "gemini": ["groq"],
    }
]

NUM_RETRIES = 2