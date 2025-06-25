AI News Assistant
AI News Assistant is a web application that fetches and summarizes news articles, analyzes sentiment, and supports multi-language translation. Users can get news by keyword search, URL summary, or plain text input, all powered by Python Flask backend and modern frontend.

Features
Fetch latest news and search news by keywords (supports multiple words).

Summarize articles from URLs or plain text input.

Analyze sentiment (positive, neutral, negative).

Display article metadata: title, author, published date, top image.

Translate summaries into multiple languages including Indian languages.

Responsive and user-friendly UI with consistent blue/black color palette.

Tech Stack
Backend: Python Flask, NewsAPI, Newspaper3k, TextBlob, Googletrans

Frontend: HTML, CSS, JavaScript (Vanilla)

Deployment-ready with Gunicorn for production
Steps
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/ai-news-assistant.git
cd ai-news-assistant
Create and activate a virtual environment (optional but recommended)

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set environment variables

Create a .env file in the root folder and add your API key:

ini
Copy
Edit
NEWS_API_KEY=your_newsapi_key_here
Or export directly:

bash
Copy
Edit
export NEWS_API_KEY=your_newsapi_key_here  # Linux/Mac
set NEWS_API_KEY=your_newsapi_key_here     # Windows CMD
Run the Flask app

bash
Copy
Edit
flask run
Open your browser at http://127.0.0.1:5000
Usage
Get News: View latest news headlines.

Summarize Text: Paste any text and get a summary with sentiment.

Summarize from URL: Paste an article URL, fetch summary, sentiment, and metadata.

Search News: Enter keywords to fetch related news articles.

License
MIT License © 2025 Eakshitha KrishnaMurthy
