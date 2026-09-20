from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
load_dotenv()


def build_finance_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        markdown=True,
        tools=[YFinanceTools()],
        add_datetime_to_context=True,
        instructions=["format your response using markdown and use tables to display data where possible"],
        description="you are an investment analyst that research stock prices and recommandation and stock.",
        debug_mode=True
    )


groq_agent = build_finance_agent()

groq_agent.print_response(
    "I want to start buying stock, But i don't know which stock to but i have 10k inr to invest. Suggest me best stock to invest.."
)