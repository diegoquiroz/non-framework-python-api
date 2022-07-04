from .connection import connection


class PropertyRepositoryMySQL:
    def list(**filters) -> list:
        query = '''SELECT p.* FROM property p
            LEFT JOIN (
                select sh.* from status_history sh
                where (sh.update_date, sh.id) = (
                    SELECT MAX(sh2.update_date), MAX(sh2.id)
                    FROM status_history sh2
                    where sh2.property_id = sh.property_id
                )
            )
            AS sh
            ON p.id = sh.property_id
            WHERE sh.status_id in (3,4,5);'''
        cursor = connection.cursor()
        cursor.execute(query)
        properties = []
        __import__('pdb').set_trace()
        for (id, address, city, price, description, year) in cursor:
            properties.append({
                'id': id,
                'address': address,
                'city': city,
                'price': price,
                'description': description,
                'year': year
            })
        return properties
