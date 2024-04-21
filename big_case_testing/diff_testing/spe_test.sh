    # generating input.pig
    cat  inte_cases/xiaoyu_$1.pig > input.pig
    python3 pig_WuYueyan.py
    echo "testing $1"
    cat inte_cases/xiaoyu_$1.out > 11.out
    diff 1.out inte_cases/xiaoyu_$1.out
    if [ $? -eq 0 ]; then
        echo "No bug detected."
    else
        echo "Bug is detected during iter $1."
        # echo "$i " >> WuYueYan_res.txt
    fi
