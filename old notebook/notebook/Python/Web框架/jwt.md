- 基于传统的token认证

  ```python
  用户登录，服务端返回token，并将token保存在服务的
  以后用户访问时，需要携带token，服务端获取token后，再去数据库校验
  ```

- jwt

  ```
  用户登录，服务端给用户返回一个token(服务端不保存)
  以后用户来访问，需要携带token，服务端获取token后，再做token校验
  ```

  

## jwt实现过程

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

- jwt生成的token是由三段字符串组成，并且用点连接

  - 第一段字符串，HEADER，内部包含算法/token类型。

    json转换成字符串并且用base64url加密

    ```
    {
      "alg": "HS256",
      "typ": "JWT"
    }
    ```

  - 第二段字符串PAYLOAD，自定义值

    ```
    {
      "sub": "1234567890",
      "name": "John Doe",
      "iat": 1516239022			# 超时时间
    }
    ```

  - 第三段字符串：

    对前两部分的密文进行Hash256进行加密，再对加密后的密文进行base64url加密

    ```
    HMACSHA256(
        base64UrlEncode(header) + "." +
        base64UrlEncode(payload),
        your-256-bit-secret
    )
    ```

- 以后用户再来访问时，需要携带token，后端对token进行校验

  - 获取token

  - 第一步：对token进行切割	

  - 第二步：对第二段对base64url进行解密，获取payload，检测超时时间

  - 第三步：对第一二段进行hash256加盐进行加密，并与第三段进行对比

    

## 使用

```python
pip3 install pyjwt
```

```python
import jwt
import time
from jwt import exceptions
from flask import Flask, jsonify, request


app = Flask(__name__)


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
            "iat": time.time(),  # 开始时间
            "exp": time.time() + 20, # 结束时间
            "data": {
                "user_id": 1,
                "nickname": "屁屁",
            }
        }
        result = jwt.encode(payload=payload, key=salt, algorithm="HS256", headers=headers)
        print(result)
        return jsonify({"code": 1000, "data": result.decode("utf-8")})
    else:
        return jsonify({"code": 1001, "msg": "用户名或密码错误"})


@app.route("/index")
def index():
    token = request.args.get("token")
    RES = {
        "code": 1000,
        "msg": "success"
    }
    try:
        salt = "a5sd56a4sd65asd"
        verified_payload = jwt.decode(jwt=token, key=salt, verify=True) # verify=True开启验证
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
```

