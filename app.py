#!/usr/bin/env python
# coding: utf-8

# In[16]:


from flask import Flask, request, render_template


# In[18]:


#!pip install textblob


# In[19]:


from textblob import TextBlob


# In[26]:


app = Flask(__name__)


# In[27]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", result = r))
    else:
        return(render_template("index.html", result = "2"))


# In[28]:


if __name__ == "__main__":
    app.run()


# In[ ]:




