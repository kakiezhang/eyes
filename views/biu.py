# -*- encoding: utf8 -*-

from application import app
from flask import render_template, url_for

@app.route("/detail/")
def detail() :
    # timepoint = {
    #     "1412391780",
    #     "1412391840",
    #     "1412391900",
    #     "1412391960",
    #     "1412392020",
    #     "1412392080",
    # }
    return render_template("detail.html")

@app.route("/load/avg/")
def loadavg() :
    load_avg_path = "%s/%s" % (app.config["MINT_LOCATION"], app.config["LOAD_FNAME"])
    cpu_use_path = "%s/%s" % (app.config["MINT_LOCATION"], app.config["CPU_FNAME"])
    loads_input = open(load_avg_path, "r")
    if loads_input is not None :
        loads = loads_input.readline()
    cpus_input = open(cpu_use_path, "r")
    if cpus_input is not None :
        cpus = cpus_input.readline()

    data = {
        "loads": loads,
        "cpus": cpus,
    }

    return render_template("loadavg.html", data = data)

