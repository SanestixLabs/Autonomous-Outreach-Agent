from google.adk.agents.llm_agent import Agent
from llm_provider.factory import ProviderFactory
from .prompt import COMPANY_ANALYSIS_PROMPT
from .schema import CompanyAnalysis

root_agent = Agent(
    model=ProviderFactory.get_model(),

    name="company_analysis_agent",

    description="Analyzes company information for autonomous outreach.",

    instruction=COMPANY_ANALYSIS_PROMPT,

    output_schema=CompanyAnalysis,

    output_key="company_analysis",
)
