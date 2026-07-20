from google.adk.agents.llm_agent import Agent

from .prompt import PERSONALIZED_EMAIL_PROMPT
from .schema import PersonalizedEmail, PersonalizedEmailInput

root_agent = Agent(
    model="gemini-3.5-flash",

    name="personalized_email_agent",

    description="Generates personalized outreach emails for qualified companies.",

    instruction=PERSONALIZED_EMAIL_PROMPT,


    output_schema=PersonalizedEmail,

    output_key="personalized_email",
)