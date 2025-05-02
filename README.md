# 🎮 **Jeu du Pendu** 🏗️

Bienvenue dans le **jeu du pendu** ! Le but est simple : deviner un mot caché, lettre par lettre, avant que le dessin du pendu soit complet. À chaque erreur, une partie du pendu est dessinée. Le jeu se termine lorsque vous devinez le mot ou que le pendu est complètement dessiné.

---

## 📝 **Fonctionnalités principales**

* **Mot aléatoire** : Le jeu choisit un mot au hasard parmi une liste prédéfinie.
* **Affichage dynamique** : Le mot à deviner est affiché avec des lettres masquées (`*`), et les lettres correctement devinées sont révélées progressivement.
* **Proposition de lettres** : Vous proposez une lettre à chaque tour.

  * ✅ Si la lettre est correcte, toutes ses occurrences dans le mot sont révélées.
  * ❌ Si la lettre est incorrecte, une partie du pendu est dessinée.
* **Fin de la partie** :

  * 🏆 Si vous devinez le mot, vous gagnez !
  * ☠️ Si le pendu est complet, vous perdez.
* **Redémarrage ou quitter** : À la fin de chaque partie, vous pouvez choisir de recommencer ou de quitter
  
---

## 💻 **Comment jouer ?**

1. **Lancer le jeu** : Exécutez le script `jeu_pendu.py` pour démarrer
2. **Proposer des lettres** : Tapez une lettre à chaque tour. Le jeu vous indique les lettres déjà essayées
3. **Gagner ou perdre** :

   * 🏆 Si vous devinez le mot, vous gagnez !
   * ☠️ Si le pendu est complet, vous perdez, mais vous pouvez recommencer
4. **Rejouer ou quitter** : Après chaque partie, vous pouvez choisir de **rejouer** ou de **quitter**
