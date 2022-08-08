import { createTheme } from '@material-ui/core/styles';

export const theme = createTheme({
  palette: {
    type: 'dark',
    primary: {
      main: '#6471b7',
    },
    secondary: {
      main: '#f50057',
    },
    background: {
      default: '#000000',
      paper: '#202020',
    },
  },
  overrides: {
    MuiAppBar: {
      colorInherit: {
        backgroundColor: '#689f38',
        color: '#fff',
      },
    },
  },
  props: {
    MuiAppBar: {
      color: '',
    },
  },
  typography: {
    h1: {
      fontFamily: 'Montserrat',
    },
    h2: {
      fontFamily: 'Montserrat',
    },
    h3: {
      fontFamily: 'Lato',
    },
    h4: {
      fontFamily: 'Lato',
    },
  },
});