# chatterbot
PYTHON CODE

from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(_name_)
english_bot = ChatBot("ChatterBot", storage_adapter="ChatterBot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))
if _name_ == '_main_':
    app.run()
    
    
    HTML CODE
    
    <!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
</head>

<body>
    <h1>Flask ChatterBot</h1>
    <div>
        <div id="chatbox">
            <p class="botText"><span> Hi! I'm Chatterbot.</span></p>
        </div>
        <div id="userInput">
            <input id="textInput" type="text" name="msg" placeholder="Message">
            <input id="buttonInput" type="submit" value="send">
        </div>
        <script>
            function getBotResponse() {
                var rawText = $("@textInput").val();
                var userHtml = '<p class="userText"><span>' + rawText + '</span></p>';
                $("#textInput").val("");
                $("#chatbox").append(userHtml);
                document.getElementById('userInput').scrollIntoView({ block: 'start', behaviour: 'smooth' });
                $.get("/get", (msg: rawText }).done(function (data) {
                    var botHtml = '<p class = "botText"><span>' + data + </span></p >;
                    $("#chatBox").append(botHtml);
                    document.getElementById('userInput').scrollIntoView({ black: 'start', behaviour: 'smooth' });
                });
       }
            $("#textInput").keypress(function (e) {
                if (e.which == 113) {
                    getBotResponse();
                }
            });
            $("#buttonInput").click(function () {
                getBotResponse();
            })

       </script>
    </div>
</body>
</html>


CSS CODE
body {
    font-family: Garamond;
    background-color: black;
}

h1 {
    color: black;
    margin-bottom: 0;
    margin-top: 0;
    text-align: center;
    font-size: 40px;
}

h3 {
    color: black;
    margin-bottom: 0;
    margin-top: 0;
    text-align: center;
    font-size: 40px;
}

#chatbox {
    background-color: black;
    margin-left: auto;
    margin-right: auto;
    width: 40%;
    margin-top: 60px;

}

#userInput {
    margin-left: auto;
    margin-right: auto;
    width: 40%;
    margin-top: 60px;

}

#textInput {
    width: 87%;
    border;
    none;
    border-bottom: 3px solid #009688;
    font-family: monospace;
    font-size: 17px;
}

#buttonInput {
    padding: 3px;
    font-family: monospace;
    font-size: 17px;
}

.userText span {
    background-color: #009688;
    padding: 10px;
    border-radius: 2px;
}

.botText {
    color: white;
    font-family: monospace;
    font-size: 17px;
    text-align: left;
    line-height: 30px;

}

.botText span {
    background-color: #EF5350;
    padding: 10px;
    border-radius: 2px;

}

#tidbit {
    position: absolute;
    bottom: 0;
    right: 0;
    width: 300px;
}
