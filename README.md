
# Pessato

A web app designed to order food online from PESU Cafeteria

# Installation

- Dependencies : 

```bash
pip install flask mysql-connector-python twilio python-dotenv Flask-Session fpdf
```

- SQL :
    - Create a database named `pessato`
    ```bash
    create database pessato;
    ```
    - Import sqldump : 
    ```bash
    mysql -u <USERNAME> -p pessato < pessato_data.sql
    ```
- Python :
    - add a dotenv file with required 
## Deployment

To deploy this project run

```bash
  python3 app.py
```


## Demo

![](https://github.com/typicallhavok/Pessato/blob/main/pessato-demo.gif)

