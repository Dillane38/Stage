#!/bin/bash 

olddir=$(pwd)
dir=${olddir##*/}
file=$olddir/idutils_index
cd ..
source Makefile.local
#GROUP=sto-linuxes
NEWGROUP=$(getent group $GROUP)
mkdir -p result.index.$dir
chgrp -R $GROUP result.index.$dir
cd result.index.$dir
touch intermediaire.txt
FICHIER=intermediaire.txt
lid -f $file --key=token $1 -S newline > $FICHIER
sed -i -e "s/$1//g" $FICHIER
touch result.index.txt
FILE=result.index.txt
for f in $(cat $FICHIER); do
	    echo "$f" >> $FILE 
done
rm $FICHIER
