document.getElementById('urlForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const url = document.getElementById('articleUrl').value;

  const response = await fetch('http://127.0.0.1:5000/summarize_url', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url })
  });

  const data = await response.json();

  if (data.error) {
    document.getElementById('urlSummaryOutput').innerHTML = `<p>Error: ${data.error}</p>`;
  } else {
    document.getElementById('urlSummaryOutput').innerHTML = `
      <h2>${data.title}</h2>
      <p><strong>Author(s):</strong> ${data.authors.join(', ') || "N/A"}</p>
      <img src="${data.top_image}" alt="Top Image" style="max-width: 400px;"><br><br>
      <p><strong>Summary:</strong> ${data.summary}</p>
      <p><strong>Sentiment:</strong> ${data.sentiment}</p>
      <p><small>Polarity: ${data.polarity.toFixed(2)} | Subjectivity: ${data.subjectivity.toFixed(2)}</small></p>
    `;
  }
});
