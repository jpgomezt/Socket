import typer
from Socket import Socket
import Parser as parser

def main(host: str = typer.Argument(..., help="Target URL to make the request"), port: int = typer.Argument(80, help="Port in which the request is made"), asset: str = typer.Argument(..., help="Path inside server to find the asset")):
    my_socket = Socket()
    my_socket.connect(host, port)
    http_response = my_socket.send_request(asset)
    http_header, http_body = parser.parse_http_response(http_response)
    content_type, subtype = http_header['Content-Type'].split('/')
    if(http_header['Status'] != 'HTTP/1.1 200 OK'):
        typer.echo('Error: ' + http_header['Status'])
        raise typer.Exit()
    f = open('test.' + subtype, 'wb')
    f.write(http_body)
    f.close()

if __name__ == "__main__":
    typer.run(main)

#www-net.cs.umass.edu/wireshark-labs/Wireshark_HTTP_v8.0.pdf
#www.columbia.edu/~fdc/sample.html
#python ycurl.py www.columbia.edu 80 /~fdc/sample.html
#www.columbia.edu/~fdc/picture-of-something.jpg
#python ycurl.py www.columbia.edu 80 /~fdc/picture-of-something.jpg