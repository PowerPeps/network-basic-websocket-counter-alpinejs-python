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

### Fonctionnement

**Initialisation de la connexion :**
<img width="622" height="441" alt="image" src="https://github.com/user-attachments/assets/dcb3bf97-e982-4161-8158-97c5d106039f" />

Étapes :
1. Le client ouvre une connexion WebSocket vers `ws://localhost:8000/ws`
2. Le serveur accepte la connexion avec `websocket.accept()`
3. Le serveur ajoute cette connexion à la liste `connections[]`
4. Le serveur envoie immédiatement la valeur actuelle du compteur
5. Le client affiche cette valeur

**Modification de la valeur du Compteur :**
<img width="572" height="433" alt="image" src="https://github.com/user-attachments/assets/5859dcae-ad91-4b6b-bf55-fb5d82b7d565" />

**Étapes :**

1. **Client (Frontend)** :
   - L'utilisateur clique sur le bouton `+` ou `-`.
   - La fonction `change(d)` met à jour le compteur localement.
   - Un debounce de 250ms attend que l'utilisateur arrête de cliquer.
   - Envoie la nouvelle valeur du compteur au serveur via WebSocket.

2. **Serveur (Backend)** :
   - Reçoit le message JSON : `{"counter": la_nouvelle_valeur}`.
   - Met à jour la variable globale `counter`.
   - Appelle `broadcast()` pour notifier tous les clients.

3. **Broadcast** :
   - Parcourt la liste `connections[]`.
   - Envoie le nouveau compteur à chaque client connecté.
   - Si l'envoi échoue, retire le client de la liste (déconnexion automatique, le client re-tentera de ce connecter au bout de 3s).

4. **Reception** :
   - Les client reçoivent le message avec le nouveau compteur.
   - Ils mettent à jour leur affichage automatiquement avec alpinejs.

**Déconnexion &| Reconnexion :**

<img width="452" height="676" alt="image" src="https://github.com/user-attachments/assets/76dee0d7-8475-4f44-9091-0357dc4374f7" />


