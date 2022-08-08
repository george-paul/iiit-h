const express = require("express");
const cors = require ("cors");
const moongose = require("mongoose");

require("dotenv").config();

const app = express();
const port = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

// mongoDB connection
const uri = process.env.ATLAS_URI;
moongose.connect(uri, {  });
const connection = moongose.connection;
connection.once("open", () =>{
  console.log("MongoDB database connection established");
});

const usersRouter = require('./routes/users');
app.use('/users', usersRouter);
const vendorsRouter = require('./routes/vendors');
app.use('/vendors', vendorsRouter);

// start server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});