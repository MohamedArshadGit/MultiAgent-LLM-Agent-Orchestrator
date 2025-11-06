from langchain.agents import Tool
from playwright.async_api import async_playwright
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_experimental.tools import PythonREPLTool
import os
from dotenv import load_dotenv
import requests

load_dotenv(override = True)

async def playwright_tools():
    playwright =await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    toolkit =PlayWrightBrowserToolkit.from_browser(browser=browser)
    return toolkit.get_tools(),browser,playwright

def file_management_tool():
    toolkit =FileManagementToolkit(root_dir=r'MultiAgent_llm_lab\sandbox')
    tools =toolkit.get_tools()
    #print('file_management_tool','\t',tools)
    return tools

#pushover tool
pushover_url ='https://api.pushover.net/1/messages.json'
pushover_token =os.getenv('PUSHOVER_API')
pushover_user =os.getenv('PUSHOVER_USER')

def push(text):
    requests.post(url=pushover_url,data={"user":pushover_user,"token":pushover_token,"message":text})
    return 'push notification successful'


#helper function to need langchain tool wrapper or not
#tool wrapping needed for custom tools or attributes like when name,description ,run is not defined
def needs_wrapping(obj):
    return not (hasattr(obj, "name") and hasattr(obj, "description") and hasattr(obj, "run"))

print(needs_wrapping(PythonREPLTool()))  
print(needs_wrapping(WikipediaAPIWrapper()))  
print(needs_wrapping(GoogleSerperAPIWrapper()))

async def other_tools():

    #file_management tool
    file_tool =file_management_tool()

    #push notification tool
    tool_push =Tool(name='push_notification',
    func=push,
    description='send push notification')

    #serper api tool
    serper=GoogleSerperAPIWrapper()

    #serper internet search tool
    tool_search = Tool(
    name="google_search",
    func=serper.run,
    description="Search Google using Serper API")

    
    #wikipedia tool
    wiki_api_wrapper =WikipediaAPIWrapper()
    wiki_tool =WikipediaQueryRun(api_wrapper=wiki_api_wrapper) 
    #Option 1: Prebuilt tool wrapper like above
    # or below manual tool wrapping like Tool(name,func etc also can be done without importing Prebuilt tool wrapper WikipediaQueryRun like below )
    
    #wikipedia = WikipediaAPIWrapper()
    # wiki_tool = Tool(
    #     name="wikipedia_lookup",
    #     func=wikipedia.run,
    #     description="Search Wikipedia articles and return relevant information"
    # )

    #python repl tool
    python_repl = PythonREPLTool()







    