py_file=$1
echo "composing $1"
json_file=${py_file/py/json}
echo "creating ${json_file}"
pycompose ${py_file} > ${json_file}
func_name=${py_file/.py/}
echo "deploying" $func_name
pydeploy $func_name $json_file -w