from google.adk.agents import Agent
from config import MODEL
from tools.cache_tools import load_cache

summary_agent = Agent(
    name="summary_agent",
    model=MODEL,
    instruction="""
You are a research paper summarization expert.

Steps:
1. Call load_cache tool to retrieve the paper content.
2. Summarize based on the retrieved content:
   - Contribution: what problem is solved and why it matters
   - Methodology: how it was done
   - Key findings: main results and conclusions
""",
    tools=[load_cache]
)
