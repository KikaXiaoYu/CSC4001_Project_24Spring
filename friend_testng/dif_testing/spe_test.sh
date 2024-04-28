    # generating input.pig
    cat  inte_cases/xiaoyu_$2.pig > input.pig
    python3 pig_$1.py
    echo "testing $2"
    cat inte_cases/xiaoyu_$2.out > 11.out
    diff 1.out inte_cases/xiaoyu_$2.out
    if [ $? -eq 0 ]; then
        echo "No bug detected."
    else
        echo "Bug is detected during iter $2."
        # echo "$i " >> WuYueYan_res.txt
    fi
