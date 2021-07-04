import React, {Component} from "react";
import ProfilePage from "./ProfilePage";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    Redirect,
} from "react-router-dom";
import MeetsPage from "./MeetsPage";
import NavLinks from "./NavLinks";
import VisitedPage from "./VisitedPage";

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        // return this.renderPage();
        return <Router>
            <Switch>
                <Route exact path="/" component={MeetsPage}/>
                <Route path="/profile" component={ProfilePage}/>
                <Route path="/visited" component={VisitedPage}/>
            </Switch>
            <NavLinks/>
        </Router>

    }
}
