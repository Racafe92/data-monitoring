from flask_restx import Namespace, Resource
from flask import request
from werkzeug.datastructures import FileStorage
import io
import csv
import datetime
import re
from setup import db

api = Namespace('Data Monitoring',
                description='Insert and fetch data from monitoring reports csv files')

# Parser for File Import
data_file_parser = api.parser()
data_file_parser.add_argument('file', type=FileStorage, required=True, location='files')

@api.route('/', endpoint='data-monitoring')
class DataMonitoring(Resource):
    def get(self):
        return "API ok"

    def post(self):
        content = request.files['file']
        stream = io.StringIO(content.stream.read().decode("UTF-8"), newline = None)
        csv_reader = csv.DictReader(stream)
        digested_csv = []
        for row in csv_reader:
            row['Date'] = str(datetime.datetime.timestamp(datetime.datetime.strptime(row['Date'], '%d %b %Y %H:%M:%S')))
            rowkeys=list(row.keys())
            for key in rowkeys:
                row[str.lower(str.strip(re.sub(r'\(.*\)', '', key))).replace(" ", "_")] = row.pop(key)
            digested_csv.append(row)
        db.db.drop_collection("data")
        db.db.data.insert_many(digested_csv)
        return "{message: ok, status: 200}"