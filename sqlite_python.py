import sqlite3
verbindung = sqlite3.connect("geburtstage.db")
zeiger = verbindung.cursor()
 
# Create Table
create_table = "CREATE TABLE IF NOT EXISTS personen (vorname TEXT, nachname TEXT, geburtstag DATE )"
zeiger.execute(create_table)
verbindung.commit()

# Insert many values
insert_into = "INSERT INTO personen VALUES(?,?,?)"
contents = [('Mischa', 'Haenen', '23.10.97'), ('Timon', 'Galeazzi', '01.01.2022'), ('Johann Wolfgang', 'von Goethe', '28.8.1749'), ('Hanelore', 'Fridli', '01.03.69')]
zeiger.executemany(insert_into, contents)
verbindung.commit()

# Update entry
zeiger.execute("UPDATE personen SET vorname='Aschi' WHERE nachname='Galeazzi'")
verbindung.commit()

# Delete entry
zeiger.execute("DELETE FROM personen WHERE nachname=?", ('Haenen',))
verbindung.commit()

# Show entries
''' for row in zeiger.execute('SELECT * FROM personen'):
        print(row) '''
        
# DROP TABLE 
drop_table = "DROP TABLE personen"
zeiger.execute(drop_table)
verbindung.commit()

verbindung.close()


verbindung = sqlite3.connect("company.db")
zeiger = verbindung.cursor()
personen_table = "CREATE TABLE IF NOT EXISTS personen(name TEXT, vorname TEXT, personalnummer INTEGER PRIMARY KEY, gehalt REAL, geburtstag TEXT)"
zeiger.execute(personen_table)
verbindung.commit()
# Create persons
insert_into = "INSERT INTO personen VALUES(?,?,?,?,?)"
personen = [
    ('Maier','Hans',6714,3500.00,'15.03.62'),
    ('Schmitz','Peter',81343,3750.00,'12.04.58'),
    ('Mertens','Julia',2297,3621.50,'30.12.59')]

zeiger.executemany(insert_into, personen)

# Show entries
#for row in zeiger.execute("SELECT * FROM personen WHERE name = 'Schmitz'"):
#for row in zeiger.execute("SELECT * FROM personen WHERE gehalt >= 3600 AND gehalt <= 3650"):
for row in zeiger.execute('SELECT * FROM personen WHERE gehalt > 3600'):
        print(row)
        
# Like
#for row in zeiger.execute("SELECT * FROM personen WHERE name LIKE '%M%' OR name LIKE '%m%' OR vorname LIKE '%M%' OR vorname LIKE '%m%'"):
#for row in zeiger.execute("SELECT * FROM personen WHERE name LIKE 'M%' AND name LIKE '%er'"):
for row in zeiger.execute("SELECT * FROM personen WHERE name LIKE '%i%' OR vorname LIKE '%i%'"):
    print(row)
# Sort
#for row in zeiger.execute("SELECT gehalt FROM personen DESC"):
for row in zeiger.execute("SELECT name, vorname FROM personen ASC"):
    print(row)
# DROP Table
zeiger.execute("DROP TABLE personen")
verbindung.commit()

verbindung.close()