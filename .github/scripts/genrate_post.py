import openai
import frontmatter
from datetime import datetime
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# Define topic — rotate or randomize for variety
topic = "Best Lightweight Hiking Stoves for Summer 2025"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a gear-savvy outdoor blogger who writes SEO-optimized content."},
        {"role": "user", "content": f"Write a 1000-word SEO blog post on: {topic}. Include gear recommendations with bullet points."}
    ],
    temperature=0.7,
)

body = response.choices[0].message.content
slug = topic.lower().replace(" ", "-").replace(",", "")
date_str = datetime.utcnow().strftime("%Y-%m-%d")
filename = f"_posts/{date_str}-{slug}.md"

post = frontmatter.Post(body, **{
    "title": topic,
    "date": date_str,
    "categories": ["gear", "camping"],
    "layout": "post"
})

with open(filename, "w") as f:
    f.write(frontmatter.dumps(post))

print(f"✅ Blog post generated: {filename}")

