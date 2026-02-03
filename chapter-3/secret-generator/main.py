from bottle import route,run,template,request
import secrets

HTML= '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secret Generator</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0;
        }

        .card {
            background: #fff;
            padding: 25px 30px;
            border-radius: 12px;
            width: 360px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            text-align: center;
        }

        .card h2 {
            margin-bottom: 15px;
            color: #333;
        }

        .secret-box {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #f5f6fa;
            padding: 10px 12px;
            border-radius: 8px;
            margin-bottom: 15px;
            font-family: monospace;
            font-size: 14px;
            color: #2d3436;
            word-break: break-all;
        }

        .secret-text {
            max-width: 240px;
            overflow-wrap: anywhere;
        }

        button {
            background: #667eea;
            color: #fff;
            border: none;
            padding: 8px 14px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 14px;
            transition: background 0.3s ease;
        }

        button:hover {
            background: #5a67d8;
        }

        .copied {
            font-size: 13px;
            color: #27ae60;
            display: none;
            margin-top: 8px;
        }
    </style>
</head>
<body>

<div class="card">
    <h2>🔐 Secret Key</h2>

    <div class="secret-box">
        <span class="secret-text" id="secretKey">{{code}}</span>
        <button onclick="copySecret()">Copy</button>
    </div>

    <div class="copied" id="copiedMsg">✔ Copied to clipboard</div>
</div>

<script>
    function copySecret() {
        const secretText = document.getElementById("secretKey").innerText;
        navigator.clipboard.writeText(secretText).then(() => {
            const msg = document.getElementById("copiedMsg");
            msg.style.display = "block";

            setTimeout(() => {
                msg.style.display = "none";
            }, 2000);
        });
    }
</script>

</body>
</html>

'''


@route('/')
def index():
    length=32
    if query_len :=request.query.len:
        length=int(query_len)
    code=secrets.token_urlsafe(length)
    return template(HTML,code=code)

run(host="localhost",port=8080,debug=True,reloader=True)
