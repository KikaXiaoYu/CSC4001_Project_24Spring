# set -x

for i in $(seq 1 1000); do
    echo "For gen testing with intep $1, iter $i testing... "

    # generating input.pig
    python3 gen.py

    # interpreting to 1.out and 2.out
    python3 pig.py
    buggy_interpreters/pig$1 <input.pig >2.out

done
