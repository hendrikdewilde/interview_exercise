import pytz

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

USER_TYPE = (("Admin", "Admin"),
             ("API", "API"),
             ("Web", "Web"),
             ("System", "System"),
             )

NETWORK_TYPE = (("STD", "STD"),
                ("EN", "EN"),
                ("CN", "CN"),
                )

CONNECTION_TYPE = (("FTP", "FTP"),
                   ("SFTP", "SFTP"),
                   ("REST", "REST"),
                   ("SOAP", "SOAP"),
                   )

FLOW_DIRECTION = (("X", "X"),
                  ("I", "I"),
                  )
