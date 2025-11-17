# network-basic-websocket-counter-alpinejs-python
Travaux pratique en Python &amp; web pour un travail pratique, du cours de réseau de l'universita di corsica pasquale paoli.

### Prérequis
```bash
pip install fastapi uvicorn websockets
```

### Démarrage
```bash
python main.py
```

### Accès
Ouvrez plusieurs onglets/fenêtres sur : `http://127.0.0.1:8000/static/index.html`

---

**Initialisation et Polling :**

Étapes :
1. Le client démarre et appelle immédiatement `fetchCounter()`
2. Le serveur répond avec `GET /api/counter` → `{"counter": valeur_actuelle}`
3. Le client affiche la valeur reçue
4. Un `setInterval` de 1000ms est lancé pour interroger le serveur en boucle
5. Toutes les secondes, le client redemande la valeur via `GET /api/counter`

**Modification de la valeur du Compteur :**

**Étapes :**

1. **Le Client** :
   - Quand l'utilisateur clique sur le bouton `+` ou `-`
   - La fonction `change(d)` met à jour le compteur localement
   - Un debounce de 250ms attend que l'utilisateur arrête de cliquer
   - Envoie la nouvelle valeur au serveur via `POST /api/counter` avec `{"counter": la_nouvelle_valeur}`

2. **Le Serveur** :
   - Reçoit le message JSON : `{"counter": la_nouvelle_valeur}`
   - Met à jour la variable globale `counter`
   - Répond avec la nouvelle valeur

3. **Synchronisation** :
   - Les autres clients récupèrent la nouvelle valeur lors de leur prochain polling (max 1 seconde de délai)

**Gestion de la connexion :**

Étapes :
1. À chaque requête `fetch`, le client vérifie si le serveur répond
2. Si succès → `connected = true` (affichage "OK" en vert)
3. Si échec → `connected = false` (affichage "NOP" en rouge)
4. Le polling continue automatiquement et se reconnecte dès que le serveur est à nouveau disponible

---

**Nota-Bene** : Pour une version sans pooling & sans websocket, veuillez seulement enléver le polling toutes les 1s.
