

for i in $(seq 1 100); do

    # generating input.pig
    python3 gen_my.py
    # cat input.pig > dataflow_cases/xiaoyu_$i.pig

    # interpreting to 1.out
    python3 da.py < input.pig > output.out
    echo -n "$i: "
    cat output.out
    echo 

    # python3 da.py < input.pig
    # cat output.out > dataflow_cases/xiaoyu_$i.out
done


# for i in $(seq 101 1000); do

#     # generating input.pig
#     python3 gen_bug.py
#     cat input.pig > dataflow_cases/xiaoyu_$i.pig

#     # interpreting to 1.out
#     python3 da.py < input.pig > output.out
#     echo -n "$i: "
#     cat output.out
#     echo 
#     # python3 da.py < input.pig
#     cat output.out > dataflow_cases/xiaoyu_$i.out
# done
