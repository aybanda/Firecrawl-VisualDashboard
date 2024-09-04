# Web Content Visualization Dashboard

This Streamlit application provides an interactive dashboard for visualizing web content scraped using Firecrawl. Users can input a URL, scrape its content, and explore the data through various plots and statistical summaries.

## Features

- Web scraping using Firecrawl API
- Dataset overview with interactive table
- Dynamic histogram for selected features
- Correlation heatmap (when applicable)
- Basic statistics display
- User-selectable columns for visualization

## Installation

1. Clone this repository:

2. Create a virtual environment (optional but recommended):

   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
  
3. Install the required packages:

   pip install -r requirements.txt
   
5. Set up your Firecrawl API key:
   - Create a .env file in the project root
   - Add your Firecrawl API key to the .env file:
   
     FIRECRAWL_API_KEY=your_api_key_here
   

## Usage

Run the Streamlit app with:    

streamlit run app.py


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
