import React, { useState } from "react";

import { Typography, Container } from '@material-ui/core';

import TopBar from "./TopBar";

const Profile = () => {
  return(
    <>
      <TopBar loggedIn={false}/>
      <main>
        <Container>
          <Typography variant="h1">
            Profile
          </Typography>
        </Container>
      </main>
    </>
  );
}

export default Profile;