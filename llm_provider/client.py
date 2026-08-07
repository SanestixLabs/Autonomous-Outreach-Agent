from litellm import Router
from google.adk.models.lite_llm import LiteLLMClient


class RouterLiteLLMClient(LiteLLMClient):
    """LiteLLM client backed by a LiteLLM Router."""

    def __init__(self, router: Router):
        self.router = router

    async def acompletion(
        self,
        model,
        messages,
        tools,
        **kwargs,
    ):
        return await self.router.acompletion(
            model=model,
            messages=messages,
            tools=tools,
            **kwargs,
        )

    def completion(
        self,
        model,
        messages,
        tools,
        stream=False,
        **kwargs,
    ):
        return self.router.completion(
            model=model,
            messages=messages,
            tools=tools,
            stream=stream,
            **kwargs,
        )