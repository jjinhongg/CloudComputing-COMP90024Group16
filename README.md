# COMP90024 Group16

**Team members:**

- Zenan Ji (Student ID: 1122396) - city: Nanjing

- Weijie Ye (Student ID: 1160818) - city: Fuzhou

- Wenqin Liu (Student ID: 807291) - city: Guangdong

- Jinhong Yong (Student ID: 1198833) - city: Kuala Lumpur

- Zixuan Zeng (Student ID: 1088297) - city: Melbourne

As Twitter is among the most widely used social media platforms in recent days, the analysis of twitter data can reveal societal patterns in cities or countries. Understanding the feeling and distribution of cities is critical for a better understanding and, as a result, a better management strategy and plan for the future. Utilising Cloud computing, this project focuses on the analysis of twitter data across five Australian cities: Adelaide, Brisbane, Canberra, Melbourne and Sydney, visualising data on Total Tweets, Tweet Time Distribution, Sentiment Analysis, Language Distribution, as well as Top-30 Hashtags. Automation of instance creation, management, as well as security group configuration are facilitated by Ansible interacting with the OpenStack API exposed by the Melbourne Research Cloud (MRC). Moreover, deployment of the entire system onto four virtual machines (VMs) on the MRC was also done via Ansible. We containerized all services and applications by harnessing Docker. In regards to data collection, we utilised Tweepy and Aurin. Data and results were then stored in CouchDB databases in the CouchDB cluster. In addition, we have developed a RESTful realtime web application, powered by Flask as the backend, where communication with the frontend is achieved via HTTP GET requests to query data from URLs defined by the backend server running on the MRC instance.

## Git Directory Structure
* `Ansible/mrc` -- Ansible scriptes for depoloying on the MRC.
* `TwitterHarvester/` -- Scripts for continuously retriving tweet data. 
* `data/` -- Analysis and AURIN data related to Languages.  
* `webapp/` -- Scripts for the frontend and backend of the web application.

## 1. Overview of the System Architecture
<img width="944" alt="Screen Shot 2021-05-23 at 18 20 10" src="https://user-images.githubusercontent.com/62043185/119256532-b3079e00-bbf3-11eb-87d0-38d0d6b35060.png">


## 2. Techonology Stack
- automation tool - Ansible
- database - CouchDB Cluster
- data collection - tweepy, AURIN
- data analysis - MapReduce
- webapp - Flask
- [x] All services are deployed using Docker Containers


## 3. Deployment Guide
Make sure you are connecting to the Unimelb AnyConnect VPN even though you are using the campus network. Ansible may hang if being run from the unimelb network without proxy
Clone this repo and change directory to mrc using command 
```
cd Ansible/mrc
```

To deploy, there are two cases:

(1) Create instances and set up remote instances and start the service. 
```
. openrc.sh; ansible-playbook -i inventory/host --extra-var db-action=backup master.yaml
```


(2) Remote instances are all set and only run the service.
```
. openrc.sh; ansible-playbook -i inventory.host --extra-var db-action=backup webapp.yaml
```
