import asyncio
from lean_explore.api.client import Client
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.tools import tool
# Load API key (ensure it's configured via CLI or ENV variable)
from dotenv import load_dotenv
import os
load_dotenv()
LEANEXPLORE_API_KEY = os.getenv("LEANEXPLORE_API_KEY")
if LEANEXPLORE_API_KEY is None:
    LEANEXPLORE_API_KEY=input("Please enter your Lean Explore API key: ")

client = Client(api_key=LEANEXPLORE_API_KEY)
print("API Client initialized.")

from typing import TypedDict
class SearchResponse(TypedDict):
    id : int | None
    theorem_name : str | None
    display_statement : str | None  
    docstring : str | None
    informal_description : str | None
    source_file : str | None
    range_start_line : int | None

@tool
async def search_lean_theorem(query_str: str) -> list[SearchResponse]:
    """
    Searches for Lean theorems based on the provided query string and displays the results.
    Args:
        query_str (str): The search query string.
    Returns:
        list [SearchResponse]

    SearchResponse: A dictionary containing search results. Each result includes:
        - id (int): The unique identifier of the theorem.
        - theorem_name (str): The name of the theorem.
        - display_statement (str): The display statement of the theorem.
        - docstring (str): The dictionary string representation of the theorem.
        - informal_description (str): The informal description of the theorem.
        - source_file (str): The source file where the theorem is defined.
        - range_start_line (int): The starting line number of the theorem's definition.
    """
    global client
    search_response_api =await client.search(query=query_str)
    res_ls=[]
    for item in search_response_api.results[:6]:
        search_response=SearchResponse(id=item.id,
                                       theorem_name=item.primary_declaration.lean_name
                    if item.primary_declaration else "N/A",
                                       display_statement=item.display_statement_text,
                                       docstring=item.docstring,
                                       informal_description=item.informal_description,
                                       source_file=item.source_file,
                                       range_start_line=item.range_start_line)
        res_ls.append(search_response)
    return res_ls

search = DuckDuckGoSearchResults(output_format="list")
@tool
def ddgs_search(query_str:str) -> str:
    """
    Searches the web for the given query string using DuckDuckGo.
    Args:
        query_str (str): The search query string.
    Returns:
        str: The search results."""
    return search.invoke(query_str)

if __name__ == "__main__":
       res=ddgs_search.invoke("Obama's first name?",)
       print(len(res))
