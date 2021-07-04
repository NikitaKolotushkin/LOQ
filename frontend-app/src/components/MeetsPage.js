import React, {Component} from "react";
import {Link} from "react-router-dom";

export default class MeetsPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            time: "-",
        };
        fetch('http://127.0.0.1:5000/time')
            .then((response) => response.json())
            .then((data) => {
                this.setState({
                    time: data.time
                })
                console.log(data.time)
            });
    }

    render() {
        return (
            <div>
                <div className="main__bg"/>

                <section className="main_content">
                    <div className="container">
                        <h1 className="main__title">Подбор встречи</h1>
                        <div className="map"/>
                    </div>
                    <div className="small_container">
                        <h2 className="range__title">Радиус поиска</h2>
                        <input type="range" name="" className="range__selector selector"/>
                        <hr/>
                        <h2 className="novelty__title">Степень новизны</h2>
                        <input type="range" className="novelty__selector selector"/>
                        <p className="novelty__description">всегда должно быть что-то знакомое</p>
                        <h2 className="price__title">Цена {this.state.time}</h2>
                        <input type="range" className="price__selector"/>
                        <hr/>
                        <div className="lists-row">
                            <select name="payment" id="">
                                <option disabled selected value="0">Способ оплаты</option>
                            </select>
                            <select name="date" id="">
                                <option disabled selected value="0">Время и дата</option>
                                <option value="123">Hehehe</option>
                            </select>
                        </div>
                        <hr/>
                        <input type="submit" value="Подобрать встречу"
                               className="meet__button"/>
                    </div>
                </section>

            </div>
        );
    }
}
