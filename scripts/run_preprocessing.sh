mkdir ../output
mkdir ../parsed_data
mkdir ../tables

cd parse_data

for f in *.py; do
    python -W ignore $f
done
#Create aux data gets all cites from pubmeds and dois
#Analyze data does most of the job
cd ../analyze_data/
bash analyze_data.sh

#Just check things
cd ../support/
python check_activities.py
python review_tree.py

#Create tables
cd ../create_tables
bash create_tables.sh