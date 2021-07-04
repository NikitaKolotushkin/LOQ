import React, {Component} from "react";
import {Link} from "react-router-dom";

export default class NavLinks extends Component {
    render() {
        return (
            <nav>
                <div className="nav__container">

                    <div className="nav__element">

                        <Link to="/visited">
                            <img src="/assets/img/visited.png" alt=""/>
                        </Link>
                    </div>
                    <div className="nav__element">
                        <Link to="/">
                            <img src="/assets/img/meets.png" alt=""/>
                        </Link>
                    </div>
                    <div className="nav__element">
                        <Link to="/profile">
                            <img src="/assets/img/profile.png" alt=""/>
                        </Link>
                    </div>
                </div>
            </nav>
        )
    }
}
