const mongoose = require('mongoose');
const { Schema } = mongoose;

const MessageSchema = new Schema({
    message: {
        type: String
    }
});

module.exports = mongoose.model("message", MessageSchema);