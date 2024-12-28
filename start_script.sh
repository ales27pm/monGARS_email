#!/bin/bash

# Démarrer le backend
cd backend
python app.py &

# Démarrer le frontend
cd ../frontend
npm run serve

echo "Services démarrés."
