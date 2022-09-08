Ce dépot git contient le script d'utilisation de idutils utilé dans le makefile de linux-infra.
Il contient aussi un programme python utilisant la bibliothèque Enoslib.
Pour déployer une image avec Enoslib il faut rajouter trois arguments dans la variable d"deploye configuration conf qui sont:
env_name: préciser le path pour trouver l'image (stocker l'image sur l'APIde grid5000)
job_type: "deploy" pour préciser qu'on fait le déploiement
force_deploy: "True" pour forcer le déploiement en cas d'erreur
Pour faire du parallélisme sur les noeuds, il faut spécifier la stratégie : free et le background : true dans la commande actions.
De plus plusieurs personnalisations sont possible dans le fichier de configuration de Enoslib.
Pour finir le programme python réalise l'expérience en attribuant chaque noeud à une faute de manière parallèle puis fait une boucle sur l'ensemble des versions linux disponibles. 
