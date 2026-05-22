from google.adk.agents import Agent
from config import MODEL
from tools.cache_tools import load_cache

qa_agent = Agent(
    name="qa_agent",
    model=MODEL,
    instruction="""
You are a technical Q&A assistant for research papers.

Steps:
1. Call load_cache tool to retrieve the paper content.
2. Answer the user's question strictly based on the paper content.
3. If the answer is not in the paper, say so clearly.
""",
    tools=[load_cache]
)
