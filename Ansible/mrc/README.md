# cd Ansible/mrc
. openrc.sh; ansible-playbook -i hosts master.yaml

# connect to instances
ssh -i cloud.key ubuntu@172.26.131.217

# hosts
server1: 172.26.133.205 
server2: 172.26.133.212 
server3: 172.26.131.34 
server4: 172.26.133.109 

# change directory to where cloud.key in
# cd Ansible/mrc
# Connect to instances
# 172.26.133.109
# ssh -i cloud.key ubuntu@172.26.133.109
# 172.26.131.34
# 怎么解决就是 删掉重新连接
# ssh -i cloud.key ubuntu@172.26.131.34
# 172.26.133.212
# ssh -i cloud.key ubuntu@172.26.133.212
# 172.26.133.205
# ssh -i cloud.key ubuntu@172.26.133.205