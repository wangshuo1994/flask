#!/Users/xiaoshanzha/code/mytestgit/flaskvue/backend/venv/bin python
# -*- coding: utf-8 -*-
from flask import Flask, abort, request, render_template, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, send_file, make_response, jsonify
from datetime import datetime, date, timedelta
import json
import mysql.connector

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")

CORS(app)

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, timedelta):
        return str(obj)
    raise TypeError("Type %s not serializable" % type(obj))

@app.route('/data/', methods=['GET'])
def getData():
    indicatorcode = request.args.get('indicatorcode')
    # ave_sum = request.args.get('cal')
    # if ave_sum == None:
    #     ave_sum = 'sum'
    print('indicatorcode',indicatorcode)
    # print('ave_sum', ave_sum)
    response_data = {}

    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='Aa789789',
        database='edstatsDB',
    )

    DEFAULT_QUERY = 'select * from edstatscountry limit 1'
    query = DEFAULT_QUERY


    if indicatorcode != None:
        query = 'select t1.indicatorname, t1.indicatorcode, t2.region, 7 as sum, count(t2.countrycode) as country_cnt,' \
                'sum(`1970`) as sum_1970,sum(`1971`) as sum_1971 ,sum(`1972`) as sum_1972 ,sum(`1973`) as sum_1973 ,sum(`1974`) as sum_1974 ,sum(`1975`) as sum_1975,' \
                'sum(`1976`) as sum_1976 ,sum(`1977`) as sum_1977 ,sum(`1978`) as sum_1978 ,sum(`1979`) as sum_1979 ,sum(`1980`) as sum_1980 ,sum(`1981`) as sum_1981,' \
                'sum(`1982`) as sum_1982 ,sum(`1983`) as sum_1983 ,sum(`1984`) as sum_1984 ,sum(`1985`) as sum_1985 ,sum(`1986`) as sum_1986 ,sum(`1987`) as sum_1987,' \
                'sum(`1988`) as sum_1988 ,sum(`1989`) as sum_1989 ,sum(`1990`) as sum_1990 ,sum(`1991`) as sum_1991 ,sum(`1992`) as sum_1992 ,sum(`1993`) as sum_1993,' \
                'sum(`1994`) as sum_1994 ,sum(`1995`) as sum_1995 ,sum(`1996`) as sum_1996 ,sum(`1997`) as sum_1997 ,sum(`1998`) as sum_1998 ,sum(`1999`) as sum_1999,' \
                'sum(`2000`) as sum_2000 ,sum(`2001`) as sum_2001 ,sum(`2002`) as sum_2002 ,sum(`2003`) as sum_2003 ,sum(`2004`) as sum_2004 ,sum(`2005`) as sum_2005,' \
                'sum(`2006`) as sum_2006 ,sum(`2007`) as sum_2007 ,sum(`2008`) as sum_2008 ,sum(`2009`) as sum_2009 ,sum(`2010`) as sum_2010 ,sum(`2011`) as sum_2011,' \
                'sum(`2012`) as sum_2012 ,sum(`2013`) as sum_2013 ,sum(`2014`) as sum_2014 ,sum(`2015`) as sum_2015 ,sum(`2016`) as sum_2016 ,sum(`2017`) as sum_2017,' \
                'sum(`2020`) as sum_2020 ,sum(`2025`) as sum_2025 ,sum(`2030`) as sum_2030 ,sum(`2035`) as sum_2035 ,sum(`2040`) as sum_2040 ,sum(`2045`) as sum_2045,' \
                'sum(`2050`) as sum_2050 ,sum(`2055`) as sum_2055 ,sum(`2060`) as sum_2060 ,sum(`2065`) as sum_2065 ,sum(`2070`) as sum_2070 ,sum(`2075`) as sum_2075,' \
                'sum(`2080`) as sum_2080 ,sum(`2085`) as sum_2085 ,sum(`2090`) as sum_2090 ,sum(`2095`) as sum_2095 ,sum(`2100`) as sum_2100 ' \
                'from edstatsdata t1 right join edstatscountry t2 on t1.countrycode = t2.countrycode where t1.indicatorcode = "'+indicatorcode+'" and t2.region != "" ' \
                'group by t2.region, t1.indicatorname, t1.indicatorcode'


    # elif indicatorcode != None and ave_sum == 'ave':
    #     query = 'select t1.indicatorname, t1.indicatorcode, t2.region, 7 as ave, count(t2.countrycode) as country_cnt,' \
    #             'avg(`1970`) as avg_1970,avg(`1971`) as avg_1971 ,avg(`1972`) as avg_1972 ,avg(`1973`) as avg_1973 ,avg(`1974`) as avg_1974 ,avg(`1975`) as avg_1975 ,' \
    #             'avg(`1976`) as avg_1976 ,avg(`1977`) as avg_1977 ,avg(`1978`) as avg_1978 ,avg(`1979`) as avg_1979 ,avg(`1980`) as avg_1980 ,avg(`1981`) as avg_1981 ,' \
    #             'avg(`1982`) as avg_1982 ,avg(`1983`) as avg_1983 ,avg(`1984`) as avg_1984 ,avg(`1985`) as avg_1985 ,avg(`1986`) as avg_1986 ,avg(`1987`) as avg_1987 ,' \
    #             'avg(`1988`) as avg_1988 ,avg(`1989`) as avg_1989 ,avg(`1990`) as avg_1990 ,avg(`1991`) as avg_1991 ,avg(`1992`) as avg_1992 ,avg(`1993`) as avg_1993 ,' \
    #             'avg(`1994`) as avg_1994 ,avg(`1995`) as avg_1995 ,avg(`1996`) as avg_1996 ,avg(`1997`) as avg_1997 ,avg(`1998`) as avg_1998 ,avg(`1999`) as avg_1999 ,' \
    #             'avg(`2000`) as avg_2000 ,avg(`2001`) as avg_2001 ,avg(`2002`) as avg_2002 ,avg(`2003`) as avg_2003 ,avg(`2004`) as avg_2004 ,avg(`2005`) as avg_2005 ,' \
    #             'avg(`2006`) as avg_2006 ,avg(`2007`) as avg_2007 ,avg(`2008`) as avg_2008 ,avg(`2009`) as avg_2009 ,avg(`2010`) as avg_2010 ,avg(`2011`) as avg_2011 ,' \
    #             'avg(`2012`) as avg_2012 ,avg(`2013`) as avg_2013 ,avg(`2014`) as avg_2014 ,avg(`2015`) as avg_2015 ,avg(`2016`) as avg_2016 ,avg(`2017`) as avg_2017 ,' \
    #             'avg(`2020`) as avg_2020 ,avg(`2025`) as avg_2025 ,avg(`2030`) as avg_2030 ,avg(`2035`) as avg_2035 ,avg(`2040`) as avg_2040 ,avg(`2045`) as avg_2045 ,' \
    #             'avg(`2050`) as avg_2050 ,avg(`2055`) as avg_2055 ,avg(`2060`) as avg_2060 ,avg(`2065`) as avg_2065 ,avg(`2070`) as avg_2070 ,avg(`2075`) as avg_2075 ,' \
    #             'avg(`2080`) as avg_2080 ,avg(`2085`) as avg_2085 ,avg(`2090`) as avg_2090 ,avg(`2095`) as avg_2095 ,avg(`2100`) as avg_2100, ' \
    #             'from edstatsdata t1 right join edstatscountry t2 on t1.countrycode = t2.countrycode where t1.indicatorcode = "'+indicatorcode+'" ' \
    #             'group by t2.region, t1.indicatorname, t1.indicatorcode'
    #     print('query', query)



    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    response_data["body"] = data
    response_data["status"] = "200"

    return make_response(json.dumps(response_data, default=json_serial))

tasks = [1,2,3,4,5]

@app.route('/add_task/', methods=['POST'])
def add_task():
    if not request.json or 'id' not in request.json or 'info' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'info': request.json['info']
    }
    tasks.append(task)
    return jsonify({'result': 'success'})


@app.route('/get_task/', methods=['GET'])
def get_task():
    if not request.args or 'id' not in request.args:
        return jsonify(tasks)
    else:
        task_id = request.args['id']
        task = filter(lambda t: t['id'] == int(task_id), tasks)
        return jsonify(task) if task else jsonify({'result': 'not found'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)