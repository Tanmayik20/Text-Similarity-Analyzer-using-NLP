from flask import Flask,render_template,request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

def calculate_similarity(text1,text2):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([text1,text2])

    similarity = cosine_similarity(vectors[0],vectors[1])

    percentage = round(similarity[0][0]*100,2)

    return percentage


@app.route("/",methods=["GET","POST"])

def index():

    percentage=None

    if request.method=="POST":

        text1=request.form["text1"]

        text2=request.form["text2"]

        percentage=calculate_similarity(text1,text2)

    return render_template("index.html",percentage=percentage)


if __name__=="__main__":
    app.run(debug=True)