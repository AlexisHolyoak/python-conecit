import MySQLdb
DB_HOST ="localhost"
DB_USER ="root"
DB_PASS ="1234"
DB_NAME ="Usuarios"

def run_query(query =""):
	datos =[DB_HOST,DB_USER,DB_PASS,DB_NAME]
	conn = MySQLdb.connect(*datos)
	cursor = conn.cursor()
	cursor.execute(query)

	if query.upper().startswith("SELECT"):
		data=cursor.fetchall() #trae resultados
	elif query.upper().startswith("INSERT"):
		conn.commit()
		data= cursor.lastrowid()
	else:
		conn.commit()
		data=True
	cursor.close()
	conn.close()

	return data	