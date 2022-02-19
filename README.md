# commerce-analytics

Repo to do some analysis on a ecommerce customer data
## Setting Up:

Clone project
```bash
git clone  https://github.com/sendwyre/commerce-analytics.git 
```

cd into project
```bash 
cd commerce-analytics
```

Create Isolated Environment within project folder
```bash 
python3 -m  pip install virtualenv
``` 
```bash
python3 -m virtualenv env
``` 

Activate virtualenv
```bash
source env/bin/activate
```

Install dependencies 
```bash 
pip3 install -r requirments.txt
```

## Running the tool:

```bash 
python3 main.py
```

## Testing the code:
```bash 
pytest test/*
```
