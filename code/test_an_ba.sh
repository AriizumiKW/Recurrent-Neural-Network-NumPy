an=5
step=3

for((ba=5;ba<=10;ba=ba+1))
do
	for((an=7;an<=10;an=an+1))
	do
		echo "---------"
		python rnn.py train-lm ../data/ 50 0 0.5 $an $ba --> "$ba:$an:.txt"
		echo $ba
		echo $an
		echo "---------"
	done
done
