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
            drugs_1 = str(drugs)


        def company(self,drug,limit):
            conn = http.client.HTTPSConnection("api.fda.gov")
            headers = {'User-Agent': 'http-client'}
            url = "/drug/label.json?search=brand_name:" + company + "&" + "limit=" + limit
            print(url)
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            drugs_raw = r1.read().decode("utf-8")
            conn.close()
            drugs = json.loads(drugs_raw)
            drugs_1 = str(drugs)


        def list(self,drug,limit):
            self.send_response(200)
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            url = "/drug/label.json?" + "limit=" + limit
            print(url)
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            drugs_raw = r1.read().decode("utf-8")
            conn.close()
            drugs = json.loads(drugs_raw)
            drugs_1 = str(drugs)
            self.wfile.write(bytes(drugs_1, "utf8"))

    Client = OpenFDAClient()

    class OpenFDAparser()
        def data_drug(self,drug_1,list):
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

        def data_company(self, drug_1, list):
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

        def data_warning(self, drug_1, list):
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

    Parser = OpenFDAParser()


    class OpenFDAHTML()

        def html(self,list)
            list = []
            intro = "<!doctype html>" + "\n" + "<html>" + "\n" + "\t" + "<body>" + "\n" + "<ol>" + "\n"
            end = "<\ol>" + "\n" + "<body>" + "<html>"

    HTML = OpenFDAHTML()


    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):

        if self.path == "/":
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
                dug_limit=Client.active_component(drug,limit)
                Parser.data_drug(drug_limit, list_1)
            if "&" not in self.path:
                params = self.path.split("?")[1]
                drug = params.split("&")[0].split("=")[1]
                limit=10
                dug_limit = Client.active_component(drug, limit)
                Parser.data_drug(drug_limit, list_1)
            HTML.html(list_1)


        elif "searchCompany" in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            if "&" in self.path:
                params = self.path.split("?")[1]
                drug = params.split("&")[0].split("=")[1]
                limit = params.split("&")[1].split("=")[1]
                esmeralda = Client.company(drug, limit)
                Parser.data_company(esmeralda, list_1)
            if "&" not in self.path:
                params = self.path.split("?")[1]
                drug = params.split("&")[0].split("=")[1]
                limit = 10
                dug_limit = Client.active_component(drug, limit)
                Parser.data_drug(drug_limit, list_1)
            HTML.html(list_1)

        elif "listDrug" in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            params = self.path.split("?")[1]
            limit = params.split("=")[1]

            rojo= Client.active_componentlist(limit)

            Parser.data_company(rojo,list_1)

            HTML.html(list_1)

            self.wfile.write(bytes(file, "utf8"))

            web_contents = file
            web_headers = "HTTP/1.1 200"
            web_headers += "\n" + "Content-Type: text/html"
            web_headers += "\n" + "Content-Length: %i" % len(str.encode(web_contents))

        elif "listCompanies" in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            params = self.path.split("?")[1]
            limit = params.split("=")[1]
            self.wfile.write(bytes(file, "utf8"))

            rubi= Client.list(limit)

            Parser.data_company(rubi, list_1)

            HTML.html(list_1)
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

            Parser.data_warning(plata, list_1)

            HTML.html_visual(list_1)


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

