const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const vendorSchema = new Schema(
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
  managerName: {
    type: String,
    trim: true,
    minlength: 3
  },
  shopName: {
    type: String,
    required: true,
    trim: true,
    minlength: 3
  },
  openClose: {
    type: String,
    required: true,
    trim: true,
  },
},
{
  timestamps: true,
});

const Vendor = mongoose.model("Vendor", vendorSchema);

module.exports = Vendor;