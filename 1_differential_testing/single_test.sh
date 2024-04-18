# set -x

for i in $(seq 1 100); do
    echo ""
    echo "For buggy interp $1, iter $i testing... "

    # generating input.pig
    python3 gen.py

    # interpreting to 1.out and 2.out
    python3 pig.py
    buggy_interpreters/pig$1 <input.pig >2.out

    diff 1.out 2.out -q

    if [ $? -eq 0 ]; then
        echo "No bug detected."
    else
        echo "Bug is detected during iter $i."
    fi

done
