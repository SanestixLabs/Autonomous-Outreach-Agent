from google.adk.agents.llm_agent import Agent

from .prompt import SERVICE_RECOMMENDATION_PROMPT
from .schema import ServiceRecommendation, ServiceRecommendationInput

root_agent = Agent(
    model="gemini-3.5-flash",

    name="service_recommendation_agent",

    description="Recommends suitable AI services for qualified companies.",

    instruction=SERVICE_RECOMMENDATION_PROMPT,

    input_schema=ServiceRecommendationInput,

    output_schema=ServiceRecommendation,
)