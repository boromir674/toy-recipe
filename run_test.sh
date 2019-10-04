
python -m pip install tox

res=$(add-two 2 4)
if [[ "$res" == "6" ]]; then
    exit 0
fi
exit 1
