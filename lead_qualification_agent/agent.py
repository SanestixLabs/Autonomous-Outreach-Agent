from google.adk.agents.llm_agent import Agent
from company_analysis_agent.schema import CompanyAnalysis
from llm_provider.factory import ProviderFactory
from .prompt import LEAD_QUALIFICATION_PROMPT
from .schema import LeadQualification

root_agent = Agent(
    model=ProviderFactory.get_model(),

    name="lead_qualification_agent",

    description="Evaluates whether a company is a qualified sales lead.",

    instruction=LEAD_QUALIFICATION_PROMPT,

    output_schema=LeadQualification,


    output_key="lead_qualification"
)