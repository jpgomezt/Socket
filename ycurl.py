import typer
from Assets.Socket import Socket
import Assets.Parser as parser

def main(host: str = typer.Argument(..., help="Target URL to make the request"), asset: str = typer.Argument(..., help="Path inside server to find the asset"), port: int = typer.Argument(80, help="Port in which the request is made")):
    """
    Connect to a URL using HOST, asking for an ASSET and saving it locally
    """
    try:
        page_name = host.split('.')[1]
        my_socket = Socket()
        my_socket.connect(host, port)
        http_response = my_socket.send_request(asset)
        http_header, http_body = parser.parse_http_response(http_response)
        if(http_header['Status'] != 'HTTP/1.1 200 OK'):
            typer.echo('Error: ' + http_header['Status'])
            raise typer.Exit()
        typer.echo(http_header['Status'])
        content_type, subtype = http_header['Content-Type'].split('/')
        subtype = subtype.split(';')[0]
        if(subtype == 'html'):
            images, links, scripts = parser.parse_html(http_body.decode())
            typer.echo('\n\rEncountered '+ str(len(images)) + ' <img> tags:')
            for image in images:
                typer.echo(image['src'])
            typer.echo('\n\rEncountered '+ str(len(links)) + ' <link> tags:')
            for link in links:
                typer.echo(link['href'])
            typer.echo('\n\rEncountered '+ str(len(scripts)) + ' <script> tags:')
            for script in scripts:
                typer.echo(script['src'])
        doc_name = page_name + '.' + subtype
        file = open(doc_name, 'wb')
        file.write(http_body)
        file.close()
        typer.echo('Document was saved under name: ' + doc_name)
    except Exception as exception:
        raise typer.Exit(exception)

if __name__ == "__main__":
    typer.run(main)