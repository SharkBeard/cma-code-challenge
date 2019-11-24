import json
import sqlite3
connection = sqlite3.connect('../lib/cma-artworks.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute("SELECT artwork.*, department.name AS department, "
               "creator.role AS creator_role, creator.description AS creator_description "
               "FROM artwork "
               "LEFT JOIN artwork__creator "
               "ON artwork.id = artwork__creator.artwork_id "
               "LEFT JOIN creator "
               "ON artwork__creator.creator_id = creator.id "
               "LEFT JOIN artwork__department "
               "ON artwork.id = artwork__department.artwork_id "
               "LEFT JOIN department "
               "ON artwork__department.department_id = department.id"
               )
results = cursor.fetchall()

results = [dict(row) for row in results]
print(json.dumps(results, sort_keys=True, indent=4))
