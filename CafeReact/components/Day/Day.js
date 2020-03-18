import { View, Text, StyleSheet, SectionList, ActivityIndicator } from "react-native";
import * as React from 'react';


export default class Day extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            isLoading: true,
            data: {},
        }
    }
    
    async componentDidMount(){
        try{
            const response = await fetch('https://b8ce0c62.ngrok.io/cafeapi/food?day=3');
            const data = await response.json();
            // console.log(data);
            this.setState({
                data: data,
                isLoading: false,
            });
        } catch (err){
            console.log(error);
        }
    }

    render(){

        if(this.state.isLoading){
            return(
                <View style={styles.activityIndicator}>
                    <ActivityIndicator />
                </View>
            );
        }
        
        console.log(this.state.data)
        return(
            <View style={styles.container}>
                <Text style={styles.day}>Wed</Text>
                <SectionList 
                    sections={this.state.data}
                    keyExtractor={(item, index) => item + index}
                    renderItem={({ item }) => (
                    <Text>{ item }</Text>
                    )}
                    renderSectionHeader={({ section: { title } }) => (
                        <Text style={styles.header}>{ title }</Text>
                    )}
                />
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
    },
    day: {
        fontSize: 40,
        fontWeight: "700",
        flex: 1,
        paddingHorizontal: 20,
        paddingTop: 15,
    },
    foodList: {
        flex: 6,
    },
    activityIndicator: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    header: {
        fontSize: 32,
    }
})
