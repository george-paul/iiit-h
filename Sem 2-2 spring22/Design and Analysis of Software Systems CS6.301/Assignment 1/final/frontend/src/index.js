import React from 'react';
import ReactDOM from 'react-dom';
import { CssBaseline } from '@material-ui/core';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { ThemeProvider } from '@material-ui/styles';
import { theme } from './theme';

import Home from './components/Home';
import LoginForm from './components/LoginForm';
import Profile from './components/Profile';
import RegisterForm from './components/RegisterForm';

const App = () => {
  return(
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Home/>}/>
          <Route path='/login' element={<LoginForm/>}/>
          <Route path='/register' element={<RegisterForm/>}/>
          <Route path='/profile' element={<Profile/>}/>
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  );
}

ReactDOM.render(
  <App/>,
  document.getElementById("root")
);