import React from "react";

import { Typography, Container } from '@material-ui/core';

import TopBar from "./TopBar";

const Home = () =>{

return(
  <>
    <TopBar loggedIn={false}/>
    <main>
      <div>
        <Container maxWidth="sm">
          <Typography  variant="h2" align="center" color="textPrimary" gutterBottom style={{paddingTop: 100}}>
            IIITH Food Portal
          </Typography>
          <Typography  variant="h5" align='center' color='textSecondary' paragraph>
            Login and order food from any vendor in IIITH
          </Typography>
        </Container>
      </div>
    </main>
  </>
);
}

export default Home;