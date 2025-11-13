from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
application = app

@app.route('/')
def index():
    try:

        df = pd.read_excel('./CamFruitWebsite.xlsx', sheet_name='Sheet1') 
        
        # Convert the DataFrame to an HTML table
        html_table = df.to_html(classes='table table-striped', index=False) 
        # 'classes' adds Bootstrap styling; 'index=False' prevents pandas from including the DataFrame index
        
        return render_template('index.html', table=html_table)
    except FileNotFoundError:
        return "Error: Excel file not found. Please check the file path."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True, port=8000)