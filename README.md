# Yet Another CURL

## About The Project

This is a CLI app that connects via socket to a web server using port 80, and retrieves the defined asset

### Usage
1. Set up a python virtual enviroment
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```
2. Install project Dependencies
    ```sh
    pip install -r requirements.txt
    ```
2. Run ycurl (see example)
    ```sh
    python ycurl.py www.columbia.edu /~fdc/sample.html
    ```
You are ready to go.
You can run `--help` tag to find more about the app

Usage: ycurl.py [OPTIONS] `HOST` `ASSET` `[PORT]`
Arguments:
- HOST: Target URL to make the request  [required] ex: www.columbia.edu
- ASSET: Path inside server to find the asset  [required] ex: /~fdc/picture-of-something.jpg
- [PORT]: Port in which the request is made  [default: 80]

### References
- https://realpython.com/python-sockets/
- https://docs.python.org/3/howto/sockets.html
- https://www.geeksforgeeks.org/socket-programming-python/
- https://typer.tiangolo.com/
- https://stackabuse.com/guide-to-parsing-html-with-beautifulsoup-in-python/
