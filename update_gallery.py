import os

files = [
    "1001388839.jpg", "1001388840.jpg", "1001388841.jpg", "1001388842.jpg", "1001388843.jpg",
    "1001388844.jpg", "1001388845.jpg", "1001388846.jpg", "1001388847.jpg", "1001388848.jpg",
    "1001388849.jpg", "1001388850.jpg", "1001388851.jpg", "1001388852.jpg", "1001388853.jpg",
    "1001388854.jpg", "1001388856.jpg", "1001388857.jpg", "1001388859.jpg", "1001388860.jpg",
    "1001388861.jpg", "1001388862.jpg"
]

html = '      <div id="mainGallery" style="display:flex; gap:20px; overflow-x:auto; scroll-snap-type:x mandatory; scroll-behavior:smooth; -ms-overflow-style:none; scrollbar-width:none; padding:10px 0;">\n'
for f in files:
    html += f"""        <div class="gallery-item" style="flex: 0 0 85%; max-width: 380px; scroll-snap-align: center; position:relative; border-radius:18px; overflow:hidden; min-height:340px; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
          <img src="assets/gallery/{f}" alt="Gallery" style="width:100%; height:100%; object-fit:cover; position:absolute; inset:0; filter: blur(0.8px); transition: all 0.4s ease;" onmouseover="this.style.filter='blur(0)'; this.style.transform='scale(1.04)';" onmouseout="this.style.filter='blur(0.8px)'; this.style.transform='scale(1)';">
        </div>\n"""
html += '      </div>'

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Replace lines 586 to 610 (0-indexed 585:610)
lines[585:610] = [html + '\n']

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
