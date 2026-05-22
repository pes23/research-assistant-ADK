from google.adk.agents import Agent
from config import MODEL
from tools.paper_tools import load_paper

from agents.summary_agent import summary_agent
from agents.critic_agent import critique_agent
from agents.qa_agent import qa_agent
from agents.insight_agent import insight_agent

coordinator = Agent(
    name="coordinator",
    model=MODEL,
    instruction="""
You are the coordinator of a paper analysis system.

If the user wants to load a paper, call load_paper tool with the file path.
  - Default path: "data/paper.pdf"
  - Example trigger: "load paper", "analyze this paper", "read paper"

Otherwise, route to the appropriate sub-agent:
  - summarize / overview / contributions  → summary_agent
  - critique / weakness / limitation      → critique_agent
  - why / how / what / explain            → qa_agent
  - future / application / extension      → insight_agent

Always choose exactly one action.
""",
    tools=[load_paper],
    sub_agents=[summary_agent, critique_agent, qa_agent, insight_agent]
)
