import React, {Component} from 'react';
import {View,Text} from 'react-native';
import {StackNavigator} from 'react-navigation';

import Screen1 from './Screen1';
import Home from './Home.js';

const StackRouter = StackNavigator({
    ScreenOne: {
        screen: Screen1,
    },
    ScreenMain: {
        screen: Home,
    },
  },
    {
        headerMode: "none"
    },
    {
        initialRouteName: 'ScreenMain',
      }
  )


export default StackRouter;
