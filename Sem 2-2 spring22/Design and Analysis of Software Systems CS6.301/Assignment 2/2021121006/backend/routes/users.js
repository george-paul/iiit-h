const router = require("express").Router();
let User = require('../models/user.model');

router.route('/').get((req, res) => {
  User.find()
    .then(users => res.json(users))
    .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/create').post((req, res) => {
  const newUser = new User(req.body);

  newUser.save()
    .then(() => res.json("User added!"))
    .catch(err => res.status(400).json('Error: ' + err))
});

router.route('/login').get((req, res) => {

  console.log(req.body);
  User.findOne(req.body)
    .then(() => res.json("Found User"))
    .catch(err => res.status(400).json('Error (Could not find user): ' + err))
});

module.exports = router;