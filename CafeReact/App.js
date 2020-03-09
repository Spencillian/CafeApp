import React, { Component } from "react";
import { View, Text, SectionList, StyleSheet } from "react-native";

export default class App extends Component{
  constructor(props){
    super(props)
    this.state = {}
  }

  componentDidMount(){
  }

  render(){
    return(
      <View style={styles.container}>
        <Text>
          
        </Text>
      </View>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  }
})