# set -x

for i in $(seq 1 1000); do

    # generating input.pig
    cat  inte_cases/xiaoyu_$i.pig > input.pig
    python3 pig_WuYueyan.py
    echo "testing $i"
    diff 1.out inte_cases/xiaoyu_$i.out
    if [ $? -eq 0 ]; then
        echo "No bug detected."
    else
        echo "Bug is detected during iter $i."
        echo "$i " >> WuYueYan_res.txt
    fi

done
