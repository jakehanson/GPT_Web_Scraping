import pandas as pd
from flask import Flask, render_template

application = Flask(__name__)

## Load dataframe
df = pd.read_csv('gpt_results_clean.csv')

@application.route('/')
def index():
    # Convert your DataFrame to HTML with Bootstrap classes
    data = df.to_html(classes='table table-hover table-striped', border=0, index=False, table_id="dataTable")

    # Pass the data to your HTML template
    return render_template('index.html', data=data)

if __name__ == '__main__':
    application.run(debug=False)