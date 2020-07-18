# Instant JSON API

Create instant API endpoints for your JSON files.

Simply place your JSON files in the folder and run `python app.py`. The default port is `9001` but you can change it by passing a port number on run, ie `python app.py port=8000`.

API endpoint: `localhost:9001/api/<filename>`

# Use Case

Save time when working on personal projects to generate an API without having to set up a back end or database. Just write a JSON file instead.

# Caveats

If you decide to add additional JSON files to the folder, you will need to rerun the server.

Additionally, only `GET` requests are supported.

# Requirements

Currently works with Python 2 and 3, and only requires Flask.

