# nagios

Collection of Nagios plugins for EOS.

#### To-DO

* Allow for check_fork function to read hosts from file.


####  📌 check_bp.py


A python script to monitor your Block Producers using nagios or other.
Each function performs a particular action and EXITS with 0 if there are no issues and EXITS with 2 if there are issues. 




#####  (1) Check the head_block_num of your producer is incrementing 

* Checks your host's head_block_num and saves that as a varaible, waits 5 secodns and checks again.
* EXITS with 0 if head_block_num has incremented. 
* EXITS with 2 if head_block_num has not incremented. 

###### Usage for check_head
`check_bp.py  x.x.x.x:8888 check_head`

#####  (2) Check whether producer is paused


###### Usage for check_head
`check_bp.py  x.x.x.x:8888 check_paused


####  📌 check_producing.sh

* Checks the producer list and records your unpaid_blocks integer an saves to a file.
* Re-Checks the producer list and checks whewther number has increased. 

###### Usage 
`check_producing.sh`


####  📌 check_last_claim.sh

* Checks the last time your producer claimedrewards and ensures the value is not > 24 hours.

###### Usage 
`check_last_claim.sh`

####  📌 check_history.sh

* Checks whether your BASH history contains any EOS wallet passwords OR Private keys.

###### Usage 
`check_history.sh`

####  📌 zfs_backup.sh

* Checks whether your ZFS snapshots contain a recent snapshot.

###### Usage 
`zfs_backup.sh`


####  📌 check_account_ram.sh

* Checks teh RAM usage for an account on chain and alerts if current usage is over $MAX variable.

####  📌 account-cpu.sh

* Checks CPU usage of account over 60 seconds period and compares average to $MAX variable, if higher it alerts.

