from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team
load_dotenv()


english_agent = Agent(name="English Agent", role="You Answer questions in english")
german_agent = Agent(name="German Agent", role="You Answer questions in German")
spanish_agent = Agent(name="Spanish Agent", role="You Answer questions in Spanish")

Team_Leader = Team(
    name = "Answer & Translation Team",
    members=[english_agent, german_agent, spanish_agent],
    model=Groq(id="openai/gpt-oss-120b"),
    markdown=True,
    show_members_responses=True,
    instructions="""
                        All Member agent must response to answer the query in their langugae.
                        show output of all the agents 
                        do not route to just one agent 
                """
)

Team_Leader.print_response("What is the capital of India?")

#! OUTPUT

#*                                                                               ┃
#* Answer in English: New Delhi                                                  ┃
#*                                                                               ┃
#* Antwort auf Deutsch: Neu‑Delhi                                                ┃
#*                                                                               ┃
#* Respuesta en español: Nueva Delhi                                             ┃
#*                                    