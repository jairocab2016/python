from flask import Flask
app = Flask(__name__)

@app.route("/")

def hello():
    return "Hello World!"

@app.route("/post/<int:post_id>")
def mostrar_post(post_id):
    return "Post %d" % post_id

if __name__== "__main__":
    app.run()