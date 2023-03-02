from ncclient import manager


router = {"host": "ios-xemgmt-latest.cisco.com", "port": "1000", "username": "developer", "password": "DeezNutz"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"],password=router["password"],hostkey_verify=False) as m:
    m.close_session()