#!/bin/bash
source ./list.sh
PASSWORD=ars%^*8421.

check_gpu_power() {
	echo  "================= $1 reboot start ==============="
	sshpass -p $2 ssh -o StrictHostKeyChecking=no  root@$1  "reboot"
	echo  "================ $1 reboot finish done ================="
}

check_all() {

	for host in "${HOSTS[@]}"
	do
#		check_data_power $host $PASSWORD
		check_gpu_power $host $PASSWORD &
	done
	wait
}
check_all

