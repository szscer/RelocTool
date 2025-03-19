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

# Given data                                                                                                                                                                
locations = ["Miami, FL", "Orlando, FL", "Tampa, FL", "Fort Lauderdale, FL", "Sarasota, FL", "Cape Coral, FL", "Charleston, SC", "Albuquerque, NM", "Madison, WI",          
"Durham, NC"]                                                                                                                                                               
origin = "Sonoma, CA"                                                                                                                                                       
                                                                                                                                                                            
# Median sales prices                                                                                                                                                       
median_sales_prices = {                                                                                                                                                     
    "Sonoma, CA": (857000 + 927500 + 767000 + 1027917) / 4,                                                                                                                 
    "Miami, FL": (593833 + 628000 + 440000) / 3,                                                                                                                            
    "Orlando, FL": (372800 + 425000) / 2,                                                                                                                                   
    "Tampa, FL": (418967 + 429661 + 461000) / 3,                                                                                                                            
    "Fort Lauderdale, FL": (610500 + 480983 + 599887) / 3,                                                                                                                  
    "Sarasota, FL": (569500 + 489738 + 462000) / 3,                                                                                                                         
    "Cape Coral, FL": (349738 + 355133 + 395000) / 3,                                                                                                                       
    "Charleston, SC": (673000 + 593000 + 425000) / 3,                                                                                                                       
    "Albuquerque, NM": (347029 + 349921) / 2,                                                                                                                               
    "Madison, WI": (439000 + 405222) / 2,                                                                                                                                   
    "Durham, NC": (515000 + 512500) / 2                                                                                                                                     
}                                                                                                                                                                           
                                                                                                                                                                            
# Average house sizes                                                                                                                                                       
average_house_sizes = {                                                                                                                                                     
    "Sonoma, CA": (2200 + 2400) / 2,                                                                                                                                        
    "Miami, FL": (1400 + 1600) / 2,                                                                                                                                         
    "Orlando, FL": (1700 + 1800) / 2,                                                                                                                                       
    "Tampa, FL": (1800 + 2000) / 2,                                                                                                                                         
    "Fort Lauderdale, FL": (1700 + 1900) / 2,                                                                                                                               
    "Sarasota, FL": (1900 + 2100) / 2,                                                                                                                                      
    "Cape Coral, FL": (1500 + 1700) / 2,                                                                                                                                    
    "Charleston, SC": (2200 + 2400) / 2,                                                                                                                                    
    "Albuquerque, NM": (1600 + 1700) / 2,                                                                                                                                   
    "Madison, WI": (2000 + 2200) / 2,                                                                                                                                       
    "Durham, NC": (1800 + 2000) / 2                                                                                                                                         
}                                                                                                                                                                           
                                                                                                                                                                            
# Full-service moving costs (estimates from observations)                                                                                                                   
moving_costs = {                                                                                                                                                            
    "Miami, FL": (3220 + 7700) / 2,                                                                                                                                         
    "Orlando, FL": (2580 + 6000) / 2,                                                                                                                                       
    "Tampa, FL": (2510 + 5700) / 2,                                                                                                                                         
    "Fort Lauderdale, FL": (2580 + 6000) / 2,                                                                                                                               
    "Sarasota, FL": (2520 + 5700) / 2,                                                                                                                                      
    "Cape Coral, FL": (2630 + 5900) / 2,                                                                                                                                    
    "Charleston, SC": (2490 + 5500) / 2,                                                                                                                                    
    "Albuquerque, NM": (2310 + 5100) / 2,                                                                                                                                   
    "Madison, WI": (2680 + 6000) / 2,                                                                                                                                       
    "Durham, NC": (2640 + 5800) / 2                                                                                                                                         
}                                                                                                                                                                           
                                                                                                                                                                            
# Coordinates                                                                                                                                                               
coordinates = {                                                                                                                                                             
    "Sonoma, CA": (38.29186, -122.45804),                                                                                                                                   
    "Miami, FL": (25.77427, -80.19366),                                                                                                                                     
    "Orlando, FL": (28.53834, -81.37924),                                                                                                                                   
    "Tampa, FL": (27.94752, -82.45843),                                                                                                                                     
    "Fort Lauderdale, FL": (26.12231, -80.14338),                                                                                                                           
    "Sarasota, FL": (27.33643, -82.53065),                                                                                                                                  
    "Cape Coral, FL": (26.56290, -81.94953),                                                                                                                                
    "Charleston, SC": (32.77657, -79.93092),                                                                                                                                
    "Albuquerque, NM": (35.08449, -106.65114),                                                                                                                              
    "Madison, WI": (43.07305, -89.40123),                                                                                                                                   
    "Durham, NC": (35.99776, -78.90366)                                                                                                                                     
}                                                                                                                                                                           
                                                                                                                                                                            
# Calculate relocation costs                                                                                                                                                
relocation_costs = {}                                                                                                                                                       
for location in locations:                                                                                                                                                  
    origin_median_price = median_sales_prices[origin]                                                                                                                       
    origin_house_size = average_house_sizes[origin]                                                                                                                         
    dest_median_price = median_sales_prices[location]                                                                                                                       
    dest_house_size = average_house_sizes[location]                                                                                                                         
    move_cost = moving_costs[location]                                                                                                                                      
                                                                                                                                                                            
    relocation_cost = calculate_relocation_costs(                                                                                                                           
        median_sales_price_origin=origin_median_price,                                                                                                                      
        median_sales_price_dest=dest_median_price,                                                                                                                          
        estimated_moving_costs=move_cost                                                                                                                                    
    )                                                                                                                                                                       
    relocation_costs[location] = relocation_cost                                                                                                                            
                                                                                                                                                                            
# Create a data frame for plotting                                                                                                                                          
import pandas as pd                                                                                                                                                         
                                                                                                                                                                            
data = {                                                                                                                                                                    
    "name": ["Sonoma, CA"] + locations,                                                                                                                                     
    "centroid_lat": [coordinates["Sonoma, CA"][0]] + [coordinates[loc][0] for loc in locations],                                                                            
    "centroid_lon": [coordinates["Sonoma, CA"][1]] + [coordinates[loc][1] for loc in locations],                                                                            
    "relocation_cost": [0] + [relocation_costs[loc] for loc in locations]                                                                                                   
}                                                                                                                                                                           
                                                                                                                                                                            
df = pd.DataFrame(data)                                                                                                                                                     
                                                                                                                                                                            
# Generate the map                                                                                                                                                          
import plotly.express as px                                                                                                                                                 
                                                                                                                                                                            
fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", text="name", color="relocation_cost",                                                                   
                        color_continuous_scale=px.colors.sequential.Magma, size_max=15, zoom=2, mapbox_style="carto-positron")                                              
                                                                                                                                                                            
fig.show()                                                                                                                                                                  
fig.write_image("saved_map_test.png")                                                                                                                                            
                                                                                                                                                                            
# Provide the final answer                                                                                                                                                  
#final_answer(fig)
print(df.sort_values(by=["relocation_cost"], ascending=False))