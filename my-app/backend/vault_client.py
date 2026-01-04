# vault_client.py
import os
import hvac

VAULT_ADDR = os.getenv("VAULT_ADDR", "http://vault:8200")
VAULT_TOKEN = os.getenv("VAULT_TOKEN", "root")

_client = None

def get_vault_client():
    global _client
    if _client is None:
        _client = hvac.Client(
            url=VAULT_ADDR,
            token=VAULT_TOKEN
        )
    return _client


def get_db_credentials():
    client = get_vault_client()

    secret = client.secrets.kv.v2.read_secret_version(
        path="db",
        mount_point="secret"
    )

    return secret["data"]["data"]
