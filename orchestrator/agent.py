from google.adk.agents.sequential_agent import SequentialAgent

from company_analysis_agent.agent import root_agent as company_analysis_agent
from lead_qualification_agent.agent import root_agent as lead_qualification_agent
from service_recommendation_agent.agent import (
    root_agent as service_recommendation_agent,
)
from personalized_email_agent.agent import (
    root_agent as personalized_email_agent,
)

root_agent = SequentialAgent(
    name="outreach_orchestrator",

    description=(
        "Runs the complete autonomous outreach workflow from "
        "company analysis to personalized email generation."
    ),

    sub_agents=[
        company_analysis_agent,
        lead_qualification_agent,
        service_recommendation_agent,
        personalized_email_agent,
    ],
)