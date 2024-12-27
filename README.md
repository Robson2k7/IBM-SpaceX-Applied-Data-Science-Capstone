![image](https://github.com/user-attachments/assets/0f57b3a2-7f91-445d-ac88-5e54a81b187a)

Project background and context

SpaceX is a leader in the space industry, known for groundbreaking achievements such as the first successful recovery of a rocket from low Earth orbit by a private company in December 2010. One of the key elements of SpaceX's strategy is to reuse rockets through safe first stage landings, significantly reducing launch costs.
The standard launch cost of a Falcon 9 rocket is $62 million, which is significantly cheaper compared to offerings from other companies (whose costs can exceed $165 million). The big savings come from rocket reusability, but this depends on the success of the first stage landing.

Therefore, the goal of the project is to analyze the factors affecting landing success and develop predictive models. Successful prediction of landing results can be valuable both to SpaceX and to competing companies considering entering the space market. The analysis includes aspects such as payload mass, launch site location, orbit type and the use of advanced analytical methods such as classification models.

Methodology - Executive Summary:

•	Data collection methodology:
Data was collected by using request to the SpaceX API and by using web scraping from Wikipedia 

•	Perform data wrangling:
Data was filtered to only include Falcon 9 launches. Missing values was replaced by mean. One-hot encoding was used for categorical data. 

•	Perform exploratory data analysis (EDA) using visualization and SQL

•	Perform interactive visual analytics using Folium and Plotly Dash

•	Perform predictive analysis using classification models:
Developed classification models, performed hyperparameter tuning using Grid Search, and evaluated their performance using metrics such as accuracy.

Robson2k7
11.11.2024


-----------------------------------------------------------------------------------------------------------------------------------------------------

Opis projektu:

SpaceX jest liderem w branży kosmicznej, znanym z przełomowych osiągnięć, takich jak pierwsze udane odzyskanie rakiety z niskiej orbity okołoziemskiej przez prywatną firmę w grudniu 2010 roku. Jednym z kluczowych elementów strategii SpaceX jest ponowne wykorzystanie rakiet poprzez bezpieczne lądowanie na pierwszym stopniu, co znacznie obniża koszty startu.
Standardowy koszt startu rakiety Falcon 9 wynosi 62 mln USD, co jest znacznie niższą ceną w porównaniu do ofert innych firm (których koszty mogą przekraczać 165 mln USD). Duże oszczędności wynikają z możliwości ponownego użycia rakiety, ale zależy to od powodzenia lądowania pierwszego stopnia.

Dlatego celem projektu jest analiza czynników wpływających na powodzenie lądowania i opracowanie modeli predykcyjnych. Skuteczne przewidywanie wyników lądowania może być cenne zarówno dla SpaceX, jak i dla konkurencyjnych firm rozważających wejście na rynek kosmiczny. Analiza obejmuje takie aspekty jak masa ładunku, lokalizacja miejsca startu, typ orbity oraz wykorzystanie zaawansowanych metod analitycznych, takich jak modele klasyfikacyjne.

Metodologia - streszczenie:

- Metodologia zbierania danych:
Dane zostały zebrane za pomocą zapytania do interfejsu API SpaceX oraz za pomocą web scrapingu stron internetowych z Wikipedii. 

- Analiza danych:
Dane zostały przefiltrowane tak, aby obejmowały tylko starty Falcona 9. Brakujące wartości zastąpiono średnią. W przypadku danych kategorycznych zastosowano kodowanie one-hot. 

- Przeprowadzenie eksploracyjnej analizy danych (EDA) przy użyciu wizualizacji i SQL.

- Wykonywanie interaktywnych analiz wizualnych przy użyciu Folium i Plotly Dash

- Przeprowadzanie analizy predykcyjnej przy użyciu modeli klasyfikacji:
Opracowano modele klasyfikacji, przeprowadzono strojenie hiperparametrów przy użyciu wyszukiwania siatki i oceniono ich wydajność przy użyciu wskaźników, takich jak dokładność.

Robson2k7
11.11.2024
