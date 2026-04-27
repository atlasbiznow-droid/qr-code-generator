# ABN Free QR Code Generator

## Deployment Instructions

### Option 1: GitHub Pages (Recommended - Free)

1. **Create a GitHub Repository**
   - Go to https://github.com/new
   - Name: `qr-code-generator`
   - Make it **Public** (GitHub Pages requires public repos)

2. **Upload Files**
   ```bash
   # Clone the repo
   git clone https://github.com/YOUR_USERNAME/qr-code-generator.git
   cd qr-code-generator
   
   # Copy the files
   # (index.html, adsense-config.js, ads.txt, README.md)
   
   # Push to GitHub
   git add .
   git commit -m "Initial QR Code Generator"
   git push origin main
   ```

3. **Enable GitHub Pages**
   - Go to your repo → Settings → Pages
   - Source: **Deploy from a branch**
   - Branch: `main` (or `gh-pages`)
   - Folder: `/ (root)`
   - Save

4. **Your site will be at:**
   ```
   https://YOUR_USERNAME.github.io/qr-code-generator/
   ```

### Option 2: Google Sites Embed

1. **Upload to GitHub Pages first** (see above)
2. **Get your raw URL:**
   ```
   https://raw.githubusercontent.com/YOUR_USERNAME/qr-code-generator/main/index.html
   ```
3. **Embed in Google Sites:**
   - Edit your Google Site
   - Insert → Embed → URL
   - Paste the GitHub Pages URL:
     ```
     https://YOUR_USERNAME.github.io/qr-code-generator/
     ```

### Option 3: Netlify (Alternative)

1. **Sign up at** https://netlify.com
2. **Drag & drop** the folder with your files
3. **Get your URL** instantly

---

## Files Included

| File | Purpose |
|------|---------|
| `index.html` | Main QR Generator app |
| `adsense-config.js` | AdSense config (update with your publisher ID) |
| `ads.txt` | AdSense verification |
| `README.md` | This file |

---

## AdSense Setup

1. Create account at https://adsense.google.com
2. Get your publisher ID (`pub-xxxxxxxxxxxxxxx`)
3. Edit `adsense-config.js` and replace `YOUR_PUBLISHER_ID`
4. Create ad units and get slot IDs
5. Update the ad unit IDs in `adsense-config.js`
6. Set `enabled: true` when ready

**Tip:** Use a custom domain for better AdSense approval!

---

## Custom Domain (Optional)

1. Buy a domain (e.g., from Namecheap, Cloudflare)
2. Go to your GitHub repo → Settings → Pages
3. Add your custom domain under "Custom domain"
4. Update DNS records as instructed

---

## Need Help?

- GitHub Pages Docs: https://docs.github.com/en/pages
- AdSense Help: https://support.google.com/adsense