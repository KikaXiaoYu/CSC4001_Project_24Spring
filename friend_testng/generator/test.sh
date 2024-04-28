for i in $(seq 1 1000); do
    echo "testing for $i"
    python gen_wyy.py >output_log.txt
    python pig_xzy.py

done
