from .connection import connection


class PropertyRepositoryMySQL:
    def list(**filters) -> list:
        query = '''SELECT p.*, sh.status_id as status FROM property p
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
            WHERE sh.status_id in (3,4,5)'''
        if filters:
            for filter in filters:
                if filter == 'limit':
                    query += f' LIMIT {filters[filter]}'
                else:
                    query += f' AND {filter}={filters[filter]}'
        cursor = connection.cursor()
        cursor.execute(query)
        properties = []
        for (id, address, city, price, description, year, status) in cursor:
            properties.append({
                'id': id,
                'address': address,
                'city': city,
                'price': price,
                'description': description,
                'year': year,
                'status': status
            })
        return properties
