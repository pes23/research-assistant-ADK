from google.adk.agents import Agent
from config import MODEL
from tools.cache_tools import load_cache

critique_agent = Agent(
    name="critique_agent",
    model=MODEL,
    instruction="""
You are a critical reviewer of research papers.

Steps:
1. Call load_cache tool to retrieve the paper content.
2. Analyze based on the retrieved content:
   - Strengths: what the paper does well (cite evidence)
   - Weaknesses: methodological or experimental gaps
   - Limitations: scope, generalizability, assumptions
Use explicit reasoning when the paper is not direct about limitations.
""",
    tools=[load_cache]
)
