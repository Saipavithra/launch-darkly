from flask import Flask

#ld import and initialization

import ldclient
from ldclient.config import Config

ldclient.set_config(Config("sdk-6f69d5f7-f5b7-4743-8a6e-55c272184ae0"))
ld_client = ldclient.get()
#print(ld_client)

#flask app
app = Flask(__name__)

# Everything below this line is part of the example app.
@app.route('/')
def hello_world():
    show_feature = ld_client.variation("hello-world", {"key": "hello-world"}, "master")
    print(show_feature)
    if show_feature == "ld":
        return 'Hello, Launch Darkly!'
    else:
      return 'Hello World!'
