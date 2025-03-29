!pip install langchain langchain_groq 
!pip install tavily-python
import os

# the code explaination is in Readme file

from tavily import TavilyClient

print('start location')
Query=str(input())
print('destination')
Query0=str(input())
print('provide your travel date')
Query1=str(input())
print('provide your budget')
Query2=str(input())
print('provide extra preferences')
Query3=str(input())
Query='travel plan for'+Query+'to'+Query0+'on'+Query1+'under the budget of'+Query2+'with'+Query3 +'with nice hotels for stay and dine'
tavily_client = TavilyClient(api_key="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")

# Step 2. Executing the search request
response = tavily_client.search(Query, search_depth = "advanced", max_results=5)
# Step 3. Printing the search results
urls=[]
for result in response['results']:
  url=result['url']
  urls.append(url)
response = tavily_client.extract(urls=urls, include_images=False)
Information=''
for result in response['results']:
  Information=Information+result['raw_content']

from langchain_groq import ChatGroq
llm= ChatGroq(temperature=0, groq_api_key="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", model_name="llama-3.3-70b-versatile" )
result=llm.invoke("use" + str(Information[:1000])+ "and give a travel plan")
result.content
