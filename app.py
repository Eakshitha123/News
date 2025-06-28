from flask import Flask, request, jsonify, render_template
from newspaper import Article
from textblob import TextBlob
from flask_cors import CORS
import requests
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from newsapi import NewsApiClient

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend to talk to backend

newsapi = NewsApiClient(api_key='8f0c6c1305ad4992a325957e93a9c669')

NEWS_API_KEY = '8f0c6c1305ad4992a325957e93a9c669'  # Replace with your real API key

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/summary')
def summary():
    return render_template('summary.html')

@app.route('/url')
def url_summarize():
    return render_template('url.html')

@app.route('/search_news', methods=['POST'])
def search_news():
    data = request.get_json()
    keyword = data.get('keyword', '')

    if not keyword:
        return jsonify({'error': 'Keyword is required'}), 400

    try:
        newsapi = NewsApiClient(api_key=NEWS_API_KEY)
        results = newsapi.get_everything(q=keyword, language='en', page_size=10)

        articles = []
        for article in results['articles']:
            articles.append({
                'title': article['title'],
                'description': article['description'],
                'url': article['url'],
                'image': article['urlToImage']
            })

        return jsonify(articles)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/default_news')
def default_news():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           f'apiKey={NEWS_API_KEY}')
    try:
        response = requests.get(url)
        data = response.json()

        articles = []
        for item in data.get('articles', []):
            articles.append({
                'title': item.get('title'),
                'description': item.get('description'),
                'url': item.get('url'),
                'image': item.get('urlToImage')
            })

        return jsonify(articles)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize_text', methods=['POST'])
def summarize_text():
    data = request.json
    text = data.get('text')

    if not text or len(text.strip()) == 0:
        return jsonify({"error": "Text is empty."}), 400

    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LexRankSummarizer()
        summary_sentences = summarizer(parser.document, 3)

        summary = " ".join(str(sentence) for sentence in summary_sentences)

        blob = TextBlob(summary)
        polarity = blob.polarity
        subjectivity = blob.subjectivity
        sentiment = "😊 Positive" if polarity > 0 else "😐 Neutral" if polarity == 0 else "😠 Negative"

        return jsonify({
            "summary": summary,
            "sentiment": sentiment,
            "polarity": round(polarity, 3),
            "subjectivity": round(subjectivity, 3)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/summarize_url', methods=['POST'])
def summarize_url():
    data = request.json
    url = data.get('url')

    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        summary = article.summary
        title = article.title
        authors = article.authors
        top_image = article.top_image

        blob = TextBlob(summary)
        polarity = blob.polarity
        subjectivity = blob.subjectivity

        sentiment = "😊 Positive" if polarity > 0 else "😐 Neutral" if polarity == 0 else "😠 Negative"

        return jsonify({
            "title": title,
            "authors": authors,
            "top_image": top_image,
            "summary": summary,
            "sentiment": sentiment,
            "polarity": polarity,
            "subjectivity": subjectivity
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
