const router = require("express").Router();
let Vendor = require('../models/vendor.model');

router.route('/').get((req, res) => {
  Vendor.find()
    .then(vendors => res.json(vendors))
    .catch(err => res.status(400).json('Error: ' + err));
});

module.exports = router;