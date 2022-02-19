# commerce-analytics

Repo to do some analysis on a ecommerce customer data
## Setting Up:

1. Clone project
```bash
git clone  https://github.com/sendwyre/commerce-analytics.git 
```

1. cd into project
```bash 
cd commerce-analytics
```

1. Create Isolated Environment within project folder
```bash 
python3 -m  pip install virtualenv
``` 
```bash
python3 -m virtualenv env
``` 

1. Activate virtualenv
```bash
source env/bin/activate
```

1. Install dependencies 
```bash 
pip3 install -r requirments.txt
```

1. Download all csv data into data/ folder


## Running the tool:

```bash 
python3 main.py
```

## Testing the code:
```bash 
pytest test/*
```
