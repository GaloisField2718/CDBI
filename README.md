# CDBI

**Community Decentralised Building Identity**



# How to install

``` bash
pip3 install tweepy
```
Fill `config.py` file.




# What you need ?

A twitter developper account (in free and basic version [Twitter developers](https://developer.twitter.com/en)) and tokens with `Write Permission`.

At least one Near Wallet to create the DAO and post proposals, you can [create a wallet on testnet](https://wallet.testnet.near.org/) or [on the mainnet](https://wallet.near.org/).


# How to create a DAO on AstroDAO

[Doc AstroDAO](https://github.com/near-daos/astro-ui/wiki/Use-cases#why-start-a-dao) This documentation is not fulfil but I will complete it soon.



# Working discussion with the Team


### CODE

Le but est de relier les `proposals` d'un DAO à un compte Twitter. 

Une idée pourrait être de créer un fichier Python qui observe les actions du DAO et lorsqu'il voit un action : `Vote` avec une `proposal` de la forme "POST : ..." (par exemple) prendrait le contenu qui suit "POST" et ferait un Tweet contenant ce texte. 

Pour ce faire il va falloir :

i) Intéragir on-chain avec le DAO (au moins pouvoir récupérer les actions et arguments) ;  

ii) Communiquer avec l'API Twitter pour mettre online le POST souhaité (ou réaliser l'action souhaitée) ;

iii) Faire tourner tout ça en continue ou au moins s'assurer de l'éxecution de ce code suite à la validation d'une telle `proposal`. 


### Les étapes d'un Algo

#### Répétition de la boucle

Ici la répétition peut être dans un premier temps toutes les 6h puis sera affiner avec le temps et la maturation du projet.

#### Récupère le `Texte` à poster

Pour récupérer le `Texte` je pense qu'il va falloir faire de la ligne de commande. 

Pour ce faire deux choses à utiliser d'après moi : 

\item
```bash
npm install -g near-cli

near login
```
Les infos sur **https://github.com/near/near-cli**

\item
Soit tout faire avec `near` soit utiliser la commande `sputnik` **https://github.com/cloudmex/sputnikdao-cli**

```bash
npm install -g sputnikdao

sputnikdao --help
```

Avec ces commandes il doit être relativement aisé de récupérer la Description de la `proposal` souhaitée.


#### Exécute le Post Twitter avec le `Texte`

Afin d'exécuter le POST sur Twitter, il doit falloir exécuter une commande du style : 
`https://twitter.api.com/POST/ACCES_KEYS/title=""?message="`Text``

Pour cela il faut tester et creuser : **https://developer.twitter.com/en/docs/twitter-api/migrate/twitter-api-endpoint-map** 
Un topic *help* provenant de Twitter est dispo à l'adresse **https://help.twitter.com/en/rules-and-policies/twitter-api**




////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

## Présentation très courte des DAOs

### Cycles de vie d'une `proposal`

Les `proposals` sont créés via une interface utilisateur (UI) **https://testnet.app.astrodao.com/all/feed** ou ON-CHAIN (via une commande à télécharger : `npm install near-cli` et le déploiement des "contrats" via cette commande). 
Les arguments créés sont de cette forme : 
```json
{
  "proposal": {
    "description": "POST : \n\nHello everyone, it's the first DAO's post. \n#nearcontest #SocialDAO\n\nIs it suitable ?$$$$$$$$ProposePoll",
    "kind": "Vote"
  }
}
```

Une fois créée, tous ceux qui ont le droit peuvent voter. Ces actions se retrouve sous cette forme : 
<img width="722" alt="Capture d’écran 2022-10-24 à 22 37 23" src="https://user-images.githubusercontent.com/84255448/197624527-f31ad9c1-96e6-4911-962d-c1c71d74a217.png">


Dont le détail est trouvable à l'adresse **https://explorer.testnet.near.org/transactions/5RDydfASkmNDZ9QUvCNeGUrvrRcgd9jbEaKNmNtBLitD**.

Ces informations se trouvent dans les arguments de la transaction. *Je vais chercher la commande pour détailler les opérations d'une transaction en ligne de commande.*

Suite à quoi la proposition a un statut noté `finalized` et `approved` ou `rejected`.

### Proposition de mise en pratique

Pour mettre en pratique tout ceci je vous propose que suite à la création d'un wallet sur testnet, nous créeyons un DAO afiin de s'exercer à prendre des décisions basiques entres nous. 

Cela permettra de voir ce qu'il en est et de mieux saisir les utilisations et limitations. 

N'hésitez pas à détailler vos visions et à ce que l'on échange dans les différents canaux sur ce repo !

####### Repo AstroDAO (UI)
Le repo d'AstroDAO UI se trouve ici **https://github.com/near-daos/astro-ui** s'il vous intéresse. Ce repo peut-être utile pour récupérer des infos 



