import React from "react";

import { AppBar, Toolbar, IconButton, Typography, Button } from "@material-ui/core";
import { Home as HomeIcon } from "@material-ui/icons";

const TopBar = ({ loggedIn }) => {

  if(loggedIn)
  {
    return(<></>);
  }
  else{
    return(
      <AppBar position="relative">
        <Toolbar>
          <IconButton href="/" style={{marginRight: 30}}>
            <HomeIcon/>
          </IconButton>
          <Typography variant="h6" style={{flexGrow: 1}}>
            IIITH Food Portal
          </Typography>
          <Button color="primary" variant="contained" href="/register" style={{marginRight: 30}}>
            Register
          </Button>
          <Button variant="contained" href="/login">
            Login
          </Button>
        </Toolbar>
      </AppBar>
    );
  }
}

export default TopBar;