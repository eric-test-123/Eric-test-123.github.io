---
layout: home
title: "Trail Tested: Outdoor Gear & Guides"
description: "Expert picks, honest reviews, and curated guides for hikers, campers, and weekend warriors."
---

## 🏕️ Featured Posts

<ul>
  {% for post in site.posts limit:5 %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - <small>{{ post.date | date: "%B %d, %Y" }}</small>
    </li>
  {% endfor %}
</ul>

---

## 🔍 Explore by Category
- [Gear Reviews](./categories/gear)
- [Hiking Guides](./categories/hiking)
- [Camping Tips](./categories/camping)
- [Trail Food](./categories/food)

---

## 📬 Subscribe for Monthly Gear Picks
<form action="https://example.com/subscribe" method="POST">
  <input type="email" name="email" placeholder="you@example.com" required>
  <button type="submit">Subscribe</button>
</form>

