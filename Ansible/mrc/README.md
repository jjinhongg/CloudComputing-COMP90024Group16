# Ansible
###### Desciption of YAML files

 - *master.yaml* includes mrc.yaml, remote-setup.yaml and couchdb.yaml
 - *mrc.yaml* creates instances with necessary security groups, voulmes attached
 - *remote-setup.yaml* sets up all necesary proxy and docker proxy, install docker and also mount volumes in all instances
 - *couchdb.yaml* creates couchdb clusters using docker containers
 - *spider.yaml* running twitter harvester and data analysis using docker containers
 - *webapp.yaml* running our web service using docker containers

###### How to run the playbook
```
cd Ansible/mrc
. openrc.sh; ansible-playbook -i inventory/hosts master.yaml
```

###### How to connect to instances
```
cd Ansible/mrc
ssh -i cloud.key ubuntu@172.26.133.205 
```

###### Hosts and associated attached volumes
1. server1: 172.26.133.205 
 - persistent on /dev/vdc 
 - db_1 on /dev/vdb
2. server2: 172.26.133.212
 - db_2 on /dev/vdb 
3. server3: 172.26.131.34 
 - db_3 on /dev/vdb 
4. server4: 172.26.133.109 
 - db_4 on /dev/vdb 
