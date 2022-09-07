#!/bin/bash

#Script pour coccinelle

FLAGS="-timeout 90 -use_idutils -no_includes -include_headers"
if [ "$1" = "realloc.cocci" -a "$1" = "noderef.cocci" -a "$1" = "var.cocci" -a "$1" = "ret6.cocci"]
then
	FLAGS1="-timeout 90 -use_idutils"
        spatch $FLAGS1 -sp_file ./cocci/$1 -dir /root/linuxes/$2 2> /root/Dune_fault_linux/faults-in-Linux/faults/results/linuxes/$2/Linux_$1.log > /root/Dune_fault_linux/faults-in-Linux/faults/results/linuxes/$2/Linux_$1.orig.org
elif [ "$1" = "intr_noarg.cocci" ]
then
	FLAGS2="-D lock=cli -D unlock=sti"
        spatch $FLAGS $FLAGS2 -sp_file ./cocci/$1 -dir /root/linuxes/$2 2> /root/Dune_fault_linux/faults-in-Linux/faults/results/linuxes/$2/Linux_$1.log > /root/Dune_fault_linux/faults-in-Linux/faults/results/linuxes/$2/Linux_$1.orig.org
elif [ "$1" = "free.cocci" ]
then
	FLAGS2="-D fn=kfree"
        spatch $FLAGS $FLAGS2 -sp_file ./cocci/$1 -dir /root/linuxes/$2 2> /root/Dune_fault_linux/faults-in-Linux/faults/results/linuxes/$2/Linux_$1.log > /root/Dune_fault_linux/faults-in-Linux/faults/results/linuxes/$2/Linux_$1.orig.org
elif [ "$1" = "size.cocci" ]
then
	FLAGS2="-all_includes"
        spatch $FLAGS $FLAGS2 -sp_file ./cocci/$1 -dir /root/linuxes/$2 2> /root/Dune_fault_linux/faults-in-Linux/faults/results/linuxes/$2/Linux_$1.log > /root/Dune_fault_linux/faults-in-Linux/faults/results/linuxes/$2/Linux_$1.orig.org
else
	spatch $FLAGS -sp_file ./cocci/$1 -dir /root/linuxes/$2 2> /root/Dune_fault_linux/faults-in-Linux/faults/results/linuxes/$2/Linux_$1.log > /root/Dune_fault_linux/faults-in-Linux/faults/results/linuxes/$2/Linux_$1.orig.org
fi 


