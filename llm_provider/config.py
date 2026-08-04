from common.enums import ProviderType

DEFAULT_PROVIDER = ProviderType.GEMINI

PROVIDER_MODELS = {
    ProviderType.GEMINI: "gemini-3.5-flash",
    ProviderType.GROQ: "llama-3.3-70b-versatile",
    ProviderType.OPENAI: "gpt-5",
}