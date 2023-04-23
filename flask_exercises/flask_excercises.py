from flask import Flask, request


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.
    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422
    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200
    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200
    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        dict_user = {}


        @app.route("/user", methods=["POST"])
        def create_user():
            data = request.json
            if data.get('name'):
                dict_user[data['name']] = {}
                return {"data": f"User {data.get('name')} is created!"}, 201

            return {"errors": {"name": "This field is required"}}, 422


        @app.route("/user/<name>", methods=["GET"])
        def get_user(name):
            if name in dict_user:
                return {"data": f"My name is {name}"}, 200

            return "User not found", 404


        @app.route("/user/<name>", methods=["PATCH"])
        def update_user(name):
            new_name = request.json.get('name')
            if name in dict_user:
                dict_user[new_name] = dict_user[name]
                del dict_user[name]
                return {"data": f"My name is {new_name}"}, 200


        @app.route("/user/<name>", methods=["DELETE"])
        def delete_user(name):
            if name in dict_user:
                del dict_user[name]
                return '', 204

            return "User not found", 404
