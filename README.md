# Server-Manager

** /!\ **Le projet vas bientôt recevoir des modifications majeures 

Le projet s'oriente plus vers un manager de configuration de Systemd que un outils de virtualisation de programme tels que Pufferpanel ou Pterodactyle

`Base de donnée`
### Server
identifiants unique  :  id <br>
nom d'affichage : name <br>
nom config systemd : local_name<br>
nom du gérant: owner_name<br>
permission: permission

```mariadb
CREATE TABLE server(id INT AUTO_INCREMENT PRIMARY KEY , name TEXT, local_name TEXT, owner_name TEXT, permission JSON);
```