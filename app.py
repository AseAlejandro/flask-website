from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine, text
from keyss import connection_string
from database import hitDB, hitUniqueDB

app = Flask(__name__)

engine = create_engine(connection_string,
                       connect_args={
                            "ssl": {
                                "ssl_ca": "/etc/ssl/cert.pem"
                            }
                       })

# Computers = [
#     {
#         "id": 1,
#         "Salon": "Sala B",
#         "Equipo": "CPU",
#         "Activo": "585800",
#         "No de serie": "2UA1180XZR",
#         "Marca": "HP",
#         "Modelo": "Z200",
#         "Windows": "10",
#         "CPU": "Intel Core i5",
#         "RAM (GB)": "4 GB",
#         "Disco Duro (GB)": "298 GB",
#         "Direccion IP": "148.234.69.80",
#         "Tarjeta de Video": "Nvida Quadro FX380lp"
#     },
#     {
#         "id": 2,
#         "Salon": "Sala B",
#         "Equipo": "CPU",
#         "Activo": "609064",
#         "No de serie": "2UA2250VBJ",
#         "Marca": "HP",
#         "Modelo": "Z210",
#         "Windows": "10",
#         "CPU": "Intel Xeon CPU E31225 3.10 GHz",
#         "RAM (GB)": "4 GB",
#         "Disco Duro (GB)": "466 GB",
#         "Direccion IP": "148.234.69.54",
#         "Tarjeta de Video": "ATI firepro 3800"
#     },
#     {
#         "id": 3,
#         "Salon": "Sala B",
#         "Equipo": "Monitor",
#         "Activo": "609111",
#         "No de serie": "6CM20709ZZ",
#         "Marca": "HP",
#         "Modelo": "HP LV1911",
#     }
# ]

@app.route("/")
def HelloWorld():
    Computers = hitDB()
    return render_template("home.html", computers=Computers)

@app.route("/computers")
def listJobs():
    Computers = hitDB()
    return jsonify(Computers)

@app.route("/computer/<id>")
def showComputer(id):
    computer = hitUniqueDB(id)
    if not computer:
        return "Not Found", 404
    computer = computer[0]

    # return jsonify(computer)
    return render_template("objects.html", computers = computer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)