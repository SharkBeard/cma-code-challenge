import json
import sqlite3
connection = sqlite3.connect('../lib/cma-artworks.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute("SELECT artwork.*, department.name AS department_name, "
               "GROUP_CONCAT(DISTINCT artwork__creator.creator_id) AS creator_ids "
               "FROM artwork "
               "LEFT JOIN artwork__creator "
               "ON artwork.id = artwork__creator.artwork_id "
               "LEFT JOIN artwork__department "
               "ON artwork.id = artwork__department.artwork_id "
               "LEFT JOIN department "
               "ON artwork__department.department_id = department.id "
               "GROUP BY artwork.id"
               )
results = cursor.fetchall()
artworks = [dict(row) for row in results]

cursor.execute("SELECT * FROM creator")
results = cursor.fetchall()
creators = [dict(row) for row in results]

for artwork in artworks:
    if artwork['creator_ids'] is not (None):
        artwork_creator_ids = artwork['creator_ids'].split(',')
        artwork['creators'] = []
        for creator in creators:
            cid = creator['id']
            if cid in artwork_creator_ids:
                artwork['creators'].append({'name': creator['description'], 'role': creator['role']})

with open('../dist/artwork.json', 'w') as output:
    json.dump(artworks, output, sort_keys=True, indent=4)
