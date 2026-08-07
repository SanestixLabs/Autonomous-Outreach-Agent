from litellm import Router
from google.adk.models.lite_llm import LiteLlm

from llm_provider.client import RouterLiteLLMClient
from llm_provider.config import (
    DEFAULT_PROVIDER,
    PROVIDER_MODELS,
    MODEL_LIST,
    FALLBACKS,
    NUM_RETRIES,
)


class ProviderFactory:

    @staticmethod
    def get_model() -> LiteLlm:

        model_group = PROVIDER_MODELS.get(DEFAULT_PROVIDER)

        if model_group is None:
            raise ValueError(
                f"Unsupported provider: {DEFAULT_PROVIDER}"
            )

        router = Router(
            model_list=MODEL_LIST,
            fallbacks=FALLBACKS,
            num_retries=NUM_RETRIES,
        )

        client = RouterLiteLLMClient(router)

        return LiteLlm(
            model=model_group,
            llm_client=client,
        )