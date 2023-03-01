# Requires OpenAI API Key & Twitter Developer Key (Bearer Token)


### Notes
Implementing https://github.com/jerryjliu/gpt_index and their connectors (in this example twitter from https://github.com/emptycrown/llama-hub/tree/main/loader_hub/twitter in a flask application for prototyping and demo. Needs more work for additional prompt saving. Credit to https://github.com/jdan/98.css for the CSS.



## install

```
git clone https://github.com/mewmix/llama-index-flask-demo && cd llama-index-flask-demo


pip install -r requirements.txt

```

## edit the server.py file with your keys and then run.


```
python3 server.py

```

### Go to  browser
```
http://127.0.0.1:5000/

```



### Screenshots
<img width="499" alt="Screen Shot 2023-02-28 at 9 11 45 PM" src="https://user-images.githubusercontent.com/42463809/222051370-8a1d08d5-7212-4395-ad2d-b214b1e7a952.png">
<img width="494" alt="Screen Shot 2023-02-28 at 9 14 22 PM" src="https://user-images.githubusercontent.com/42463809/222051368-df2a38c1-fdef-447a-9b61-4b6c189c68a5.png">
<img width="498" alt="Screen Shot 2023-02-28 at 9 17 05 PM" src="https://user-images.githubusercontent.com/42463809/222051575-646b6cb4-a527-4b10-9910-df9759d04dc8.png">


### example prompt

```
What would be a trendy summary tweet based on this user? 

```


### File upload requires data (supporting docx) in the /data/ folder
# llama-index-flask-demo
