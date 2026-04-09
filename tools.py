from langchain.tools import Tool
from langchain_community.tools.tavily_search import TavilySearchResults

search = TavilySearchResults()

search_tool = Tool(
    name="Search",
    func=search.run,
    description="Use this for latest news and real-time information"
)
