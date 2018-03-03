import React from 'react';

import { render } from 'react-dom';
import {Router, Route} from 'react-router';
import axios from 'axios';
import Paper from 'material-ui/Paper';
import color from 'material-ui/styles';

import createTypography from 'material-ui/styles/typography';
const style = {
  height: 1100,
  width: 400,
  padding :5,
  paddingTop :8,
  marginTop: -10,
  color:'#D84315',
  backgroundColor:'#212121',
  fontFamily: 'PT\ Sans',
  textAlign: 'center',
  display: 'inline-block',
  fontSize :20,textAlign: 'center',
 


  
};

class Requests extends React.Component{
  constructor(){
    super();
    this.state = {
        table:[]
    }

  }


componentDidMount(){
    //console.log('Success!');
  

  var url = "https://data.incipiently69.hasura-app.io/v1/query";
var requestOptions = {
    "method": "POST",
    "headers": {
        "Content-Type": "application/json"
    }
};
// If you have the auth token saved in offline storage
// var authToken = window.localStorage.getItem('HASURA_AUTH_TOKEN');
// headers = { "Authorization" : "Bearer " + authToken }
  var body = {
          "type": "select",
          "args": {
              "table": "logs",
              "columns": [
                  "*"
              ]
          }
};
requestOptions.body = JSON.stringify(body);
  



axios.post(url,requestOptions.body )
  .then((response) => {
   console.log(response.data);
   const arr = response.data.map((element)=>({answer:element.answer,error:element.error,response_time:element.response_time,query_text:element.query_text}));
   console.log(arr)
   this.setState({table:arr});
   
  })
  .catch(function(error) {
  console.log('Request Failed:' + error);
});
  

  
}

render(){
    let count =0 ;
    return(
      <div>
          <Paper style={style} zDepth={1} rounded={false} >
            <table>
         
          
          <tr>{this.state.table.map(e=>(<p key={count++}> {e.answer}</p>))}</tr>
        
          </table>

          </Paper>
          
          <Paper style={style} zDepth={1} rounded={false} >
            <table>
         
          
          
          <tr>{this.state.table.map(e=>(<p key={count++}> {e.response_time}</p>))}</tr>
            <br/>
            <br/>
        
          


          </table>

          </Paper>
          
          

          

      </div>
    );
  }
}


export default Requests;
