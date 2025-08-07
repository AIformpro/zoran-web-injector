# Zoran Web Injector

Cette application fournit une interface web pour tester les *glyphes glottaux* du cadre mimétique **Zoran IA**. Elle utilise Flask pour gérer les requêtes HTTP et le rendu de gabarits.

## Contenu du dépôt

- **`app.py`** : application Flask minimaliste qui expose une route pour entrer un glyphe et afficher le résultat du parseur.
- **`templates/index.html`** : gabarit HTML avec un formulaire d’entrée et une zone d’affichage du résultat.
- **`.gitignore`** : exclusions standard pour les environnements Python, build et IDE.

## Prérequis

- Python 3.8+
- [Flask](https://flask.palletsprojects.com/) (installé via `pip install flask`)
- **glottal_parser** (issu du dépôt principal `zoran-ia`)

## Démarrage rapide

1. Clonez ce dépôt et placez-vous dans le répertoire :
   ```bash
git clone https://github.com/AIformpro/zoran-web-injector.git
cd zoran-web-injector
```
2. Installez les dépendances :
   ```bash
pip install flask
```
   (Assurez-vous aussi que le module `glottal_parser.py` est accessible via votre `PYTHONPATH`.)
3. Lancez le serveur :
   ```bash
python app.py
```
4. Rendez-vous sur [http://localhost:5000](http://localhost:5000) puis saisissez un glyphe dans le champ prévu.

## Structure

```
zoran-web-injector/
├── app.py
├── templates/
│   └── index.html
├── .gitignore
└── README.md
```

## Licence

Ce projet est distribué sous licence MIT, comme l’ensemble de l’écosystème Zoran.
