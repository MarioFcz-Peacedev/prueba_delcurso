'''
                                            Cuadernillo virtual de Git y GitHub

'''
                                                #######################
                                                # Importancia de Git!
                                                #######################

'''
Es un control de versiones para evitar sobreescribir código en producción o en otras palabras una "time machine"

un proyecto es un "Repositorio" y se divide en:

- Repositorio Central (es recomendable hacer backups)
- Repositorio Distribuido (es como trabaja GitHub, todo el equipo tiene una copia del repositorio principal y al modificar el repo central todos reciben los cambios)

'''

                                                #######################
                                                # Importancia de Git!
                                                #######################


" COMANDOS BASICOS "

from codeop import CommandCompiler
from http.client import ImproperConnectionState
from importlib.abc import SourceLoader
from itertools import combinations_with_replacement
from socket import CAN_BCM_RX_ANNOUNCE_RESUME
from textwrap import shorten


- git -- version  # Es para saber la versión de git. (el "--" es para indicarle que viene una palabra completa y un "-" es para indicarle que son abreviaturas)
- git help  # Es la ayuda de git 

" Primera configuración"

- git config --global user.name "Mario Cabrera" # Para definir mi nombre o usuario

- git config --global user.email "mariocabrera65@live.com" # Para poner el correo que usamos en GitHub

- git config --global -e # para ver los emails, para editar aquí se presiona la tecla "a" y para guardar es la tecla "esc" + :wq! + enter

- git config core.autocrlf true # quitamos warnings

" Para crear nuestro primer repositorio"

Lo más básico es que tenemos que estar en el directorio de nuestro proyecto o repositorio


- git init # Esto inicializa el repositorio
- git status # Nos va a dar la info de los commits, de la rama donde estamos y otras cosas como si git esta haciendo seguimiento al repo.
- git add <archivo> # aqui añadimos los archivos a git, es como preparar los archivos para realizar el seguimiento.
- git add . # añadimos todo el directo a preparación
- git add *.<extensiondearchivo> #Añade todos los archivos a stage con ese tipo de extensión
- git reset archivo #Este comando nos permite bajar del stage un archivo y seguir editando
- git commit -m "<nombre_de_lo_que_hicimos>" #Realizamos el proceso de commit a los archivos
- git commit --amend -m "<nombre corregido de lo que hicimos>" #Este comando nos permite editar el nombre al ùltimo commit
- git checkout -- . # Sirve para restaurar todo el repositorio a como estaba en el commit anterior

- git branch # Nos indica la rama en la que estamos trabajando
- git branch -m "nombre que vamos a cambiar" "nombre que vamos a poner" # Comando para cambiar el nombre de una rama 

- git config --global init.defaultBranch main # Coloca por defecto el nombre de la rama principal a "main"
- git commit -am "<nombre de lo que hicimos" # Esto permite hacer un add y un commit en un solo comando, pero solo a archivos que ya esten añadidos en el stage
- git log # Con esto podemos ver el log de los commits


##############
# IMPORTANTE!!!
##############

#cuando Git encuentra que una carpeta esta vaciá no la sube por eso se debe crear un archivo dentro de ella que se llame ".gitkeep" esto no pesa nada y mantiene la carpeta


################

CREAR ALIAS 

################

- git status --short #Resumen del status

#crear un alias propio sirve para dar un atajo a un CommandCompiler

- git config --global alias.<nuevo atajo> status --short 

#un ejemplo -> git config --global alias.s status --short

- git log --oneline # Podemos ver mas compacto el log


- git config --global alias.lg "log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all" # crea un alias para resumir todo de una manera genial!, quedo con git lg


- git diff # Nos indica que diferencias hay en un archivo en sus diferentes versiones pero a los que no estan en el stage
- git diff --stage # Ver los cambios que estan en el stage

- git reset --soft HEAD^#     # NOs pemite editar un commit sin necesidad de realizar un commit nuevo, es decir, editar el stage que queramos, con el ^# donde al reemplazar el # eligiarimos el commit a editar (2,3,4,5...)

- git reset --mixed #deHash  ## Este comando nos devuelve a un punto especifico que queremos 
- git reset --hard #deHash  ## Este comando practicamente elimina los commits despues del hash que seleccionamos, o puede volver a un punto que ya eliminamos utilizando el numero de hash con git reflog

