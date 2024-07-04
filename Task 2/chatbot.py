import pandas as pd
import re
final_report = pd.read_csv('final_report.csv')
summary_report = pd.read_csv('summary.csv')

def extract_info(user_query):
    # Regular expression to extract the company name and fiscal year
    company_pattern = r'\b(Apple|Microsoft|Tesla)\b'
    year_pattern = r'\b(2021|2022|2023)\b'
    
    company_match = re.search(company_pattern, user_query, re.IGNORECASE)
    year_match = re.search(year_pattern, user_query)
    
    company = company_match.group(0).capitalize() if company_match else None
    fiscal_year = int(year_match.group(0)) if year_match else None
    
    return company, fiscal_year

def financial_chatbot(user_query):
    company_input, fiscal_year = extract_info(user_query)
    
    if not company_input:
        return "Please provide a valid company name (Apple, Microsoft, Tesla)."
    
    if fiscal_year and "cash flow from operations growth" in user_query:
        try:
            cash_ops_growth = final_report[(final_report['Year'] == fiscal_year) & 
                                           (final_report['Company'].str.lower() == company_input.lower())]['CashFlow Growth(%)'].values[0]
            return f"The Cash Flow from Operations Growth(%) for {company_input} in {fiscal_year} is {cash_ops_growth:.4f}%"
        except IndexError:
            return "Sorry, the data for the specified query is not available."
    elif "cash flow from operations growth" in user_query:
        try:
            cash_growth=summary_report[summary_report['Company'].str.lower()== company_input.lower()]['CashFlow Growth(%)'].values[0]
        except IndexError:
            return "Sorry, the data for the specified query is not available."

    elif "year by year average revenue growth rate" in user_query:
        try:
            year_avg_revenue_growth = summary_report[summary_report['Company'].str.lower() == company_input.lower()]['Revenue Growth(%)'].values[0]
            return f"The Year by Year Average Revenue Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_revenue_growth:.4f}%"
        except IndexError:
            return "Sorry, the data for the specified query is not available."
        
    elif fiscal_year and "year by year average revenue growth rate" in user_query:
        try:
            cash_ops_growth = final_report[(final_report['Year'] == fiscal_year) & 
                                           (final_report['Company'].str.lower() == company_input.lower())]['Revenue Growth(%)'].values[0]
            return f"The Cash Flow from Operations Growth(%) for {company_input} in {fiscal_year} is {cash_ops_growth:.4f}%"
        except IndexError:
            return "Sorry, the data for the specified query is not available."
    
    elif fiscal_year and "net income" in user_query:
        try:
            net_income = final_report[(final_report['Year'] == fiscal_year) & 
                                           (final_report['Company'].str.lower() == company_input.lower())]['Net Income'].values[0]
            return f"The Cash Flow from Operations Growth(%) for {company_input} in {fiscal_year} is {net_income:.4f}%"
        except IndexError:
            return "Sorry, the data for the specified query is not available."
        

    elif "year by year average net income growth rate" in user_query:
        try:
            year_avg_net_income_growth = summary_report[summary_report['Company'].str.lower() == company_input.lower()]['Net Income Growth(%)'].values[0]
            return f"The Year by Year Average Net Income Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_net_income_growth:.4f}%"
        except IndexError:
            return "Sorry, the data for the specified query is not available."
        
    elif "assets growth" in user_query:
        try:
            asset_growth=summary_report[summary_report['Company'].str.lower()== company_input.lower()]['Assets Growth(%)'].values[0]
            return f"The Year by Year Average Assets Growth Rate(%) from 2021 to 2023 for {company_input} is {asset_growth:.4f}%"
        except IndexError:
            return "Sorry, the data for the specified query is not available."
    
    elif fiscal_year and "assets growth" in user_query:
        try:
            asset_growth = final_report[(final_report['Year'] == fiscal_year) & 
                                           (final_report['Company'].str.lower() == company_input.lower())]['Assets Growth(%)'].values[0]
            return f"The assets growth for {company_input} in {fiscal_year} is {asset_growth:.4f}%"
        except IndexError:
            return "Sorry, the data for the specified query is not available."
        
    elif "total revenue" in user_query:
        try:
            value=summary_report[summary_report['Company'].str.lower()== company_input.lower()]['Total Revenue'].values[0]
            return f"The Year by Year Average total revenue from 2021 to 2023 for {company_input} is {value:.4f}%"
        except IndexError:
            return "Sorry, the data for the specified query is not available."
    
    elif fiscal_year and "total revenue" in user_query:
        try:
            value = final_report[(final_report['Year'] == fiscal_year) & 
                                           (final_report['Company'].str.lower() == company_input.lower())]['Total Revenue'].values[0]
            return f"The sum of total revenue for {company_input} in {fiscal_year} is {value:.4f}%"
        except IndexError:
            return "Sorry, the data for the specified query is not available."
        
    elif "total liabilities" in user_query:
        try:
            value=summary_report[summary_report['Company'].str.lower()== company_input.lower()]['Total Liabilities'].values[0]
            return f"The Year by Year Average total liabilities from 2021 to 2023 for {company_input} is {value:.4f}%"
        except IndexError:
            return "Sorry, the data for the specified query is not available."
    
    elif fiscal_year and "total liabilities" in user_query:
        try:
            value = final_report[(final_report['Year'] == fiscal_year) & 
                                           (final_report['Company'].str.lower() == company_input.lower())]['Total Liabilities'].values[0]
            return f"The sum of total liabilities for {company_input} in {fiscal_year} is {value:.4f}%"
        except IndexError:
            return "Sorry, the data for the specified query is not available."

    else:
        return "Sorry, I can only provide information on the requested query."
