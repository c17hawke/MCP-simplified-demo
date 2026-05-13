import os
from typing import Any
from fastmcp import FastMCP
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY environment variable is not set.")

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)
mcp = FastMCP(name="SimpleServer")

def _web_search(query: str) -> str:
    """Perform a web search using Tavily."""
    results = tavily_client.search(query)
    return results

@mcp.tool(annotations={"title": "Simple Web Search"})
def web_search(query: str) -> str:
    """A Simple web search tool that uses Tavily to perform searches and return results.

    Args:
        query (str): The search query to be performed.

    Returns:
        str: The search results returned by Tavily.
    """
    search_results = _web_search(query)
    return f"{search_results}"

@mcp.resource("resource://response_formatting_instructions")
def response_formatting_instructions() -> str:
    """Provide guidelines for how the LLM should format its responses when using the tools."""
    return """Markdown formatting instructions: 1. Use headings (##) for each section. 2. Use bullet points for lists. 3. Include URLs as hyperlinks. 4. Use bold for important points. 5. Keep the response concise and informative. 6. Use tables if needed to present structured data clearly."""

@mcp.prompt
def main_prompt(query: str, formatting_instructions: str, search_results: str) -> str:
    """The main prompt that the LLM will use to generate responses.
    
    Args:
        query (str): The user's search query.
        formatting_instructions (str): The guidelines for how the LLM should format its response.
        search_results (str): The results from the web search tool.

    Returns:
        str: The prompt that will be used by the LLM to generate a response.
    """
    return f"""You are a helpful assistant who takes the user query and search results and provides a concise and informative response. Use the following formatting guidelines: ```{formatting_instructions}```. Here is the user query: `{query}`. Here are the search results: ```{search_results}```. Please provide a well-formatted response based on the query and search results."""

if __name__ == "__main__":
    mcp.run(transport="streamable-http")