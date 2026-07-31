const express = require("express");

const app = express();

const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get("/health", (req, res) => {
    res.json({
        status: "UP"
    });
});

app.get("/ready", (req, res) => {
    res.json({
        ready: true
    });
});

app.get("/messages", (req, res) => {
    res.json({
        messages: [],
        source: "Cassandra"
    });
});

app.listen(PORT, () => {
    console.log(`Main App listening on port ${PORT}`);
});