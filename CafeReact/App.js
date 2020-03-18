import 'react-native-gesture-handler';
import * as React from 'react';
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import Day from './components/Day/Day';
// import Week from "./components/Week/Week";

function HomeScreen(){
    return(
        <Day/>
    );
}

const Stack = createStackNavigator()

function App(){
    return(
        <NavigationContainer>
            <Stack.Navigator initialRouteName="Home">
                <Stack.Screen
                    name="Home" component={HomeScreen}
                />
            </Stack.Navigator>
        </NavigationContainer>
    );
}

export default App;