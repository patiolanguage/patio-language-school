# Patio Language School — website

The website for [patiolanguage.pt](https://patiolanguage.pt), a language school and
cultural community in Lagos, Portugal.

## What this is

A hand-coded **static site**: plain HTML + one CSS file, with a small amount of
vanilla JavaScript. **No framework, no build step, no backend** — the files are
served as-is.

- No `package.json`, no React/Vue/Next/Vite/Tailwind, no bundler.
- To make changes: edit the HTML/CSS and redeploy (see below). Nothing to install or compile.

## Structure

```
index.html            Main one-page site (English) with anchor sections
about.html            (redirect/stub)
classes.html          (redirect/stub)
contact.html          (redirect/stub)
pt/index.html         European Portuguese version
css/style.css         Single stylesheet (cache-busted via ?v=NN in the HTML)
assets/img/           Images, icons, logos
_redirects            Cloudflare Pages redirects (short links)
social/               Marketing assets + Python generators (not part of the site)
merch/                Merch catalogue (HTML + PDF)
forms/                Google Apps Script for the registration form
```

## Tech / integrations

- **Fonts:** Google Fonts (Anton for headings, Barlow for body).
- **Bilingual:** English at `/`, European Portuguese at `/pt/`, linked with `hreflang` tags.
- **Contact form:** [Formspree](https://formspree.io) (submissions go to patiolanguage@gmail.com). No server code.
- **Newsletter:** [MailerLite](https://mailerlite.com) embedded form + universal script. The same
  form is embedded twice (hero + footer), so a small inline script de-duplicates the element ids.
- **Class registration:** an external Google Form. Short links `/inscrever` (PT) and `/register` (EN)
  redirect to it via `_redirects`.

## Hosting & deploy

- Hosted on **Cloudflare Pages**; custom domain **patiolanguage.pt** on Cloudflare DNS.
- Deploys are done with the **Wrangler** CLI from a clean `dist/` folder:

  ```bash
  # build a clean dist/ (copy the html + css/ + assets/img/ + pt/ + _redirects), then:
  npx wrangler pages deploy dist --project-name=patio-language-school --branch=main --commit-dirty=true
  ```

- `dist/`, `.wrangler/`, and a few scratch files are git-ignored.

## Source control

GitHub: [patiolanguage/patio-language-school](https://github.com/patiolanguage/patio-language-school)

## Notes

- Bump the CSS cache-buster (`?v=NN` on the `style.css` link in each HTML file) when you change `css/style.css`.
- CDN edge cache can serve old pages for a while after deploy; purge in the Cloudflare dashboard if needed.
