from google.adk.agents.llm_agent import Agent
from llm_provider.factory import ProviderFactory
from .prompt import SERVICE_RECOMMENDATION_PROMPT
from .schema import ServiceRecommendation, ServiceRecommendationInput

root_agent = Agent(
    model=ProviderFactory.get_model(),

    name="service_recommendation_agent",

    description="Recommends suitable AI services for qualified companies.",

    instruction=SERVICE_RECOMMENDATION_PROMPT,


    output_schema=ServiceRecommendation,

    output_key="service_recommendation",
)