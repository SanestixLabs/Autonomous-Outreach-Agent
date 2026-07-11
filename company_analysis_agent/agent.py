from google.adk.agents.llm_agent import Agent
from .prompt import COMPANY_ANALYSIS_PROMPT

root_agent = Agent(
    model="gemini-3.5-flash",

    name="company_analysis_agent",

    description="Analyzes company information for autonomous outreach.",

    instruction=COMPANY_ANALYSIS_PROMPT,
)