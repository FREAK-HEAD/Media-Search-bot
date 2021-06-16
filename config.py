import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "4064460"))
    API_HASH = os.environ.get("API_HASH", "1ec640d5d326c11742dcc38025fc52b5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1858646441:AAE_eFvfwINjWrsOCi26Oim0Fw75DBl5Ogc") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "1752711364")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Erichdaniken:Erichdaniken@cluster0.a7wex.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "1AZWarzsBu6Ek1NBKvB-V1yaVRYk7D50qiK4sroKuutqrk8FjJPgFKmKEbTdQbAi91WBNEg4iHMYeYMpIrdEiI39HVCzV4cmcVDWIDd0ryDwDqMIZs9uMd44kB4-w0ZdAt46l4BJ7SCH-tbkyzgzZQWZ3wloKTA7HdaRyZYVxIGxe4gGBRw1gpAPvbmmdyQutgQzu92oS6Txab4D4wRWbUrBVvhk_3TS-BeqCVDkpBazs-alRcxbOs4dGv962cyS3a-E4abATdTeRESUw4v-M6TpllBJWlp9LsJ8KPbjpP14Z5U_CulTpeHF1Xu8epe4bufDsLBhZIaxvyK2fFZZEjpP3qE9BSWE=")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001180843317"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "testMirror_aria_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
