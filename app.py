# We first make a tool to get the cargo plane transfer time.
from smolagents import tool
from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool, VisitWebpageTool, ToolCallingAgent

import os

@tool
def calculate_relocation_costs(
    median_sales_price_origin: float,
    median_sales_price_dest: float,
    estimated_moving_costs: float,  # Average speed for cargo planes
) -> float:
    """
    Calculate relocation costs from a given location to new destination.  

    Args:
        median_sales_price_origin: sales price of current home
        median_sales_price_dest: sales price at new location or destination. 
        estimated_moving_costs: estimated moving costs for average sized house at median price

    Returns:
        float: The total relocation cost 

    Example:
        >>> # median sales price in San Francisco is $1,300,000, median sales price in Chapel Hill is $530,000,
        >>> estimated_moving_costs (full service) are $10,950, and payoff loan amount is $100,000
        >>> result = calculate_relocation_cost(1300000.00, 530000.00, 10950.00, 100000.000)
    """

    #additional parameters
    prep_cost = 10000.00
    percent_sale_comission = 0.05
    percent_closing_cost = 0.02
    payoff_loan_amount = 100000
    
    #calculate comissions
    sale_comission = percent_sale_comission * median_sales_price_origin
    closing_cost =  percent_closing_cost * median_sales_price_dest
    
    #net proceeds from sale of house
    net_proceeds = median_sales_price_origin - (sale_comission + prep_cost + payoff_loan_amount) 
    
    #remainder after purchase of new home
    sale_surplus = net_proceeds - (median_sales_price_dest + closing_cost) 

    #relocation cost 
    reloc_cost = estimated_moving_costs - sale_surplus
    return round(reloc_cost, 2)

#connect to hugging face
from huggingface_hub import login; login(os.environ['HF_TOKEN'])

model = HfApiModel(
    "Qwen/Qwen2.5-Coder-32B-Instruct", max_tokens=8096
) 

web_agent = ToolCallingAgent(
    model=model,
    tools=[
        DuckDuckGoSearchTool(),
        VisitWebpageTool(),
        calculate_relocation_costs,
    ],
    name="web_agent",
    description="Browses the web to find information",
    verbosity_level=0,
    max_steps=10,
)

from smolagents.utils import encode_image_base64, make_image_url
from smolagents import OpenAIServerModel
import os
from PIL import Image

def check_reasoning_and_plot(final_answer, agent_memory):
    final_answer
    multimodal_model = OpenAIServerModel("gpt-4o", max_tokens=8096)
    filepath = "saved_map.png"
    assert os.path.exists(filepath), "Make sure to save the plot under saved_map.png!"
    image = Image.open(filepath)
    prompt = (
        f"Here is a user-given task and the agent steps: {agent_memory.get_succinct_steps()}. Now here is the plot that was made."
        "Please check that the reasoning process and plot are correct: do they correctly answer the given task?"
        "First list reasons why yes/no, then write your final decision: PASS in caps lock if it is satisfactory, FAIL if it is not."
        "Don't be harsh: if the plot mostly solves the task, it should pass."
        "To pass, a plot should be made using px.scatter_map and not any other method (scatter_map looks nicer)."
    )
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt,
                },
                {
                    "type": "image_url",
                    "image_url": {"url": make_image_url(encode_image_base64(image))},
                },
            ],
        }
    ]
    output = multimodal_model(messages).content
    print("Feedback: ", output)
    if "FAIL" in output:
        raise Exception(output)
    return True


manager_agent = CodeAgent(
    #model=HfApiModel("deepseek-ai/DeepSeek-R1", max_tokens=8096),
    model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct", max_tokens=8096),
    tools=[calculate_relocation_costs],
    managed_agents=[web_agent],
    additional_authorized_imports=[
        "geopandas",
        "plotly",
        "shapely",
        "json",
        "pandas",
        "numpy",
    ],
    planning_interval=5,
    verbosity_level=2,
    final_answer_checks=[check_reasoning_and_plot],
    max_steps=15,
)

manager_agent.run("""
Find the ten best places to retire in the United States and calculate the relocation costs for Sonoma, CA, (38.2919° N, 122.4580° W).
Consider median sales prices for origin and destination locations, and average size houses for the median price in both locations when
determining estimated moving costs. Also, provide full-service moving costs only. 
Represent this as spatial map of the world, with the locations represented as scatter points with a color that depends on the relocation cost, 
and save it to saved_map.png!

Here's an example of how to plot and return a map:
import plotly.express as px
df = px.data.carshare()
fig = px.scatter_map(df, lat="centroid_lat", lon="centroid_lon", text="name", color="peak_hour", size=100,
     color_continuous_scale=px.colors.sequential.Magma, size_max=15, zoom=1)
fig.show()
fig.write_image("saved_image.png")
final_answer(fig)

Never try to process strings using code: when you have a string to read, just print it and you'll see it.
""")