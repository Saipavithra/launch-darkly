# launch-darkly
This is a hello-world demo app built using python and python flask framework.
This integration used Launch Darkly's Python Server Side SDK.

**Pre-requisites**:

A hello-world feature flag is created via the launch-darkly portal with strings as flag variations, and values "world"/"ld".
Flags are configured to return "world" when targetting is enabled.

**Python App**:

The flask app registers itself with the launch-darkly sdk using production keys and calls the ld_client.variation() function to get values configured for the feature flag. Using the if condition, the application validates the value and makes decision based on it.

**Example**:

Option 1: If the variation returns "world", the user accessing the site would see "Hello, World!"
Option 2: If the variation returns "ld", the user accessing the site would see "Hello, Launch Darkly!"

**Execute Flask App**

Install Python Flask using pip3 install flask

Run the app using

export FLASK_APP=hello-launch.py
flask run --host 0.0.0.0
