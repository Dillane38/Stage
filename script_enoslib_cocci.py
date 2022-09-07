import logging
from pathlib import Path
import enoslib as en
from enoslib.api import run_command, actions

en.init_logging(level=logging.DEBUG)
job_name = Path(__file__).name
network = en.G5kNetworkConf(type="kavlan", roles=["my_network"], site="grenoble")

conf = (

        en.G5kConf.from_settings(job_name="cocci-par" , env_name="https://api.grid5000.fr/sid/sites/grenoble/public/bmahan/update_cocci_version_13.yaml", job_type="deploy" ,force_deploy=True ,walltime="03:00:00")
        .add_network_conf(network)
        .add_machine(

                        roles=["noeud1"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

                        roles=["noeud2"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

                        roles=["noeud3"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

                        roles=["noeud4"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

                        roles=["noeud5"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

                        roles=["noeud6"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

                        roles=["noeud7"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

                        roles=["noeud8"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

                        roles=["noeud9"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

                        roles=["noeud10"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

                        roles=["noeud11"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

                        roles=["noeud12"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

                        roles=["noeud13"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

                        roles=["noeud14"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

                        roles=["noeud15"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

                        roles=["noeud16"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

                        roles=["noeud17"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )


        .add_machine(

            roles=["noeud18"],

            site="grenoble",

            cluster="dahu",

            nodes=1,

            primary_network=network,

        )
        .finalize()

)

provider = en.G5k(conf)
roles , networks = provider.init(True)


with actions(pattern_hosts="all", roles=roles) as p:
       p.shell("cp ~/linuxes/script_parrallele.sh  ~/Dune_fault_linux/faults-in-Linux/faults")
       p.shell("chmod +x  ~/Dune_fault_linux/faults-in-Linux/faults/script_parrallele.sh")
       p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && make && make init")
       p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && cp /usr/local/share/herodotos/Makefile.prj ./results/linuxes/Makefiile")


for i in range(6,8):
    with actions(pattern_hosts="noeud1" , strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh ret6.cocci linux-5.1{}".format(i))

    with actions(pattern_hosts="noeud2" , strategy="free",  background=True, roles=roles) as p:
         p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh null_ref6.cocci linux-5.1{}".format(i))

    with actions(pattern_hosts="noeud3" ,strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh realloc.cocci linux-5.1{}".fomat(i))

    with actions(pattern_hosts="noeud4" ,  strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh lock.cocci linux-5.1{}".format(i))

    with actions(pattern_hosts="noeud5" ,  strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh intr.cocci linux-5.1{}".format(i))

    with actions(pattern_hosts="noeud6" ,  strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh lockintr.cocci linux-5.1{}".format(i))

    with actions(pattern_hosts="noeud7" ,  strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh intr_noarg.cocci linux-5.1{}".format(i))

    with actions(pattern_hosts="noeud8" ,  strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh noderef.cocci linux-5.1{}".format(i))

    with actions(pattern_hosts="noeud9" ,  strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh free.cocci linux-5.1{}".format(i))

    with actions(pattern_hosts="noeud10" ,  strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh var.cocci linux-5.1{}".format(i))

    with actions(pattern_hosts="noeud11" ,  strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh block1a.cocci linux-5.1{}".format(i))

    with actions(pattern_hosts="noeud12" ,  strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh block1b.cocci linux-5.1{}".format(i))

    with actions(pattern_hosts="noeud13" ,  strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh block1c.cocci linux-5.1{}".format(i))

    with actions(pattern_hosts="noeud14" ,  strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh get.cocci linux-5.1{}".format(i))

    with actions(pattern_hosts="noeud15" ,  strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh copy.cocci linux-5.1{}".format(i))

    with actions(pattern_hosts="noeud16" ,  strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh size.cocci linux-5.1{}".format(i))

    with actions(pattern_hosts="noeud17" ,  strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh double_lock2.cocci linux-5.1{}".format(i))

    with actions(pattern_hosts="noeud18" ,  strategy="free", background=True, roles=roles) as p:
        p.shell("cd ~/Dune_fault_linux/faults-in-Linux/faults && ./script_parrallele.sh double_lockintr2.cocci linux-5.1{}".format(i))

with actions(pattern_hosts="all" , strategy="free",  roles=roles) as p:
    p.shell("cp -r ~/Dune_fault_linux/faults-in-Linux/faults/results ~/linuxes")


