# CDBI
Community Decentralised Building Identity




# CODE

Le but est de relier les `proposals` d'un DAO à un compte Twitter. 

## Cycles de vie d'une `proposal`

Les `proposals` sont créés via une interface utilisateur (UI) **https://testnet.app.astrodao.com/all/feed** ou ON-CHAIN (via une commande à télécharger : `npm install near-cli` et le déploiement des "contrats" via cette commande). 

Une fois créée, tous ceux qui ont le droit peuvent voter. Ces actions se retrouve sous cette forme : 
```json
{
  "proposal": {
    "description": "POST : \n\nHello everyone, it's the first DAO's post. \n#nearcontest #SocialDAO\n\nIs it suitable ?$$$$$$$$ProposePoll",
    "kind": "Vote"
  }
}
```
Dont le détail est trouvable à l'adresse **https://explorer.testnet.near.org/transactions/5RDydfASkmNDZ9QUvCNeGUrvrRcgd9jbEaKNmNtBLitD**.

Ces informations se trouvent dans les arguments de la transaction.  

### Ceci  est le site pour créer des DAOs sur NEAR (EN VERSION TEST) avec UI. 
 Le repo de ce site se trouve ici **https://github.com/near-daos/astro-ui** s'il vous intéresse. Ce repo peut-être utile pour récupérer des infos 



