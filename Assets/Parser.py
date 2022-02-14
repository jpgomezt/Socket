from bs4 import BeautifulSoup

def parse_http_response(response):
    httppp_header = {}
    count = 0
    current_header = 'Status'
    read_value = ''
    reading_header_value = False
    while count < len(response):
        if(response[count] == 58 and not(reading_header_value)):
            current_header = read_value
            reading_header_value = True
            read_value = ''
            count += 1
        elif((response[count] == 13) and (response[count+1] == 10)):
            httppp_header[current_header] = read_value
            if((response[count+2] == 13) and (response[count+3] == 10)):
                count += 4
                break
            reading_header_value = False
            read_value = ''
            count += 1
        else:
            read_value = read_value + chr(response[count])
        count += 1
    http_body = response[count:len(response)]
    return httppp_header, http_body

def parse_html(html_body):
    beautifulsoup_parser = BeautifulSoup(html_body, 'html.parser')
    images = beautifulsoup_parser.find_all("img")
    links = beautifulsoup_parser.find_all("link")
    scrpits = beautifulsoup_parser.find_all("script")
    return images, links, scrpits

