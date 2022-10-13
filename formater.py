import csv

""" newCSV = open('example2.csv', 'a')



writer = csv.writer(newCSV)
writer.writerows([["URL", "VISTA", "SECCION", "TIME"]])

newCSV.close() """

nombreCSV = "rendimientosegundaversion"
extensionArchivo = ".csv"

datos = []

with open(nombreCSV + extensionArchivo) as csvfile:
    reader = csv.DictReader(csvfile)
    time = 0
    lastTime = 0
    for row in reader:
        if row["URL"] == "Libra":
            time += float(row["TIME"])
            lastTime = float(row["TIME"])
            continue

        if row["URL"] != "Libra" and row["VISTA"] != "grupo":
            if row["SECCION"] == "Permisos":
                datos.append([row["URL"], "getDatosReferencia", "Libra", time])
                datos.append([row["URL"], row["VISTA"], row["SECCION"], row["TIME"]])
                continue
                    
            if row["SECCION"] == "Renderizado":
                row["TIME"] = float(row["TIME"]) - float(time)
                datos.append([row["URL"], row["VISTA"], row["SECCION"], row["TIME"]])
                time = 0
                continue
                
            datos.append([row["URL"], row["VISTA"], row["SECCION"], row["TIME"]])

        if row["VISTA"] == "grupo":
            if row["SECCION"] == "Permisos":
                datos.append([row["URL"], "grupo", "Libra", lastTime])
                datos.append([row["URL"], row["VISTA"], row["SECCION"], row["TIME"]])
                continue
                    
            if row["SECCION"] == "Renderizado":
                row["TIME"] = float(row["TIME"]) - float(lastTime)
                datos.append([row["URL"], row["VISTA"], row["SECCION"], row["TIME"]])
                time = 0
                continue

            datos.append([row["URL"], row["VISTA"], row["SECCION"], row["TIME"]])
        
with open(nombreCSV + "_formateado" + extensionArchivo, 'a') as newCSV:
    writer = csv.writer(newCSV)
    writer.writerows([["URL", "VISTA", "SECCION", "TIME"]])
    writer.writerows(datos)
    newCSV.close()