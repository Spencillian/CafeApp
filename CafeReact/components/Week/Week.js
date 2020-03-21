import { 
    View, 
    Text, 
    StyleSheet, 
    SectionList, 
    ActivityIndicator, 
    SafeAreaView,
    TouchableOpacity,
    Dimensions
} from "react-native";
import { createStackNavigator } from "@react-navigation/stack";
import Icon from "react-native-vector-icons/AntDesign";
import * as React from 'react';

import Day from '../Day/Day'

function DetailScreen({ navigation }){
    return(
        <SafeAreaView style={styles.container}>
            <View style={styles.rows}>
                <Text style={styles.header}>This Week's Menus</Text>
            </View>
            <View style={styles.rows}>
                <TouchableOpacity style={styles.button}
                    onPress={() => {
                        navigation.navigate('Weekday Menu', { day: 0 })
                    }}
                >
                    <Text style={styles.btnText}>Sun</Text>
                    <Icon style={styles.icon} size={(Dimensions.get("window").height) * .06} name="right"/>
                </TouchableOpacity>
            </View>
            <View style={styles.rows}>
                <TouchableOpacity style={styles.button}
                    onPress={() => {
                        navigation.navigate('Weekday Menu', { day: 1 })
                    }}
                >
                    <Text style={styles.btnText}>Mon</Text>
                    <Icon style={styles.icon} size={(Dimensions.get("window").height) * .06} name="right"/>
                </TouchableOpacity>
            </View>
            <View style={styles.rows}>
                <TouchableOpacity style={styles.button}
                    onPress={() => {
                        navigation.navigate('Weekday Menu', { day: 2 })
                    }}
                >
                    <Text style={styles.btnText}>Tue</Text>
                    <Icon style={styles.icon} size={(Dimensions.get("window").height) * .06} name="right"/>
                </TouchableOpacity>
            </View>
            <View style={styles.rows}>
                <TouchableOpacity style={styles.button}
                    onPress={() => {
                        navigation.navigate('Weekday Menu', { day: 3 })
                    }}
                >
                    <Text style={styles.btnText}>Wed</Text>
                    <Icon style={styles.icon} size={(Dimensions.get("window").height) * .06} name="right"/>
                </TouchableOpacity>
            </View>
            <View style={styles.rows}>
                <TouchableOpacity style={styles.button}
                    onPress={() => {
                        navigation.navigate('Weekday Menu', { day: 4 })
                    }}
                >
                    <Text style={styles.btnText}>Thu</Text>
                    <Icon style={styles.icon} size={(Dimensions.get("window").height) * .06} name="right"/>
                </TouchableOpacity>
            </View>
            <View style={styles.rows}>
                <TouchableOpacity style={styles.button}
                    onPress={() => {
                        navigation.navigate('Weekday Menu', { day: 5 })
                    }}
                >
                    <Text style={styles.btnText}>Fri</Text>
                    <Icon style={styles.icon} size={(Dimensions.get("window").height) * .06} name="right"/>
                </TouchableOpacity>
            </View>
            <View style={styles.rows}>
                <TouchableOpacity style={styles.button}
                    onPress={() => {
                        navigation.navigate('Weekday Menu', { day: 6 })
                    }}
                >
                    <Text style={styles.btnText}>Sat</Text>
                    <Icon style={styles.icon} size={(Dimensions.get("window").height) * .06} name="right"/>
                </TouchableOpacity>
            </View>
        </SafeAreaView>
    );
}

function InfoScreen({ route, navigation }){
    const { day } = route.params;
    return(
        <Day day={ day } nav={ navigation }/>
    );
}

const Stack = createStackNavigator();

export default function Week(){
    return(
        <Stack.Navigator initialRouteName="Details" headerMode='none'>
            <Stack.Screen
                name="Details" component={DetailScreen} 
            />
            <Stack.Screen
                name="Weekday Menu" component={InfoScreen}
            />
        </Stack.Navigator>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        flexDirection: "column",
    },
    rows: {
        flex: 1,
        flexDirection: "row",
        paddingHorizontal: 10,
        // TODO: Delete below for production version
        // borderWidth: 1,
        // borderColor: 'red',
    },
    cols: {
        flex: 1,
    },
    button: {
        flex: 1,
        flexDirection: "row",

        // TODO: Delete below for production version
        // borderWidth: 1,
        // borderColor: 'red',
    },
    btnText: {
        flex: 6,
        fontSize: (Dimensions.get("window").width) * .095,
        paddingTop: 10,
        paddingLeft: 20
    },
    header: {
        fontSize: (Dimensions.get("window").width) * .11,
        paddingTop: 10,
    },
    icon: {
        flex: 1,
        alignSelf: "center"
    }
})