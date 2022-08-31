from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BAB3UueIu2b-OGXXK59auB_unu12bAQoNZ63WHibb6Q6fwUXjIi_zgqtd_Gam7bpxP7eBsmcJtqGE_P8sJEYmdEZ7aGvVxkZYbi_6aEHtvggyUrZelhmjiNfVvkFTTPwBmAvpJeSW5wdmAxDIhUEUdd1cD5t7GXNTcZYpF6LaOb5lnh5u1a2nOc-jYpNWBKbPZQrAdoF8dFSNyfdQoVY14gNF5RL89fWPvYvy_zMflqYbn-v-KiIwlJgnpr3FbAXAEEKHGfrtJ8RlUSEQMaFgvKwZe-mC9pFmIOxZ2Lq2m4HyQWZULIqjjYoegkc8BuSNdNv0CjNEtDuv10ljZ8HmxAuAAAAASwBhrYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5663061406:AAGCk4Yh1UWJBmQFHxuSqeVpBICChXoWxTU")
BOT_NAME = getenv("BOT_NAME", "LionMusicBot") 
API_ID = int(getenv("API_ID", ))
API_HASH = getenv("API_HASH", "7e74b1e22026fcc291d32b3d431aa21e")
BOT_USERNAME = getenv("BOT_USERNAME", "lionmusiccbot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5033264822").split()))
