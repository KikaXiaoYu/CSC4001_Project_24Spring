for j in $(seq 2 3); do
    for i in $(seq 1 100); do
        python3 gen_meta.py
        buggy_interpreters/pig$j.exe <input1.pig >1.out
        buggy_interpreters/pig$j.exe <input2.pig >2.out
        python3 pig_formeta.py

        python3 checker.py
        echo -n "successfully do iter $i for inte $j, the check result "
        cat res.out

        diff 1.out 11.out -q

        # if [ $? -eq 0 ]; then
        #     echo "Varified 1: No bug detected."
        # else
        #     echo "Varified 1: Bug is detected during iter $i."
        # fi

        diff 2.out 22.out -q

        # if [ $? -eq 0 ]; then
        #     echo "Varified 2: No bug detected."
        # else
        #     echo "Varified 2: Bug is detected during iter $i."
        # fi
    done
done
