from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
load_dotenv()


def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        markdown=True,
        tools=[DuckDuckGoTools()],
        instructions="U are an agent who explain concept to student in simple language. (explain everything in short like 5 lines)",
        add_datetime_to_context=True
    )


groq_agent = build_agent()

groq_agent.print_response(
    "Explain ollama?"
)