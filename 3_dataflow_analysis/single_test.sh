set -x 
cat "dataflow_example/test$1.pig" > "input.pig"

python da.py < input.pig > dataflow_example/selfres$1.out

cat "dataflow_example/selfres$1.out" > "selfres.out"
