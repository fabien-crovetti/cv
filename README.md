# Mon CV

CV bilingue construit avec Vue 3, Vue Router, Vue I18n, Tailwind CSS et Vite SSG.

## Développement

```sh
yarn install
yarn dev
```

Avec Docker : `docker compose up --build`, puis ouvrir http://localhost:8001.

## Production

```sh
yarn build
yarn preview
```

Vite SSG génère le contenu français du CV dans `dist/index.html`. La langue
mémorisée sous `defaultLocale` est restaurée après l'hydratation Vue.
Les routes `/` et la page 404 restent gérées par Vue Router.

Le thème et les seuils responsive sont définis dans `src/styles/main.css`.
Roboto et les icônes Material Design sont conservés pour la présentation.

## Générer les CV PDF (français et anglais)

Prérequis : dépendances Node du projet installées (`yarn install`), Python 3.9+
avec `venv` et `pip`. Sur Debian/Ubuntu : `sudo apt install python3-venv`.

Une seule fois, depuis le dossier du projet (Linux/macOS) :

```sh
npm run pdf:setup
```

Puis après une modification du contenu :

```sh
npm run pdf
```

La commande produit **les deux langues** dans `public/cv-fabien-crovetti-fr.pdf`
et `public/cv-fabien-crovetti-en.pdf`. Les boutons du site utilisent déjà ces
fichiers. Générer les PDF avant `yarn build`, puis committer les deux PDF avec
les modifications de contenu. La génération reste manuelle, hors CI.

Avec Docker, reconstruire le service Node une première fois pour disposer de
Python, puis exécuter dans ce service `npm run pdf:setup` et `npm run pdf`.
Sous Windows, créer l'environnement avec `python -m venv .venv-pdf`, puis
`.venv-pdf\Scripts\python -m pip install -r scripts/pdf/requirements.txt` ;
`npm run pdf` détecte cet environnement automatiquement.
`PDF_PYTHON` permet de choisir un autre exécutable Python.

### Quels contenus modifier ?

- `src/i18n/fr.ts` et `src/i18n/en.ts` : contenus communs au site et aux PDF.
  Mettre à jour chaque langue ; aucune traduction automatique n'est effectuée.
- Les expériences sont toutes reprises (dates, poste, lieu et **bullets**).
  Le champ historique `information` n'est pas utilisé par le PDF.
- Pour conserver une page A4, le profil utilise `userAbout.text1` et
  `search.text`, la formation reprend diplôme/date/établissement, et les projets
  sont présentés par leur nom et leur lien. Toutes les compétences et langues
  sont incluses. Les descriptions longues des projets et les loisirs restent
  sur le site.
- `scripts/pdf/profile.json` : identité et coordonnées du PDF.
- `src/assets/user.png` : portrait partagé avec le site.
- `scripts/pdf/render.py` : mise en page ; polices Lato embarquées avec leur licence.

Si un contenu dépasse la page, la commande échoue en indiquant la langue et le
passage concerné. **Les deux anciens PDF sont conservés** tant que les deux
versions ne passent pas le contrôle. Raccourcir le texte concerné puis relancer.
Ouvrir les deux résultats pour vérifier la mise en page avant publication.
