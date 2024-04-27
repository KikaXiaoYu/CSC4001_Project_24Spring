
for i in $(seq 1 1000); do

    # generating input.pig
    echo -n "testing for $i. "
    cat dataflow_cases/xiaoyu_$i.pig > input.pig
    python3 da_wyy.py < input.pig > 1.out

    cat dataflow_cases/xiaoyu_$i.out > 2.out
    diff 1.out 2.out -q
    if [ $? -eq 0 ]; then
        echo "No bug detected."
    else
        echo "Bug is detected during iter $1."
        # echo "$i " >> WuYueYan_res.txt
    fi
done