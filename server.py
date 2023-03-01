from flask import Flask, render_template, request
import os
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, download_loader
import docx2txt

os.environ["OPENAI_API_KEY"] = 'your key here'


app = Flask(__name__)

# Define the TwitterTweetReader using the download_loader function
TwitterTweetReader = download_loader("TwitterTweetReader")

# Define a function to load the Twitter data using the TwitterTweetReader
def load_twitter_data(handles):
    # Replace 'YOUR_TOKEN' with your actual Twitter API bearer token
    loader = TwitterTweetReader(bearer_token="your key here")
    documents = loader.load_data(twitterhandles=handles)
    index = GPTSimpleVectorIndex(documents)
    return index


def load_folder():
    documents = SimpleDirectoryReader('data').load_data()
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

# Define the folder results page route


@app.route('/folder_results', methods=['POST'])
def folder_results():
    # Get the list of Twitter handles from the form input
    # Get the search query from the form input
    query = request.form['folder_query']
    # Load the Twitter data using the load_twitter_data function
    index = load_folder()
    # Perform the query on the index and extract the data
    results = index.query(query)
    # Render the results.html template with the search results
    return render_template('folder_results.html', results=results)


## Define an upload route for the /data/ folder to upload files
@app.route('/upload', methods=['POST'])
def upload():
    # Get the file from the form input
    file = request.files['file']
    # Save the file to the data folder
    file.save(os.path.join('data', file.filename))

    index = load_folder()


    ## Run the query on the uploaded file
    # Get the search query from the form input
    query = request.form['folder_query']
    ## Perform the query on the index and extract the data
    results = index.query(query)

    # Redirect to the folder_results page
    return render_template('folder_results.html', results=results)




if __name__ == '__main__':
    app.run(debug=True)
