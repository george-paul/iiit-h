import React, { useState } from "react";

import { Typography, Container } from '@material-ui/core';
import { Button, Checkbox, TextField } from '@material-ui/core';
import { FormControlLabel } from "@material-ui/core";

import TopBar from "./TopBar";
import axios from "axios";

const LoginForm = () => {

  // false is for buyer, true is for 
  const [loginType, handleLoginTypeChange] = useState(false);
  const [emailValue, handleEmail] = useState('');
  const [passwordValue, handlePassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // alert("Username: " + usernameValue + "\nPassword: " + passwordValue + "\nVendor: " + loginType);
    if(emailValue === "" || passwordValue === "")
    {
      alert("Required fields are not filled!");
      return;
    }
    const newLogin = {
      email: emailValue,
      password: passwordValue
    }
    axios.get("http://localhost:5000/users/login", newLogin)
      .then(res => {
        console.log(res.data);
        alert("Logged in as " + newLogin.email);
      })
      .catch((err) => {
        console.log(newLogin);
        alert("Something went wrong! Login details incorrect");
        console.log(console.log("Error: ", err.message));
      });
  }

  return(
    <>
      <TopBar loggedIn={false}/>
      <main>
        <Container>
          <Typography variant="h1" style={{paddingTop: 20, paddingBottom:50}}>
            Login
          </Typography>
          <form noValidate autoComplete="off" onSubmit={handleSubmit}>
            <TextField
              label="Email"
              variant="outlined"
              style = {{paddingBottom: 10}}
              value={emailValue}
              onChange={(e) => handleEmail(e.target.value)}
            />
            <br/>
            <TextField
              label="Password"
              variant="outlined"
              style = {{paddingBottom: 30}}
              value={passwordValue}
              onChange={(e) => handlePassword(e.target.value)}
            />
            <br/>
            <FormControlLabel
              control = {
                <Checkbox
                  checked={loginType}
                  onChange={() => handleLoginTypeChange(!loginType)}
                  color="primary"
                />
              }
              label = "Are you a vendor?"
              style = {{paddingBottom: 30}}
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


export default LoginForm;