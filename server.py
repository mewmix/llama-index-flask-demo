from flask import Flask, render_template, request
import os
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, download_loader

os.environ["OPENAI_API_KEY"] = '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'


app = Flask(__name__)

# Define the TwitterTweetReader using the download_loader function
TwitterTweetReader = download_loader("TwitterTweetReader")

# Define a function to load the Twitter data using the TwitterTweetReader
def load_twitter_data(handles):
    # Replace 'YOUR_TOKEN' with your actual Twitter API bearer token
    loader = TwitterTweetReader(bearer_token="AAAAAAAAAAAAAAAAAAAAAPw%2FNAEAAAAAym1knneHc4gxDegizHHwyjzfggc%3DaQP4et1DilYTU6lJdU4AxsKA1Wr7FZuvcSkDiTH6m5WWxZHR1S")
    documents = loader.load_data(twitterhandles=handles)
    index = GPTSimpleVectorIndex(documents)
    return index

# Define the home page route
@app.route('/')
def home():
    return render_template('home.html')

# Define the results page route
@app.route('/results', methods=['POST'])
def results():
    # Get the list of Twitter handles from the form input
    handles = request.form.getlist('handles')
    # Get the search query from the form input
    query = request.form['query']
    # Load the Twitter data using the load_twitter_data function
    index = load_twitter_data(handles)
    # Perform the query on the index and extract the data
    results = index.query(query)
    # Render the results.html template with the search results
    return render_template('results.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