- git reflog #Es un comando que nos indica todos los log, incluso si se eliminaron
- git mv <nombre actual> <nuevo nombre> #Este comando puede mover un archivo, pero si estamos en el mismo directorio puede renombrar el archivo
- git rm <nombre de archivo> #Comando para eliminar un archivo


                                                #######################
                                                ######## Ramas! #######
                                                #######################

# Un "Merge" significa la unión de las ramas 

-Merge de tipo "Fast Forward" # Se dispara cuando git detecta que no hay cambios en la rama principal, funciona como si nunca hubiesemos activado la rama
- "Uniones automaticas" # Git detecta que en la rama principal hubo un cambio que la rama secundaria desconoce, pero, cuando intentamos hacer el merge git sabe que no se modificaron lineas iguales y hace la union automatica
- "Union Manual" # Cuando git detecta un conflicto y no puede unir automaticamente, por eso, nos pide que solucionemos manualemnte.

- git branch <Nombre de la rama> # Para crear una nueva rama

- git branch -# Para ver el listado de las ramas creadas
- git checkout <nombre de la rama> #Comando para movernos a la otra rama

#####

#SI QUIERO UNIR LAS RAMAS, DEBO ESTAR EN EL DIRECTORIO DE LA RAMA QUE ESPERA A LOS CAMBIOS 

- git merge <nombre de rama de la que traigo los cambios> #Comando para realizar la union de las ramas
- git branch -d <nombre de rama a eliminar> # Comando para eliminar una rama
- git branch -d <nombre de rama a eliminar> -f # la bandera -f sirve para realizar una eliminacion forzada

- git checkout -b <nombre de la rama a crear> #Comando que nos permite crear una rama y moverse a esta misma automaticamente



                                                #######################
                                                ######## Etiquetas! #######
                                                #######################

# Son  una referencia  a un commit  especifico

- git tag <nombre o número de versión> # Crea un tag
- git tag -d <nombre o número de versión> # Elimina un tag
- git tag -a v<número de versión> -m "<nombre de versión" # V(X.Y.Z) x = versión mayor o salidas importantes, Y = añaden funcionalidades al pryecto pero pequeños, Z = se arregla bug fix o detalles de errores
- git tag -a v<número de versión> <HASH del commit al que queremos taggear> -m "<nombre de versión o mensaje>
- git show <nombre del tag> # con esto obtenemos mas información de los tags hechos


                                                #######################
                                                ######## Stash #######
                                                #######################

# Se puede interpretar como una boveda o contenedor y de esta manera poner en "pausa" el trabajo

- git stash # Comando para guardar los cambios sin hacer commits
- git stash list # con esto miramos la lista de stash
- git stash pop # Restaura los archivos de la bóveda y guarda las modificaciones que se hicieron en otras ramas
- git stash clear # Elimina todos los stash en curso
- git stash apply stash@{"Numero del stash que queremos recuperar"} # Recuperar un stash en especifico
- git stash drop stash@{"numero del stash que queremos borrar"} # Borrar un stash en especifico
- git stash show stash@{"numer del stash que queremos ver info"} # Podemos ver la info del stash como sus cambios
- git stash save "Comentario para guardar el stash con un nombre"


                                                #######################
                                                ######## Rebase #######
                                                #######################

# es como actualizar una rama con avances de otro compañero, es decir, si tenemos unos avances y actualizan la rama, al hacer un rebase, actualiza el repositorio y nos ubica en los ultimos cambios con el trabajo adelantado que tenemos
o actualizar el punto inicial de la rama
'''
4 de los usos mas comunes 
- ordenar commits
- corregir mensajes de los commits
- unir commits
- separar commits
'''
# debo estar ubicado en la rama donde quiero que sean aplicados los cambios

- git rebase "nombre de la rama que quiero mover"
- git rebase -i HEAD~"Numero de commits que quiero manipular" #~ se obtiene con alt+126
-"squash" sirve para "chocar" dos commits o unirlos para hacer uno Solo 
-"reward" sirve para "renombrar" el commit
- "edit" sirve para editar el combinations_with_replacement


                                                #######################
                                                ######## GITHUB #######
                                                #######################


