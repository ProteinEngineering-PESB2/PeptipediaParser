cd parse_data
for f in *.py; do
    echo $f
    python $f
done
cd ..
python merge_all.py
python summary.py
python create_tables.py
echo "READY"