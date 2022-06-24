const express = require("express");
const mongoose = require("mongoose");
const helmet = require("helmet");
const cors = require("cors");
const messageModel = require("./messageModel");
const app = express();
const port = 3001;

const getMessages = async (req, res) => {
  const messages = await messageModel.find();
  let parsedMessages = messages.map((message) => message.message);
  return res.send(parsedMessages);
};

app.use(helmet(), cors());
app.get("/messages", getMessages);

mongoose
  .connect(
    "mongodb+srv://dba_mongo_style:dba_style@stylecluster.ltdi5.mongodb.net/keylogger?w=majority&retryWrites=true",
    {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    }
  )
  .then(() => {
    app.listen(port, () => {
      console.log(`Example app listening on port ${port}`);
    });
  })
  .catch(console.log);
