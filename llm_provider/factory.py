from llm_provider.config import (
    DEFAULT_PROVIDER,
    PROVIDER_MODELS,
)


class ProviderFactory:

    @staticmethod
    def get_model() -> str:

        model = PROVIDER_MODELS.get(DEFAULT_PROVIDER)

        if model is None:
            raise ValueError(
                f"Unsupported provider: {DEFAULT_PROVIDER}"
            )

        return model