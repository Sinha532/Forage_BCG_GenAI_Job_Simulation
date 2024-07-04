# Forage BCG GenAI JOB SIMULATION

## This github contains the task of BCG job simulation powered by Forage. 
The first task in this simulation is regarding the data extraction task which is manual task form the 10-Q and 10-K reports from EDGAR. After the collection taks we have to perform the financial analysis on the collected data, which should inulcates answers of all the questions regarding the financial report of the collected data.

The Second task contains of builiding a simple rule based chatbot , which should take answers from the customers and answer their queries by traversing through our collected dataset.

# Task 1: Data Extraction and Analysis
This project performs a financial analysis of three major tech companies: Apple, Microsoft, and Tesla. Using the provided financial data, we calculate year-over-year growth rates for key metrics and analyze trends in profitability, assets, and liabilities.

### Data
The dataset contains financial information for the years 2021, 2022, and 2023, including:

- Total Revenue
- Net Income
- Total Assets
- Total Liabilities
- Cash Flow from Operating Activities

### Metrics Calculated

For each company, we calculated the following growth metrics and profitability ratios:
- Revenue Growth (%)
- Net Income Growth (%)
- Assets Growth (%)
- Liabilities Growth (%)
- Cash Flow Growth (%)
- Profit Margin
- Return on Assets (ROA)
- Return on Equity (ROE)

### Tools Used
- Pandas: For data manipulation and calculation of growth metrics.
- Matplotlib & Seaborn: For data visualization.

# Task 2: Developing an AI Driven Financial ChatBot Prototype

## Overview
This project demonstrates the development of a simple rule-based chatbot using Python and Flask. The chatbot provides predefined responses to specific user inputs, showcasing the basics of conversational AI. The project is structured to be easily understandable and extendable.

## Features
- **Rule-Based Responses:** The chatbot responds to user inputs based on predefined rules.
- **Flask Web Server:** The chatbot is served via a Flask web application.
- **Interactive UI:** The chat interface is user-friendly and styled with CSS.
- **Real-Time Communication:** The chatbot provides real-time responses to user queries.

## Project Structure
The project is organized into the following parts:

1. **Backend Development:**
   - **Flask Setup:** We set up a Flask web server to handle HTTP requests and serve the chatbot interface.
   - **Rule-Based Logic:** We implemented a basic rule-based logic in Python to generate responses based on user inputs.

2. **Frontend Development:**
   - **HTML Interface:** We created a simple HTML page to serve as the chat interface.
   - **CSS Styling:** We added CSS styles to enhance the visual appeal and usability of the chat interface.
   - **JavaScript:** We used JavaScript to handle user input, send it to the Flask server, and display responses.

3. **Integration:**
   - **Connecting Frontend and Backend:** We integrated the HTML frontend with the Flask backend to enable communication between the user and the chatbot.
   - **Deployment:** We deployed the Flask application to a local server for testing and demonstration.


## Conclusion
This project serves as a foundational example of building a rule-based chatbot with Flask. It provides a stepping stone for developing more complex conversational agents using advanced NLP techniques.

---

Feel free to reach out if you have any questions or need further assistance with the project. Happy coding!

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

