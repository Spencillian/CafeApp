import 'react-native-gesture-handler';
import * as React from 'react';
import { NavigationContainer } from "@react-navigation/native";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import Icon from "react-native-vector-icons/FontAwesome";

import Day from './components/Day/Day';
import Week from './components/Week/Week';

function HomeScreen(){
    return(
        <Day/>
    );
}

function DetailScreen(){
    return (
        <Week />
    );
}

const Tab = createBottomTabNavigator();

function App(){
    return(
        <NavigationContainer>
            <Tab.Navigator initialRouteName="Home">
                <Tab.Screen
                    name="Home" component={HomeScreen}
                    options={{
                        tabBarLabel: "Today",
                        tabBarIcon: ({ color, size}) => (
                            <Icon name="th-list" color={color} size={size}/>
                        ),
                    }}
                />
                <Tab.Screen
                    name="Week" component={DetailScreen}
                    options={{
                        tabBarLabel: "This Week",
                        tabBarIcon: ({ color, size}) => (
                            <Icon name="th" color={color} size={size}/>
                        ),
                    }}
                />
            </Tab.Navigator>
        </NavigationContainer>
    );
}

export default App;