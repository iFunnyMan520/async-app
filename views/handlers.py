import asyncio
from time import sleep

from flask import send_from_directory, jsonify
from flask.views import MethodView
from coroutines import get_data


class SendFileView(MethodView):
    def get(self, file_name: str):
        sleep(3)
        return send_from_directory('data', file_name)


class GetDataView(MethodView):
    def get(self):
        response = asyncio.run(get_data())
        return jsonify(response)
