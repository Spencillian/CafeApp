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
import Icon from 'react-native-vector-icons/AntDesign'
import * as React from 'react';


export default class Day extends React.Component{
    constructor(props){
        super(props)
        let queriedDay = props.day === undefined ? new Date().getDay() : props.day;
        this.state = {
            isLoading: true,
            data: {},
            todayNum: queriedDay,
            todayLit: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"][queriedDay],
            isQueried: !(props.day === undefined),
            nav: props.nav
        }
    }
    
    async componentDidMount(){
        try{
            const response = await fetch(`https://ed26af11.ngrok.io/cafeapi/food?day=${this.state.todayNum}`);
            const data = await response.json();
            this.setState({
                data: data,
                isLoading: false,
            });
        } catch (error){
            console.log(error);
            throw error
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
        
        if(!this.state.isQueried){
            return(
                <SafeAreaView style={styles.container}>
                    <SectionList 
                        contentContainerStyle={styles.contentContainer}
                        style={styles.sectionList}
                        sections={this.state.data}
                        keyExtractor={(item, index) => item + index}
                        renderItem={({ item }) => (
                            <Text style={styles.item}>  •    { item }</Text>
                        )}
                        renderSectionHeader={({ section: { title } }) => (
                            <Text style={styles.header}>{ title }</Text>
                        )}
                        ListHeaderComponent={
                            <View style={styles.sectionListHeaderBox}>
                                <Text style={styles.day}>{this.state.todayLit} - Today</Text>
                            </View>
                        }
                    />
                </SafeAreaView>
            );
        }

        return(
            <SafeAreaView style={styles.container}>
                <SectionList 
                    contentContainerStyle={styles.contentContainer}
                    style={styles.sectionList}
                    sections={this.state.data}
                    keyExtractor={(item, index) => item + index}
                    renderItem={({ item }) => (
                        <Text style={styles.item}>  •    { item }</Text>
                    )}
                    renderSectionHeader={({ section: { title } }) => (
                        <Text style={styles.header}>{ title }</Text>
                    )}
                    ListHeaderComponent={
                        <View style={styles.sectionListHeaderBox}>
                            <Text style={styles.day}>{this.state.todayLit}</Text>
                            <TouchableOpacity style={styles.backButton}
                                onPress={() => this.state.nav.navigate('Details')}
                            >
                                <Icon style={styles.icon} name='left' size={(Dimensions.get("window").height) * .065}/>
                            </TouchableOpacity>
                        </View>
                    }
                />
            </SafeAreaView>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
    },
    day: {
        fontSize: (Dimensions.get("window").width) * .11,
        flex: 6,
    },
    header: {
        fontSize: (Dimensions.get("window").width) * .085,
    },
    item:{
        fontSize: (Dimensions.get("window").width) * .048,
    },
    sectionList: {
        paddingTop: 10,
        paddingHorizontal: 20,
        flex: 1,
    },
    contentContainer: {
        paddingBottom: 30,
    },
    activityIndicator: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    backButton: {
        flex: 1
    },
    sectionListHeaderBox: {
        flexDirection: 'row',
        justifyContent: 'center',
        alignItems: 'center',
    },
})
