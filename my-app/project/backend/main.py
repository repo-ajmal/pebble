from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from vault_client import get_db_credentials

app = FastAPI()

# CORS (HTML frontend or React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for local testing
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db_connection():
    creds = get_db_credentials()

    return psycopg2.connect(
        host=creds["host"],
        port=int(creds["port"]),
        database=creds["database"],
        user=creds["user"],
        password=creds["password"],
 
   )
@app.get("/search")
def search_item(name: str = Query(...)):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT name, description FROM items WHERE name = %s",
        (name,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if not row:
        return {"error": f"No record found for '{name}'"}

    return {
        "name": row[0],
        "description": row[1]
    }

