import React, { useState } from "react";

import { Typography, Container } from '@material-ui/core';
import { Button, TextField } from '@material-ui/core';

import axios from "axios";

import TopBar from "./TopBar";

const RegisterForm = () => {

  // false is for buyer, true is for 
  const [usernameValue, handleUsername] = useState('');
  const [passwordValue, handlePassword] = useState('');
  const [emailValue, handleEmail] = useState('');
  const [phoneValue, handlePhone] = useState('');
  const [ageValue, handleAge] = useState('');
  const [batchValue, handleBatch] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // alert("username: " + usernameValue + "\npassword: " + passwordValue + "\nemail: " + emailValue + "\nphone: " + phoneValue + "\nage: " + ageValue + "\nbatch: " + batchValue );
    if(usernameValue === "" || passwordValue === "" || emailValue === "")
    {
      alert("Required fields (marked with *) are not filled!");
      return;
    }

    const newUser = {
      username: usernameValue,
      password: passwordValue,
      email: emailValue,
      phone: phoneValue,
      age: parseInt(ageValue),
      batch: batchValue
    }

    axios.post("/api/users/create", newUser)
      .then(res => {
        console.log(res.data);
        alert("Registered new user and logged in as " + newUser.username);
      })
      .catch((err) => {
        alert("Something went wrong! Check whether email is already registered or phone number is already registered");
        console.log(console.log("Error: ", err.message));
      });
  }

  return(
    <>
      <TopBar loggedIn={false}/>
      <main>
        <Container>
          <Typography variant="h1" style={{paddingTop: 20, paddingBottom:50}}>
            Register a new User
          </Typography>
          <form noValidate autoComplete="off" onSubmit={handleSubmit}>
            <TextField
              required
              fullWidth={true}
              label="Username"
              variant="outlined"
              style = {{marginBottom: 10}}
              value={usernameValue}
              onChange={(e) => handleUsername(e.target.value)}
            />
            <br/>
            <TextField
              required
              fullWidth={true}
              label="Password"
              variant="outlined"
              style = {{marginBottom: 10}}
              value={passwordValue}
              onChange={(e) => handlePassword(e.target.value)}
            />
            <br/>
            <TextField
              required
              fullWidth={true}
              label="Email"
              variant="outlined"
              style = {{marginBottom: 10}}
              value={emailValue}
              onChange={(e) => handleEmail(e.target.value)}
            />
            <br/>
            <TextField
              label="Phone"
              variant="outlined"
              style = {{marginBottom: 10, marginRight: 30}}
              value={phoneValue}
              onChange={(e) => handlePhone(e.target.value)}
            />
            <TextField
              type="number"
              InputProps={{
                inputProps:{
                  min: 0
                }
              }}
              label="Age"
              variant="outlined"
              style = {{marginBottom: 10, marginRight: 30}}
              value={ageValue}
              onChange={(e) => handleAge(e.target.value)}
            />
            <TextField
              label="Batch"
              variant="outlined"
              style = {{marginBottom: 10, marginRight: 30}}
              value={batchValue}
              onChange={(e) => handleBatch(e.target.value)}
            />
            <br/>
            <Button 
              type="submit"
              variant="contained"
              color="primary"
              // href="./profile"
            >
              Submit
            </Button>
          </form>
        </Container>
      </main>
    </>
  );
}


export default RegisterForm;