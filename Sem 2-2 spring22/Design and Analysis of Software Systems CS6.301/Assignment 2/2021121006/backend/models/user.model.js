const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const userSchema = new Schema(
{
  username: {
    type: String,
    required: true,
    trim: true,
    minlength: 3
  },
  password: {
    type: String,
    required: true,
    minlength: 3
  },
  email: {
    type: String,
    required: true,
    unique: true,
    trim: true,
    minlength: 3
  },
  phone: {
    type: String,
  },
  age: {
    type: Number,
  },
  batch: {
    type: String,
  },
},
{
  timestamps: true,
});

const User = mongoose.model("User", userSchema);

module.exports = User;