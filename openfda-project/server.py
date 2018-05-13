import http.server
import socketserver
import json
import http.client

# -- IP and the port of the server
IP = "localhost"  # Localhost means "I": your local machine
PORT = 8000
socketserver.TCPServer.allow_reuse_address = True


class OpenFDAClient():

    def active_component(self,drug,limit):
        headers = {'User-Agent': 'http-client'}
        conn = http.client.HTTPSConnection("api.fda.gov")
        url = "/drug/label.json?search=active_ingredient:" + drug + "&" + "limit=" + limit
        print(url)
        conn.request("GET", url, None, headers)
        r1 = conn.getresponse()
        drugs_raw = r1.read().decode("utf-8")
        conn.close()
        drugs = json.loads(drugs_raw)
        drugs_1 = drugs
        return drugs_1

    def company(self,drug,limit):
        conn = http.client.HTTPSConnection("api.fda.gov")
        headers = {'User-Agent': 'http-client'}
        url = "/drug/label.json?search=brand_name:" + drug + "&" + "limit=" + limit
        print(url)
        conn.request("GET", url, None, headers)
        r1 = conn.getresponse()
        drugs_raw = r1.read().decode("utf-8")
        conn.close()
        drugs = json.loads(drugs_raw)
        drugs_1 = drugs
        return drugs_1


    def list(self,drug,limit):
        headers = {'User-Agent': 'http-client'}
        conn = http.client.HTTPSConnection("api.fda.gov")
        url = "/drug/label.json?" + "limit=" + limit
        print(url)
        conn.request("GET", url, None, headers)
        r1 = conn.getresponse()
        drugs_raw = r1.read().decode("utf-8")
        conn.close()
        drugs = json.loads(drugs_raw)
        drugs_1 = drugs
        return drugs_1

Client = OpenFDAClient()


class OpenFDAHTML():
    def html(self, list):
        list = []
        intro = "<!doctype html>" + "\n" + "<html>" + "\n" + "\t" + "<body>" + "\n" + "<ol>" + "\n"
        end = "<\ol>" + "\n" + "<body>" + "<html>"

        with open("data.html", "w") as f:
            f.write(intro)
            for element in list:
                element_1 = "<\t>" + "<li>" + element
                f.write(element_1)
            f.write(end)

HTML = OpenFDAHTML()

class OpenFDAparser():
    def data_drug(self,drugs_1,list):
        for i in range(len(drugs_1['results'])):
            if 'active_ingredient' in drugs_1['results'][i]:
                list.append(drugs_1['results'][i]['active_ingredient'][0])

    def data_company(self, drugs_1, list):
        for element in range(len(drugs_1["results"])):
            try:
                element=element["openfda"]["manufacturer_name"][0]
                list.append(element)
            except KeyError:
                element= " Unknow"
                list.append(element)


        def data_warning(self, drug_1, list):
            for element in range(len(drugs_1["results"])):
                try:
                    element = element["warnings"][0]
                    list.append(element)
                except KeyError:
                    element = "Unknow"
                    list.append(element)

Parser = OpenFDAparser()


class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open("search.html", "r") as f:
                message = f.read()
                self.wfile.write(bytes(message, "utf8"))

        elif "searchDrug" in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            if "&" in self.path:
                params = self.path.split("?")[1]
                drug = params.split("&")[0].split("=")[1]
                limit = params.split("&")[1].split("=")[1]
                drug_limit=Client.active_component(drug,limit)
                Parser.data_drug(drug_limit, list)
            if "&" not in self.path:
                params = self.path.split("?")[1]
                drug = params.split("&")[0].split("=")[1]
                limit=10
                drug_limit = Client.active_component(drug, limit)
                Parser.data_drug(drug_limit, list)
            HTML.html(list)


        elif "searchCompany" in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            if "&" in self.path:
                params = self.path.split("?")[1]
                drug = params.split("&")[0].split("=")[1]
                limit = params.split("&")[1].split("=")[1]
                esmeralda = Client.company(drug, limit)
                Parser.data_company(esmeralda, list)
            elif "&" not in self.path:
                params = self.path.split("?")[1]
                drug = params.split("&")[0].split("=")[1]
                limit = 10
                drug_limit = Client.active_component(drug, limit)
                Parser.data_drug(drug_limit, list)
            HTML.html(list)

        elif "searchCompany" in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            params = self.path.split("?")[1]
            limit = params.split("=")[1]

            rojo= Client.list(limit)

            Parser.data_company(rojo,list)

            HTML.html(list)
            with open("data.html", "r") as f:
                file = f.read()
            self.wfile.write(bytes(file, "utf8"))

            web_contents = file
            web_headers = "HTTP/1.1 200"
            web_headers += "\n" + "Content-Type: text/html"
            web_headers += "\n" + "Content-Length: %i" % len(str.encode(web_contents))

        elif "data" in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            params = self.path.split("?")[1]
            limit = params.split("=")[1]


            rubi= Client.list(limit)

            Parser.data_company(rubi, list)

            HTML.html(list)
            with open("data.html", "r") as f:
                file = f.read()
            self.wfile.write(bytes(file, "utf8"))
            web_contents = file
            web_headers = "HTTP/1.1 200"
            web_headers += "\n" + "Content-Type: text/html"
            web_headers += "\n" + "Content-Length: %i" % len(str.encode(web_contents))


        elif "listWarnings" in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            params = self.path.split("?")[1]
            limit = params.split("=")[1]
            plata = Client.list(limit)

            Parser.data_warning(plata, list)

            HTML.html(list)

            with open("data.html", "r") as f:
                file = f.read()
            self.wfile.write(bytes(file, "utf8"))

            web_contents = file
            web_headers = "HTTP/1.1 200"
            web_headers += "\n" + "Content-Type: text/html"
            web_headers += "\n" + "Content-Length: %i" % len(str.encode(web_contents))
        elif "secret" in self.path:
            self.send_response(401)
            self.send_header("WWW-Authenticate", "Basic realm='OpenFDA Private Zone")
            self.end_headers()

        elif "redirect" in self.path:
            self.send_response(302)
            self.send_header('Location', 'http://localhost:8000/')
            self.end_headers()

        else:
            with open("Error.html", "w") as f:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                intro = "<!doctype html>" + "\n" + "<html>" + "\n" + "\t" + "<body>" + "\n" + "<ol>" + "\n"
                end = "<\ol>" + "\n" + "<body>" + "<html>"
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

