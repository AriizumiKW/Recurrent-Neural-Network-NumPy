an=5
step=3

for((ba=25;ba<=75;ba=ba+25))
do
	for((an=4;an<=10;an=an+1))
	do
		echo "---------"
		val=`expr $ba + $an`
		python rnn.py train-lm ../data/ 50 0 0.5 $an $ba --> "$val:.txt"
		echo $ba
		echo $an
		echo "---------"
	done
done
