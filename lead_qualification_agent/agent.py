from google.adk.agents.llm_agent import Agent
from company_analysis_agent.schema import CompanyAnalysis
from .prompt import LEAD_QUALIFICATION_PROMPT
from .schema import LeadQualification

root_agent = Agent(
    model="gemini-3.5-flash",

    name="lead_qualification_agent",

    description="Evaluates whether a company is a qualified sales lead.",

    instruction=LEAD_QUALIFICATION_PROMPT,

    output_schema=LeadQualification,


    output_key="lead_qualification"
)