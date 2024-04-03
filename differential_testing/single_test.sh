set -x 
cat "interp_examples/e$1.pig" > "input.pig"
cat "interp_examples/e$1.out" > "output.out"

python pig.py
diff "output.out" "1.out"
