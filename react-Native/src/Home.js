import React, { Component } from 'react';

import { AppRegistry, StyleSheet, ActivityIndicator, ListView, Text, View, Alert } from 'react-native';
import {Container,Header,Button,Body,Content,Card,CardItem,Left,Thumbnail,Right} from 'native-base';
export default class Home extends Component {

  constructor(props) {
    super(props);
    this.state = {
      isLoading: true
    }
  }



  componentDidMount() {
    var url = "https://data.incipiently69.hasura-app.io/v1/query";
    console.log('Making data query (get logs )');
    var requestOptions = {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer f214defa75df22ab6c5dd2c471e2e25cd9a2e6dc30b4fb79"
        }
    };

    var body = {
        "type": "select",
        "args": {
            "table": "logs",
            "columns": [
                "*"
            ]
        }
    };

    requestOptions["body"] = JSON.stringify(body);
    console.log('Data Response ---------------------');

    fetch(url, requestOptions)

    .then(function(response) {
      return response.json();
    })

      .then((responseJson) => {
        let ds = new ListView.DataSource({rowHasChanged: (r1, r2) => r1 !== r2});
        this.setState({
          isLoading: false,
          dataSource: ds.cloneWithRows(responseJson),
        }, function() {
          // In this block you can do something with new state.
        });
      })
      .catch((error) => {
        console.error(error);
      });
  }

  ListViewItemSeparator = () => {
    return (
      <View
        style={{
          height: .5,
          width: "100%",
          backgroundColor: "#000",
        }}
      />
    );
  }


  render() {
    if (this.state.isLoading) {
      return (
        <View style={{flex: 1, paddingTop: 20}}>
          <ActivityIndicator />
        </View>
      );
    }

    return (
      <Container>
      <Header style={styles.head}>
      <Left>
      <Button transparent>
        <Thumbnail source={require('../img/tmdb.png')}/>
      </Button>
        </Left>
        <Text style={{color: 'white' , fontSize:20, paddingTop:10 }}>Alexa:TMDB</Text>
        <Right/>
      </Header>
      <View style={styles.MainContainer}>

        <ListView

          dataSource={this.state.dataSource}

          renderSeparator= {this.ListViewItemSeparator}
          renderRow={(rowData) => <Text style={styles.rowViewContainer}
          >Answer:  {rowData.answer}{"\n"}Response Time:  {rowData.response_time}{"\n"}Query:  {rowData.query_text}</Text>}



        />

      </View>
      </Container>
    );
  }
}

const styles = StyleSheet.create({

MainContainer :{

// Setting up View inside content in Vertically center.
justifyContent: 'center',
flex:1,
margin: 10

},

   rowViewContainer: {
        fontSize: 20,
        paddingRight: 10,
        paddingTop: 10,
        paddingBottom: 10,
        backgroundColor:'#D5F5E3',
        fontWeight:'bold',
      },
      head:{
        backgroundColor:'#2ECC71'

      },

});
