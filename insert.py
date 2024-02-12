import sqlite3
conn = sqlite3.connect('example.db')
print("opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (11, 'FAITH KARIMI',23,345000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (12, 'BOB KURIA',25,445000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (13, 'JANE MUTHONI',57,345000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (14, 'MARY ANNE',23,645000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (15, 'BRIAN MURIMI',74,345000.00)")

conn.commit()
print("Record inserted successfully")
conn.close()