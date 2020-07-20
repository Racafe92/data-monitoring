from flask_restx import Namespace, Resource
from flask import request, Response
from werkzeug.datastructures import FileStorage
from bson import json_util
import werkzeug
import io
import csv
import datetime
import re
from setup import db

api = Namespace('Data Monitoring',
                description='Insert and fetch data from monitoring reports csv files')

# Parser for File Import
data_file_parser = api.parser()
data_file_parser.add_argument(
    'file', type=FileStorage, required=True, location='files')

# Extensions allowed for file with data
ALLOWED_EXTENSIONS = {'csv'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@api.route('/', endpoint='data-monitoring')
class DataMonitoring(Resource):
    def get(self):
        data = db.db.data.find()
        response = json_util.dumps(data)
        return Response(response, mimetype='application/json')

    @api.expect(data_file_parser)
    @api.doc(params={'file': 'A CSV file to parse into Database'})
    def post(self):
        if 'file' not in request.files:
            raise(FileException)
        content = request.files['file']
        if content.filename == '' or not allowed_file(content.filename):
            raise(FileException)
        stream = io.StringIO(
            content.stream.read().decode("UTF-8"), newline=None)
        csv_reader = csv.DictReader(stream)
        digested_csv = []
        for row in csv_reader:
            row['Date'] = str(datetime.datetime.timestamp(
                datetime.datetime.strptime(row['Date'], '%d %b %Y %H:%M:%S')))
            rowkeys = list(row.keys())
            for key in rowkeys:
                row[str.lower(str.strip(re.sub(r'\(.*\)', '', key))
                              ).replace(" ", "_")] = row.pop(key)
            digested_csv.append(row)
        db.db.drop_collection("data")
        db.db.data.insert_many(digested_csv)
        return "{message: ok, status: 200}"


class FileException(werkzeug.exceptions.BadRequest):
    description = 'File not CSV'


@api.errorhandler(FileException)
def handle_file_exception(error):

    return{'message': 'File Error. Make sure the file is attached and is in CSV format'}, 400
