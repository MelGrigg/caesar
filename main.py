from caesar import encrypt
import cgi
import webapp2

pageHead = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>
                Caesar
            </title>
            <style>
                body {
                    font-family:tahoma, arial, calibri, sans-serif;
                    font-size:14px;
                }

                #holder {
                    width:500px;
                    margin-top:100px;
                    margin-left:auto;
                    margin-right:auto;
                    background-color:#C4C4C4;
                    border-radius:15px;
                    border:1px solid #595959;
                    padding:20px;
                    text-align:center;
                    box-shadow:5px 5px 10px black;
                }

                label {
                    font-weight:bold;
                }

                textarea {
                    width:100%;
                    height:150px;
                    margin-top:15px;
                    margin-bottom:15px;
                }

                #error {
                    color:#D90000;
                    font-weight:bold;
                }
            </style>
        </head>
        <body>
"""

pageTail = """
        </body>
    </html>
"""

class MainHandler(webapp2.RequestHandler):
    def rotationCheck(self, amount):
        if not amount.isdigit():
            return True
        else:
            return False

    def get(self):
        caesarForm = """
            <div id="holder">
                <form action="/" method="post">
                    <label for="rotation">Rotate By:</label>
                    <input type="text" name="rotation" value="0" />
                    <br>
                    <textarea name="text"></textarea>
                    <br>
                    <input type="submit" value="Encrypt!" />
                </form>
            </div>
        """
        page = pageHead + caesarForm + pageTail
        self.response.write(page)

    def post(self):
        rotation = self.request.get("rotation")
        text = self.request.get("text")
        newText = ""
        error = ""
        if self.rotationCheck(rotation):
            error = "<p id=\"error\">Invalid rotation amount.</p>"
            newText = text
        else:
            newText = cgi.escape(encrypt(text, int(rotation)))
        caesarForm = """
            <div id="holder">
                <form action="/" method="post">
                    <label for="rotation">Rotate By:</label>
                    <input type="text" name="rotation" value="0" />
                    <br>
                    <textarea name="text">{0}</textarea>
                    <br>
                    <input type="submit" value="Encrypt!" />
                </form>
                {1}
            </div>
        """.format(newText, error)
        page = pageHead + caesarForm + pageTail
        self.response.write(page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
