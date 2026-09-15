# Changelog

Toutes les évolutions notables de `cdn` sont documentées ici.

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), versionnage
[SemVer](https://semver.org/lang/fr/). La section `[Unreleased]` accumule au fil de l'eau et
est renommée en numéro de version au moment de poser le tag.

Ce fichier est créé le 2026-09-05, après la mise en service : les évolutions antérieures ne sont
pas reconstituées, ce qui serait de la réécriture d'historique plutôt que de la documentation.
L'historique git reste la source de vérité pour ce qui précède.

## [Unreleased]

### Ajouté

- `fonts/cedule-fonts.css` : polices de l'administration Cédule. IM Fell English SC pour les
  intitulés, EB Garamond pour le texte, Fragment Mono pour les heures. **Blocs extraits par script**
  de `nopost-fonts.css`, `hucheor-fonts.css` et `noisecrypt-fonts.css` plutôt que réécrits, et les
  17 fichiers référencés ont été vérifiés présents sur le disque avant commit.

### Ajouté

- **`fonts/breme-fonts.css`**, pour le site vitrine de Brême : Fraunces en titrage, Space Mono
  pour les libellés et les chiffres. Ce sont **exactement les deux familles de l'application
  mobile**, et c'est le point : le site et l'app sont le même produit, une police différente entre
  les deux se voit immédiatement. Esprit « grand livre de compte », cohérent avec la direction
  artistique « Grand Livre Hanséatique » de l'app.
- Les blocs `@font-face` sont **extraits** de `maeil-fonts.css` (Fraunces) et `patelin-fonts.css`
  (Space Mono) plutôt que réécrits : une plage `unicode-range` recopiée de travers fait
  silencieusement tomber les caractères accentués sur un sous-ensemble, défaut qu'aucune relecture
  n'attrape. URL relatives, comme toutes les feuilles d'ici.

### Ajouté

- **`fonts/noisecrypt-fonts.css`**, pour le site vitrine de NoiseCrypt : Fragment Mono en
  titrage, IBM Plex Sans en corps, IBM Plex Mono pour les commandes. La monospace en display
  n'est pas décorative, l'identité visuelle de l'outil étant la grille de cellules noires et
  blanches que son codec dessine à l'écran. Plex Sans porte un manuel, et Plex Mono est conçu
  pour aller avec lui. URL relatives, comme toutes les feuilles d'ici.

### Corrigé

- **Convention de fins de ligne du parc posée dans `.gitattributes`.** Le bloc `run:` d'un
  workflow GitHub Actions est un script shell exécuté sur un runner Linux : un antislash de
  continuation suivi d'un retour chariot **ne continue pas** la ligne, la commande est coupée en
  deux, et le message d'erreur ne parle jamais de fins de ligne.
- Cas réel du 2026-09-07 sur `bzhzion/cabanon` : un `.yml` recommité en CRLF depuis une machine
  Windows (où `core.autocrlf` est actif) a fait échouer le déploiement de l'API sur un
  `usage: ssh`, la destination de la commande ayant disparu avec la continuation.
- LF forcé sur ce qu'exécute Linux (`*.sh`, `*.yml`, `*.yaml`, `Dockerfile`), CRLF sur ce
  qu'exécute Windows (`*.ps1`, `*.bat`, `*.cmd`), et `* text=auto` comme filet général.
  Référence : `admin/.claude/gitattributes-parc`.


## [0.1.0] - 2026-09-05

### Modifié

- **Le déploiement ne part plus sur un push de branche, mais sur un tag `vX.Y.Z`.** Pousser un
  correctif de documentation ou une expérimentation sur `main` déclenchait jusqu'ici une livraison
  en production, ce qui va contre la règle du parc et rend toute modification du dépôt risquée.
  `workflow_dispatch` est conservé comme filet, ainsi que les crons de reconstruction et les
  déclencheurs de `pull_request`, qui sont des vérifications et non des livraisons.
- Volontairement **sans filtre de chemin** : GitHub combine (branches/tags) ET `paths`, ce qui rend
  un déclencheur sur tag imprévisible dès qu'un filtre de chemin subsiste.

### Ajouté

- **Convention changelog du parc posée sur ce dépôt** : ce fichier, les hooks `pre-commit` et
  `pre-push` dans `.githooks/`, et le workflow `changelog-guard.yml` qui rejoue les mêmes
  contrôles en CI au moment du tag. Ce dépôt en était dépourvu alors qu'il est déployé, ce qui
  le laissait hors de la garantie que les autres ont.

