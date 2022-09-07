import logging
from pathlib import Path
import enoslib as en
from enoslib.api import run_command, run_ansible
import json

en.init_logging(level=logging.DEBUG)
job_name = Path(__file__).name
network = en.G5kNetworkConf(type="kavlan", roles=["my_network"], site="grenoble")

conf = (

        en.G5kConf.from_settings(job_name="cocci-par" , env_name="https://api.grid5000.fr/sid/sites/grenoble/public/bmahan/update_cocci_version_12.yaml", job_type="deploy" ,force_deploy=True ,walltime="03:00:00")
        .add_network_conf(network)
        .add_machine(

                        roles=["noeud1"], site="grenoble", cluster="dahu", nodes=1 ,primary_network=network

        )

        .add_machine(

            roles=["noeud2"],

            site="grenoble",

            cluster="dahu",

            nodes=1,

            primary_network=network,

        )
        .finalize()

)

provider = en.G5k(conf)
roles , networks = provider.init(True)

run_ansible(["script_ansible.yml"], roles=roles)












#result1 = run_command("cd linuxes && less script_parrallele.sh",pattern_hosts="control1", roles=roles)

#result2 = run_command("ls -al",pattern_hosts="control2", roles=roles)



#result1 = run_command("chmod +x script_parrallele.sh && sh ~/script_parallele.sh ~/coccinelle/scripts/coccicheck/cocci/badzero.cocci ~/linuxes/result.index.linux-1.1.23", pattern_hosts="control1", roles=roles)

#with actions(pattern_hosts="control2", roles=roles) as p:
    #p.shell("cd ~")
    #p.shell("hostname")
    #p.shell("ssh root@dahu-7.grenoble.grid5000.fr && ls")
    #p.shell("sh ~/script_parrallele.sh ~/coccinelle/scripts/coccichek/cocci/malloc.cocci ~/linuxes/result.index.linux-1.1.23")

#result2 = run_command("chmod +x script_parrallele.sh && sh ~/script_parrallele.sh ~/coccinelle/scripts/coccicheck/cocci/malloc.cocci ~/linuxes/result.index.linux-1.1.23", pattern_hosts="control2", roles=roles)

#with open('result_ok_noeud_{}'.format(result1.to_dict()[0]["host"]), 'w') as f:
       # f.write(result1.to_dict()[0]["stdout"])

#with open('result_ok_noeud_{}'.format(result2.to_dict()[0]["host"]), 'w') as f:
        #f.write(result2.to_dict()[0]["stdout"])

