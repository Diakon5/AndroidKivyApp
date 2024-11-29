schema_sql = list()
schema_version = 1
schema_sql.append("CREATE TABLE schema_meta (version INTEGER PRIMARY KEY)")
schema_sql.append("CREATE TABLE managed_vehicles_list (vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT, vehicle_display_name TEXT)")
schema_sql.append("CREATE TABLE documents (document_id INTEGER PRIMARY KEY AUTOINCREMENT, document_scan_date DATETIME, document_print_date DATETIME, document_sum_cache DECIMAL)")
schema_sql.append("CREATE TABLE document_rows (row_id INTEGER PRIMARY KEY AUTOINCREMENT, document_id INTEGER, purchase_category INT, purchase_name TEXT, purchase_price INT, FOREIGN KEY(document_id) REFERENCES documents(document_id))")


