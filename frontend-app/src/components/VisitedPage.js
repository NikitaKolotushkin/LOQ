import React, {Component} from "react";
import {Link} from "react-router-dom";

export default class VisitedPage extends Component {
    render() {
        return (
            <div>
                <div className="main__bg"></div>

                <section className="main_content">

                    <div className="container">
                        <h1 className="main__title">
                            Посещенные встречи
                        </h1>
                        <div className="content__block">
                            <h3 className="meet__title">
                                Ваша встреча:
                            </h3>
                            <p className="meet__adress">
                                Кафе "У Ашота" <br/>Улица Пушкина, Дом Колотушкина
                            </p>
                            <h3 className="meet__group">
                                Ваша компания:
                            </h3>
                            <div className="meet__peoples">
                                <div className="people">
                                    <img src="/assets/img/logo.jpg" alt="" className="avatar"/>
                                        <p className="name">
                                            Никита Колотушкин
                                        </p>
                                </div>
                                <div className="people">
                                    <img src="/assets/img/logo.jpg" alt="" className="avatar"/>
                                        <p className="name">
                                            Ашот Абобович
                                        </p>
                                </div>
                                <div className="people">
                                    <img src="/assets/img/logo.jpg" alt="" className="avatar"/>
                                        <p className="name">
                                            Даурбек Машинов
                                        </p>
                                </div>
                            </div>
                        </div>
                    </div>

                </section>

            </div>
        )
    }
}
