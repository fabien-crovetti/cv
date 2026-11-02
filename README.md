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
