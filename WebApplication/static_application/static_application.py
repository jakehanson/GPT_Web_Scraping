import pandas as pd
from flask import Flask, render_template

application = Flask(__name__)

# Load the dataframe
df = pd.read_csv('gpt_results_clean.csv')

@application.route('/')
def index():
    # Convert the DataFrame to HTML with Bootstrap classes
    data = df.to_html(classes='table table-hover table-striped', border=0, index=False, table_id="dataTable")

    # Render the HTML template and pass the data
    html_content = render_template('index.html', data=data)

    # Save the rendered HTML to a file
    with open("output/index.html", "w") as file:
        file.write(html_content)
    
    # Return the content (optional, for testing)
    return html_content

if __name__ == '__main__':
    # Generate the static HTML file
    with application.test_request_context('/'):
        index()