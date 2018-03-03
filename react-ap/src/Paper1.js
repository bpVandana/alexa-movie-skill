import React from 'react';
import Paper from 'material-ui/Paper';

const style = {
  height: 60,
  width: 400,
  fontFamily: 'PT\ Sans-Serif',
  marginTop :10,
  textAlign: 'center',
  display: 'inline-block',
  backgroundColor:'#2E7D32',
  

paddingBottom:2,
  paddingTop:2
};

const Paper1= () => (
  <div>
    <Paper style={style} zDepth={1} rounded={false} >
     <p> Response and Time logs from Alexa</p>

    </Paper>

   
  </div>
);

export default Paper1;
