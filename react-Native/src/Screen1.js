import React,{Component} from 'react';
import {Content,Text,
Container,
Button,
Header,
Footer,
Body,
Left,
Card,CardItem,
Right,
} from 'native-base';
import {Image,StyleSheet} from 'react-native';

export default class Screen1 extends Component{
  render(){
    return(
      <Container>

      <Content >
      <Card>
      <CardItem style={styles.container}>
      <Text style={{fontSize:55,fontWeight:'bold',color:'#154360'}}>Alexa: The Movie Db </Text>
      <Image source={require('../img/tmdb.png')} style={{width:200,height:200}}/>
      </CardItem>
      <CardItem>
      <Button large transparent onPress={ () => this.props.navigation.navigate("ScreenMain")}>
      <Text style={{color:'#154360'}}>Next</Text>
      </Button>
      </CardItem>
      </Card>
      </Content>
      </Container>

    );
  }
}

const styles = StyleSheet.create({
    container: {
    justifyContent:'center' ,
    alignItems:'center',
      flexDirection:'column' ,
      backgroundColor: '#FFFFFF',
      paddingTop:15,


    },

  });
