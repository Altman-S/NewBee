# TTDS Movie Search IR Project 2022
This is a group project for the course [TTDS](https://www.inf.ed.ac.uk/teaching/courses/tts/) (Text Technologies for Data Science) at the University of Edinburgh. 

The title of our project: **Movie-In-One (MIO) Search Engine**

Currently it can be accessed from this link: [http://www.newbee123.xyz](http://www.newbee123.xyz)

## Summary

The project consists of 4 basic parts:

+ Data_Collection: crawl data from web page
+ ir_eval: IR indexing and ranking
+ GUI: built with Vue
+ API: built with Flask

## Setting up

### Clone the Repository
```js
git clone git@github.com:Altman-S/NewBee.git
cd NewBee
```

### Python Environment
```js
python3 -m venv py3ttds
source py3ttds/bin/activate
pip install -r requirement.txt
```

### Run the frontend
```js
cd client
npm run serve
```

### Run the backend
```js
python3 run.py
```




