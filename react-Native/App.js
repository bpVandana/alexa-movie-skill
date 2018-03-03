/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, { Component } from 'react';
import {
  Platform,
  StyleSheet,
  Text,
  View,AppRegistry
} from 'react-native';
import Home from './src/Home.js';
import Screen1 from './src/Screen1.js';




export default class App extends Component {
  render() {
    return <Home/>

  }
}
AppRegistry.registerComponent('movie',()=>App);
