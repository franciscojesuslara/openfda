import http.server
import socketserver
import json
import http.client

# -- IP and the port of the server
IP = "localhost"  # Localhost means "I": your local machine
PORT = 8000


# HTTPRequestHandler class
class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        list = []
        intro = "<!doctype html>" + "\n" + "<html>" + "\n" + "\t" + "<body>" + "\n" + "<ol>" + "\n"
        end = "<\ol>" + "\n" + "<body>" + "<html>"


        if self.path == "/":
            with open("search.html", "r") as f:
                message = f.read()
                self.wfile.write(bytes(message, "utf8"))

        elif "searchDrug" in self.path:
            self.send_response(200)
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            params = self.path.split("?")[1]
            drug = params.split("&")[0].split("=")[1]
            limit = params.split("&")[1].split("=")[1]
            url = "/drug/label.json?search=active_ingredient:" + drug + "&" + "limit=" + limit
            print(url)
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            drugs_raw = r1.read().decode("utf-8")
            conn.close()
            drugs = json.loads(drugs_raw)
            drugs_1 = str(drugs)
            self.wfile.write(bytes(drugs_1, "utf8"))

        elif "searchCompany" in self.path:
            self.send_response(200)
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            params = self.path.split("?")[1]
            company = params.split("&")[0].split("=")[1]
            limit = params.split("&")[1].split("=")[1]
            url = "/drug/label.json?search=brand_name:" + company + "&" + "limit=" + limit
            print(url)
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            companies_raw = r1.read().decode("utf-8")
            conn.close()
            companies = json.loads(companies_raw)
            companies_1 = str(companies)
            self.wfile.write(bytes(companies_1, "utf8"))
        elif "listDrug" in self.path:
            self.send_response(200)
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            params = self.path.split("?")[1]
            limit = params.split("=")[1]
            url = "/drug/label.json?" + "limit=" + limit
            print(url)
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            drugs_raw = r1.read().decode("utf-8")
            conn.close()
            drugs = json.loads(drugs_raw)

            for element in drugs["results"]:
                print(element['id'])
                list.append(element['id'])

            with open("listdrug.html", "w") as f:
                f.write(intro)
                for element in list:
                    element_1 = "<\t>" + "<li>" + element
                    f.write(element_1)
                f.write(end)

            with open("listdrug.html", "r") as f:
                file = f.read()

            self.wfile.write(bytes(file, "utf8"))

            web_contents = file
            web_headers = "HTTP/1.1 200"
            web_headers += "\n" + "Content-Type: text/html"
            web_headers += "\n" + "Content-Length: %i" % len(str.encode(web_contents))

        elif "listCompanies" in self.path:
            self.send_response(200)
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            params = self.path.split("?")[1]
            limit = params.split("=")[1]
            url = "/drug/label.json?" + "limit=" + limit
            print(url)
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            company_raw = r1.read().decode("utf-8")
            conn.close()
            company = json.loads(company_raw)

            for element in company["results"]:
                try:
                    element=element["openfda"]["manufacturer_name"][0]
                    list.append(element)
                except KeyError:
                    element= " Unknow"
                    list.append(element)

            with open("listcompanies.html", "w") as f:
                f.write(intro)
                for element in list:
                    element_1 = "<\t>" + "<li>" + element
                    f.write(element_1)
                f.write(end)

            with open("listcompanies.html", "r") as f:
                file = f.read()

            self.wfile.write(bytes(file, "utf8"))

            web_contents = file
            web_headers = "HTTP/1.1 200"
            web_headers += "\n" + "Content-Type: text/html"
            web_headers += "\n" + "Content-Length: %i" % len(str.encode(web_contents))


        elif "listWarnings" in self.path:
            self.send_response(200)
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            params = self.path.split("?")[1]
            limit = params.split("=")[1]
            url = "/drug/label.json?" + "limit=" + limit
            print(url)
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            warning_raw = r1.read().decode("utf-8")
            conn.close()
            warning = json.loads(warning_raw)

            for element in warning["results"]:
                try:
                    element = element["warnings"][0]
                    list.append(element)
                except KeyError:
                    element = "Unknow"
                    list.append(element)

            with open("listWarnings.html", "w") as f:
                f.write(intro)
                for element in list:
                    element_1 = "<\t>" + "<li>" + element
                    f.write(element_1)
                f.write(end)

            with open("listWarnings.html", "r") as f:
                 file = f.read()

            self.wfile.write(bytes(file, "utf8"))

            web_contents = file
            web_headers = "HTTP/1.1 200"
            web_headers += "\n" + "Content-Type: text/html"
            web_headers += "\n" + "Content-Length: %i" % len(str.encode(web_contents))
        else:
            with open("Error.html", "w") as f:
                self.send_response(404)
                f.write(intro)
                element="The HTML requested is not supported"
                f.write(element)
                f.write(end)
            with open("Error.html", "r") as f:
                file = f.read()

            self.wfile.write(bytes(file, "utf8"))

            web_contents = file
            web_headers = "HTTP/1.1 200"
            web_headers += "\n" + "Content-Type: text/html"
            web_headers += "\n" + "Content-Length: %i" % len(str.encode(web_contents))

# Handler = http.server.SimpleHTTPRequestHandler
Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer((IP, PORT), Handler)
print("serving at port", PORT)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
        pass

httpd.server_close()
print("")
print("Server stopped!")

