set -x 
cat "dataflow_example/$1.pig" > "input.pig"

python da.py < input.pig > dataflow_example/$1.out

cat "dataflow_example/$1.out" > "output.out"
