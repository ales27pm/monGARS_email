#!/bin/bash

# Installer les dépendances du backend
cd backend
pip install -r requirements.txt

# Installer les dépendances du frontend
cd ../frontend
npm install

echo "Installation terminée."
