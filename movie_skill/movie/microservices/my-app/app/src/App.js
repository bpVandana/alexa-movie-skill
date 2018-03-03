import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import darkBaseTheme from 'material-ui/styles/baseThemes/darkBaseTheme';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import Request from './Request';
import Navbar from './navbar';
import Paper1 from './Paper1';
import color from 'material-ui/styles';


class App extends Component {
  render() {
    return (
       <MuiThemeProvider muiTheme={getMuiTheme(darkBaseTheme)}>
      <div className="App">
        <Navbar/>
        <Paper1/>
        <p className="App-intro">
         
        </p>
       
       <Request />

      </div>
       </MuiThemeProvider>
    );
  }
}

export default App;
