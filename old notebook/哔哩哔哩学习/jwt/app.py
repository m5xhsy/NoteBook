from flask import Flask, jsonify, request

import datetime

app = Flask(__name__)

import jwt
from jwt import exceptions


@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("username")
    pswd = request.form.get("password")
    print(user, pswd)
    if user == "m5xhsy" and pswd == "Ass078678":
        salt = "a5sd56a4sd65asd"
        headers = {
            "typ": "jwt",
            "alg": "HS256"
        }
        payload = {
            "user_id": 1,
            "nickname": "屁屁",
            "iat": datetime.datetime.now() + datetime.timedelta(seconds=20)
        }
        result = jwt.encode(payload=payload, key=salt, algorithm="HS256", headers=headers)
        return jsonify({"code": 1000, "data": result})
    else:
        return jsonify({"code": 1001, "msg": "用户名或密码错误"})


@app.route("/index")
def index():
    token = request.args.get("token")
    print(token)
    RES = {
        "code": 1000,
        "msg": "success"
    }
    try:
        salt = "a5sd56a4sd65asd"
        verified_payload = jwt.decode(token, salt, True)
    except exceptions.ExpiredSignatureError:
        RES["code"] = 1001
        RES["msg"] = "TOKEN超时"
    except jwt.InvalidTokenError:
        RES["code"] = 1003,
        RES["msg"] = "TOKEN非法"
    except jwt.DecodeError:
        RES["code"] = 1002,
        RES["msg"] = "TOKEN认证失败"
    return jsonify(RES)


if __name__ == '__main__':
    app.run(debug=True)
