const path = require("path");
const express = require('express'),
    app = express();

const host = 'localhost';
const port = 8000;

app.get('/ping', (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'application/json');
    res.json({message: 'pong'});
});

renderIndex = (req, res) => {
    res.statusCode = 200;
    res.sendFile(path.join(__dirname + '/templates/index.html'));
}

app.get('/', renderIndex)
app.get('/profile', renderIndex)

app.use(express.static('static'));

app.listen(port, host, () => console.log(`Server listens http://${host}:${port}`));
