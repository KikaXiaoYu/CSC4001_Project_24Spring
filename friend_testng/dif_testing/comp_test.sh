# set -x
echo "" > $1_res.txt
for i in $(seq 1 1000); do

    # generating input.pig
    cat  inte_cases/xiaoyu_$i.pig > input.pig
    python3 pig_$1.py
    echo -n "testing $i: "
    diff 1.out inte_cases/xiaoyu_$i.out -q
    if [ $? -eq 0 ]; then
        echo "No bug detected."
    else
        echo "Bug is detected during iter $i."
        echo "$i " >> $1_res.txt
    fi

done


