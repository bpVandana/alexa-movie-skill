import React from 'react';
import Paper from 'material-ui/Paper';

const style = {
  height: 100,
  width: 1000,
  fontFamily: 'PT\ Sans',
  fontSize :30,
  textAlign: 'center',
  display: 'inline-block',
  color:'#FFEA00'
};

const Navbar= () => (
  <div>
    <Paper style={style} zDepth={1} rounded={false} >
     <p> Welcome to Alexa Movie Suggestion Skills</p>
    </Paper>
   
  </div>
);

export default Navbar;
