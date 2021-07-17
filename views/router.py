from flask import Flask

from views import handlers


def install(app: Flask):
    app.add_url_rule(
        '/file/<string:file_name>/',
        view_func=handlers.SendFileView().as_view('file')
    )
    app.add_url_rule(
        '/get-data/',
        view_func=handlers.GetDataView().as_view('get-data')
    )
