# commerce-analytics

Repo to do some analysis on a ecommerce customer data

## Running the analysis:

```bash 
python3 main.py
```

## Setting Up:

1. Clone project
```bash
git clone  https://github.com/moeraza/commerce-analytics
```

2. cd into project
```bash 
cd commerce-analytics
```

3. Create Isolated Environment within project folder
```bash 
python3 -m  pip install virtualenv
``` 
```bash
python3 -m virtualenv env
``` 

4. Activate virtualenv
```bash
source env/bin/activate
```

5. Install dependencies 
```bash 
pip3 install -r requirments.txt
```

6. Download all csv data into data/ folder

7. change config.ini to 
```bash
[ANALYSIS]
TEST_MODE=No
``` 