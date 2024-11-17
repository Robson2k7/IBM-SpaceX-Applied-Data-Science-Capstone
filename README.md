![image](https://github.com/user-attachments/assets/0f57b3a2-7f91-445d-ac88-5e54a81b187a)

Project background and context

SpaceX is a leader in the space industry, known for groundbreaking achievements such as the first successful recovery of a rocket from low Earth orbit by a private company in December 2010. One of the key elements of SpaceX's strategy is to reuse rockets through safe first stage landings, significantly reducing launch costs.
The standard launch cost of a Falcon 9 rocket is $62 million, which is significantly cheaper compared to offerings from other companies (whose costs can exceed $165 million). The big savings come from rocket reusability, but this depends on the success of the first stage landing.

Therefore, the goal of the project is to analyze the factors affecting landing success and develop predictive models. Successful prediction of landing results can be valuable both to SpaceX and to competing companies considering entering the space market. The analysis includes aspects such as payload mass, launch site location, orbit type and the use of advanced analytical methods such as classification models.

Methodology - Executive Summary:

•	Data collection methodology:
Data was collected by using request to the SpaceX API and by using web scraping from Wikipedia 

•	Perform data wrangling
Data was filtered to only include Falcon 9 launches. Missing values was replaced by mean. One-hot encoding was used for categorical data. 

•	Perform exploratory data analysis (EDA) using visualization and SQL

•	Perform interactive visual analytics using Folium and Plotly Dash

•	Perform predictive analysis using classification models
Developed classification models, performed hyperparameter tuning using Grid Search, and evaluated their performance using metrics such as accuracy.

Robson2k7
11.11.2024
