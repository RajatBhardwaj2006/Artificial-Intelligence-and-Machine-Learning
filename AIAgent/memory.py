from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint

load_dotenv()

db = SqliteDb(db_file="Agent_memory.db")

# Clear existing memories
db.clear_memories()


def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        markdown=True,
        db=db,
        add_history_to_context=True,
        enable_agentic_memory=True,
    )


groq_agent = build_agent()

user_id = "rajat@gmail.com"

groq_agent.print_response(
    "My name is Rajat",
    user_id=user_id
)

groq_agent.print_response(
    "What is my name ? ",
    user_id=user_id
)

memories = groq_agent.get_user_memories(user_id=user_id)

pprint(memories)