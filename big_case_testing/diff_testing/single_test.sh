# set -x

for i in $(seq 1 1000); do

    # generating input.pig
    python3 gen.py
    cat input.pig > inte_cases/xiaoyu_$i.pig

    # interpreting to 1.out
    python3 pig.py
    cat 1.out > inte_cases/xiaoyu_$i.out
done
